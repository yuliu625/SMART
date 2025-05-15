"""
识别者。
"""

from ...states import MASState
from ..base_agent import BaseAgent

from langchain_core.runnables import Runnable
from pydantic import BaseModel


class Validator(BaseAgent):
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


