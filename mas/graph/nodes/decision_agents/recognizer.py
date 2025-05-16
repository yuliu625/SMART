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
        # 对于初始pdf的文本内容进行分析。
        response = self.call_llm_chain(chat_history=[HumanMessage(state.original_pdf_text)])
        # 标注身份。
        arbiter_context = [(
                "<!--recognizer-start-->\n\n"
                + response.content
                + "\n\n<!--recognizer-end-->"
        )]
        validator_chat_history = [HumanMessage(content=arbiter_context)]
        return {
            'validator_chat_history': validator_chat_history,
            'arbiter_contex': arbiter_context,
        }

