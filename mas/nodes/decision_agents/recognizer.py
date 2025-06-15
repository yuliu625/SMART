"""
识别者。
"""

from __future__ import annotations

from mas.nodes.base_agent import BaseAgent
from mas.schemas.structured_output_format import AgentProcessedResult

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import AnyMessage, AIMessage


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
        chat_prompt_template: ChatPromptTemplate,
        llm: BaseChatModel,
    ):
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            llm=llm,
            max_retries=10,
            is_need_structured_output=False,
            schema_pydantic_base_model=None,
            schema_check_type='dict',
        )

    def process_state(
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
        recognizer_result = self.recognize(original_pdf_text=state.original_pdf_text)
        return {
            'shared_chat_history': recognizer_result.chat_history,
            'current_agent_name': 'validator',
        }

    def recognize(
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
        response = self.call_llm_with_retry(chat_history=[HumanMessage(content=original_pdf_text)])
        # 获得共享的chat-history。
        shared_chat_history = self.get_initial_shared_chat_history(recognizer_response=response)
        return AgentProcessedResult(
            chat_history=shared_chat_history,
            agent_request=None,
        )

    def get_initial_shared_chat_history(
        self,
        recognizer_response: AIMessage,
    ) -> list[AnyMessage]:
        """
        将recognizer初始识别的结果转换，封装为初始shared-chat-history。

        Args:
            recognizer_response (AIMessage): recognizer初始识别的结果。

        Returns:
            list[AnyMessage]: chat-history。
                这个专用方法实际返回的是shared-chat-history，为list[HumanMessage]，仅一条初始的human-message。
        """
        # 标注身份。
        arbiter_first_message_context = self.wrap_message_content_with_agent_name(
            agent_name='recognizer',
            original_content=recognizer_response.content,
        )
        # 构建chat-history。
        shared_chat_history = [HumanMessage(content=arbiter_first_message_context)]
        return shared_chat_history

