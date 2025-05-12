"""
识别者。
"""

from ...states import MASState

from langchain_core.runnables import Runnable


class Recognizer:
    def __init__(
        self,
        llm_chain: Runnable,
    ):
        self.llm_chain = llm_chain

    def run(self, state: MASState):
        ...

