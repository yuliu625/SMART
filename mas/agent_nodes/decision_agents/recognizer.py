"""
识别者。
"""

from __future__ import annotations

from mas.schemas.structured_output_format import AgentProcessedResult
from mas.agent_nodes.base_agent import BaseAgent
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, AIMessage, SystemMessage


class Recognizer(BaseAgent):
    """
    整体公司风险识别者。

    长文档阅读能力。

    进行:
        - 读取原始文本内容，识别公司架构。
        - 初步识别风险，分派验证任务。

    架构:
        - 在MAS中的decision模块。
        - 在整个MAS开始，仅运行一次。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
    ):
        # 基本的agent，不对于输出进行限制。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 不需要结构化输出。
            is_need_structured_output=False,
            formatter_llm=None,
            schema_pydantic_base_model=None,
            formatter_llm_system_message=None,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: DecisionState,
        config: RunnableConfig,
    ) -> dict:
        """
        由于recognizer为初始化运行且仅运行一次，recognizer不专门设置chat-history，并自己完成chat-history转换过程。

        Args:
            state (DecisionState): 使用的state。需要字段:
                - original_pdf_text: 原始文档的文本信息。
            config (RunnableConfig): 运行设置。

        Returns:
            dict: 进行更新的字段，包括:
                - shared_chat_history: 初始化的shared-chat-history。
                - current_agent_name: 下一个运行的agent。冗余字段，固定边一定指向 'validator'。
        """
        recognizer_response = await self.recognize_original_pdf_text(
            original_pdf_text=state.original_pdf_text,
        )
        # 获得共享的memory。
        decision_shared_messages = self.initiate_decision_shared_messages(
            recognizer_message=recognizer_response['ai_message'],  # 这里的response只需要ai_message。
        )
        return dict(
            decision_shared_messages=decision_shared_messages,
            current_agent_name='validator',
        )

    # ====主要方法。====
    async def recognize_original_pdf_text(
        self,
        original_pdf_text: str,
    ) -> AgentProcessedResult:
        """
        读取原始文档的文本，以decision模块的shared-chat-history返回。

        Args:
            original_pdf_text (str): 原始文档的文本信息。

        Returns:
            AgentProcessedResult: 初始化的shared-chat-history。agent_request为空。
        """
        # 对于初始pdf的文本内容进行分析。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
                HumanMessage(content=original_pdf_text),
            ],
        )
        return AgentProcessedResult(
            messages=response['ai_message'],
            agent_request='validator',  # 并没有发出请求，但是下一个一定是validator。
        )

    # ====工具方法。====
    def initiate_decision_shared_messages(
        self,
        recognizer_message: AIMessage,
    ) -> list[AnyMessage]:
        """
        将recognizer初始识别的结果转换，封装为初始shared-chat-history。

        Args:
            recognizer_message (AIMessage): recognizer初始识别的结果。

        Returns:
            list[AnyMessage]: chat-history。
                这个专用方法实际返回的是shared-chat-history，为list[HumanMessage]，仅一条初始的human-message。
        """
        assert isinstance(recognizer_message, AIMessage)
        # 标注身份。
        arbiter_first_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='Recognizer',
            original_text=recognizer_message.content,
        )
        # 构建chat-history。
        decision_shared_messages = [
            HumanMessage(content=arbiter_first_message_content),  # 把recognizer的信息放进去。
        ]
        return decision_shared_messages

