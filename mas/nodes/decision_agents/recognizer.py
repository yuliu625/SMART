"""
识别者。
"""

from __future__ import annotations

from ..base_agent import BaseAgent

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate


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

    def process_state(self, state: DecisionState) -> dict:
        arbiter_context = self.recognize(original_pdf_text=state.original_pdf_text)
        shared_chat_history = [HumanMessage(content=arbiter_context)]
        return {
            'shared_chat_history': shared_chat_history,
        }

    def recognize(
        self,
        original_pdf_text: str,
    ) -> str:
        # 对于初始pdf的文本内容进行分析。
        response = self.call_llm_with_retry(chat_history=[HumanMessage(content=original_pdf_text)])
        # 标注身份。
        arbiter_context = (
            "<!--recognizer-start-->\n\n"
            + response.content
            + "\n\n<!--recognizer-end-->"
        )
        return arbiter_context

