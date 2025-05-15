"""
识别者。
"""

from ...states import MASState
from ..base_agent import BaseAgent

from langchain_core.runnables import Runnable
from pydantic import BaseModel


class Recognizer(BaseAgent):
    """

    """
    def __init__(
        self,
        llm_chain: Runnable,
    ):
        super().__init__(
            llm_chain=llm_chain,
        )

    def run(self, state: MASState):
        ...

