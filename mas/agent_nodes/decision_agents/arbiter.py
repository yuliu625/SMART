"""
仲裁者。

查看recognizer和validator分析过程，做出最终决策。
"""

from __future__ import annotations

from mas.agent_nodes.base_agent import BaseAgent
from mas.schemas.structured_output_format import ArbiterDecision
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from pydantic import BaseModel


class Arbiter(BaseAgent):
    """
    执行最终仲裁决定。

    是LRM。
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
        state: DecisionState,
        config: RunnableConfig,
    ) -> dict:
        # 合并所有的讨论记录。
        decision_shared_content = self.merge_decision_shared_messages(
            decision_shared_messages=state.decision_shared_messages,
        )
        arbiter_result = self.arbitrate(
            decision_shared_content=decision_shared_content,
        )
        return dict(
            decision_shared_messages=decision_shared_messages,
            current_agent_name='validator',
        )

    # ====主要方法。====
    async def arbitrate(
        self,
        decision_shared_content: str,
    ) -> dict:
        # 获取llm响应。
        response = await self.a_call_llm_with_retry(
            messages=[
                HumanMessage(content=decision_shared_content),
            ],
        )
        # 提取最终结论。
        arbiter_decision = self.get_structured_output(raw_str=response.content)
        return dict(
            decision_shared_messages=decision_shared_messages + [response],
            arbiter_decision=arbiter_decision,
        )

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
            merged_content += '\n\n'
        return merged_content

