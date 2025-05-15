"""
识别者。
"""

from ...states import MASState
from ..base_agent import BaseAgent

from langchain_core.messages import HumanMessage

from langchain_core.runnables import Runnable


class Recognizer(BaseAgent):
    """
    整体公司风险识别者。

    长文档阅读能力。
    """
    def __init__(
        self,
        llm_chain: Runnable,
    ):
        super().__init__(
            llm_chain=llm_chain,
        )

    def run(self, state: MASState):
        response = self.call_llm_chain(chat_history=[HumanMessage(state.original_pdf_text)])
        validator_chat_history = [HumanMessage(content=response.content)]
        arbiter_contex = [(
            "<!--recognizer-start-->"
            + response.content
            + "<!--recognizer-end-->"
        )]
        return {
            'validator_chat_history': validator_chat_history,
            'arbiter_contex': arbiter_contex,
        }

