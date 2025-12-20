"""
仲裁者。

查看recognizer和validator分析过程，做出最终决策。
"""

from __future__ import annotations

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
# from mas.schemas.structured_output_format import ArbiterDecision
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.mas_state import MASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from pydantic import BaseModel


class Adjudicator(BaseAgent):
    """
    执行最终仲裁决定。

    约定是LRM。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        # formatter相关，对于这个agent可以以不是必需的方法来实现。
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ):
        # 方案1: 基本的agent，不对于输出进行限制。 最终的决策结果由独立方法统一处理。(这里是否有结构化输出并不影响MAS运行。)
        # super().__init__(
        #     main_llm=main_llm,
        #     main_llm_system_message=main_llm_system_message,
        #     main_llm_max_retries=3,
        #     # 不需要结构化输出。
        #     is_need_structured_output=False,
        #     formatter_llm=None,
        #     schema_pydantic_base_model=None,
        #     formatter_llm_system_message=None,
        #     formatter_llm_max_retries=3,
        # )
        # 方案2: 需要显式做出最终决策的agent。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 需要结构化输出。
            is_need_structured_output=True,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: MASState,
        config: RunnableConfig,
    ) -> dict:
        """
        整个MAS的终点，将全部的decision_shared_messages交给Arbiter进行分析和做出最终决策。

        Args:
            state (DecisionState): 使用的state。需要字段:
                - decision_shared_messages: 再arbiter之前全部的分析。
            config (RunnableConfig): 运行设置。

        Returns:
            dict: 进行更新的字段，包括:
                - decision_shared_messages: 完整的decision_shared_messages。
                - final_decision: 最终完整的analysis and decision。
                - current_agent_name: 下一个运行的agent。冗余字段，固定边一定指向 'end'。系统不会再运行。
        """
        # 合并所有的讨论记录。
        # before call arbiter llm
        decision_shared_content = self.merge_decision_shared_messages(
            decision_shared_messages=state.decision_shared_messages,
        )
        # 执行最终决定。
        adjudicator_result = await self.review_report(
            decision_shared_content=decision_shared_content,
        )
        # final decision shared message
        # after call arbiter llm
        final_decision_shared_messages = self.process_final_decision(
            adjudicator_message=adjudicator_result.ai_message,
            decision_shared_messages=state.decision_shared_messages,
        )
        return dict(
            decision_shared_messages=final_decision_shared_messages,
            final_decision=adjudicator_result.structured_output,
            current_agent_name='end',
        )

    # ====主要方法。====
    async def review_report(
        self,
        decision_shared_content: str,  # 特殊初始情况，直接输入string。
    ) -> BaseAgentResponse:
        # 获取llm响应。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
                HumanMessage(content=decision_shared_content),  # 这一条HumanMessage已包括全部的messages。
            ],
        )
        return response

    # ====工具方法。====
    def merge_decision_shared_messages(
        self,
        decision_shared_messages: list[AnyMessage],
    ) -> str:
        """
        不处理原始的分析过程的情况下，自我合并信息。

        Args:
            decision_shared_messages (list[AnyMessage]): 全部的决策层级的messages。

        Returns:
            str: 合并后的文本信息。
        """
        merged_content = ""  # '\n\n'.join(message.content for message in chat_history)
        for message in decision_shared_messages:
            merged_content += message.content
            merged_content += "\n\n以上是原始文档的简要情况和全部的分析情况。现在，对该公司的情况做出最终的总结和判别。"
        return merged_content

    # ====工具方法。====
    def process_final_decision(
        self,
        adjudicator_message: AIMessage,
        decision_shared_messages: list[AnyMessage],
    ) -> list[AnyMessage]:
        """
        为保证统一性，将最后的adjudicator的message也使用ContentAnnotator进行处理。
        对于shared_messages，adjudicator实际并不参与，这个方法仅为保证规范性进行统一整理。

        Args:
            adjudicator_message (AIMessage): Adjudicator的message。但是没有标记tag。
            decision_shared_messages (list[AnyMessage]): 在Adjudicator之前的decision_shared_messages。

        Returns:
            list[AnyMessage]: Adjudicator的message被标记，全部完整的decision_shared_messages。
        """
        assert isinstance(adjudicator_message, AIMessage)
        # 标注身份。
        adjudicator_last_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='adjudicator',
            original_text=adjudicator_message.content,
        )
        # 构建decision_shared_messages。
        decision_shared_messages = decision_shared_messages + [
            HumanMessage(content=adjudicator_last_message_content),  # 标准化记录adjudicator的信息。
        ]
        return decision_shared_messages

