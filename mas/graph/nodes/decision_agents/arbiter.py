"""
仲裁者。
"""

from ...states import MASState
from ..base_agent import BaseAgent
from mas.utils import JsonOutputParser

from langchain_core.runnables import Runnable
from pydantic import BaseModel
from langchain_core.messages import AIMessage


class Arbiter(BaseAgent):
    """

    """
    def __init__(
        self,
        llm_chain: Runnable,
        structured_output_format: type[BaseModel],
    ):
        super().__init__(
            llm_chain=llm_chain,
            is_need_structured_output=True,
            structured_output_format=structured_output_format,
        )
        self.llm_chain = llm_chain

    def run(self, state: MASState):
        ...

    def arbitrate(self, state: MASState):
        ...

