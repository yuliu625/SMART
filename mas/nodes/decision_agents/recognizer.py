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
        recognizer_result = self.recognize(original_pdf_text=state.original_pdf_text)
        return {
            'shared_chat_history': recognizer_result.chat_history,
        }

    def recognize(
        self,
        original_pdf_text: str,
    ) -> AgentProcessedResult:
        # 对于初始pdf的文本内容进行分析。
        response = self.call_llm_with_retry(chat_history=[HumanMessage(content=original_pdf_text)])
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
        将封装的方法

        Args:
            recognizer_response:

        Returns:

        """
        # 标注身份。
        arbiter_first_message_context = self.wrap_message_content_with_agent_name(
            agent_name='recognizer',
            original_content=recognizer_response.content,
        )
        # 构建chat-history
        shared_chat_history = [HumanMessage(content=arbiter_first_message_context)]
        return shared_chat_history

