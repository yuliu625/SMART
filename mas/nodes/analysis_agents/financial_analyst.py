"""

"""

from mas.schemas import MASState
from .base_analyst import BaseAnalyst

from langchain_core.runnables import Runnable
from pydantic import BaseModel


class FinancialAnalyst(BaseAnalyst):
    """
    进行财务分析的analyst。
    """
    def __init__(
        self,
        llm_chain: Runnable,
        structured_output_format: type[BaseModel],
    ):
        super().__init__(
            llm_chain=llm_chain,
            structured_output_format=structured_output_format,
        )

    def run(self, state: MASState):
        state_to_be_updated = self.get_state_to_be_updated(
            this_agent_name='financial',
            analyst_chat_history=state.financial_analyst_chat_history,
            validator_chat_history=state.validator_chat_history,
            arbiter_context=state.arbiter_context,
            remaining_retrieve_rounds=state.remaining_retrieve_rounds,
        )
        return state_to_be_updated

