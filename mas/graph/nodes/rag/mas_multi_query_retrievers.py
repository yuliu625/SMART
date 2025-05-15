"""

"""

from ...states import MASState
from .multi_query_retriever import MultiQueryRetriever

from langchain_core.vectorstores import VectorStoreRetriever


class ControlMultiQueryRetriever(MultiQueryRetriever):
    def __init__(
        self,
        retriever: VectorStoreRetriever,
    ):
        super().__init__(retriever=retriever)

    def run(self, state: MASState):
        state_to_be_updated = self.get_state_to_be_updated(
            current_query=state.current_message,
            last_round_result_number=state.control_last_round_result_number,
            query_chat_history=state.control_query_chat_history,
            query_result_history=state.control_query_result_history,
        )
        return {
            'control_query_chat_history': state_to_be_updated['query_chat_history'],
            'control_query_result_history': state_to_be_updated['query_result_history'],
            'control_last_round_result_number': state_to_be_updated['last_round_result_number'],
            'control_current_query_results': state_to_be_updated['current_query_results'],
        }


class FinancialMultiQueryRetriever(MultiQueryRetriever):
    def __init__(
        self,
        retriever: VectorStoreRetriever,
    ):
        super().__init__(retriever=retriever)

    def run(self, state: MASState):
        state_to_be_updated = self.get_state_to_be_updated(
            current_query=state.current_message,
            last_round_result_number=state.financial_last_round_result_number,
            query_chat_history=state.financial_query_chat_history,
            query_result_history=state.financial_query_result_history,
        )
        return {
            'financial_query_chat_history': state_to_be_updated['query_chat_history'],
            'financial_query_result_history': state_to_be_updated['query_result_history'],
            'financial_last_round_result_number': state_to_be_updated['last_round_result_number'],
            'financial_current_query_results': state_to_be_updated['current_query_results'],
        }


class StrategicMultiQueryRetriever(MultiQueryRetriever):
    def __init__(
        self,
        retriever: VectorStoreRetriever,
    ):
        super().__init__(retriever=retriever)

    def run(self, state: MASState):
        state_to_be_updated = self.get_state_to_be_updated(
            current_query=state.current_message,
            last_round_result_number=state.strategic_last_round_result_number,
            query_chat_history=state.strategic_query_chat_history,
            query_result_history=state.strategic_query_result_history,
        )
        return {
            'strategic_query_chat_history': state_to_be_updated['query_chat_history'],
            'strategic_query_result_history': state_to_be_updated['query_result_history'],
            'strategic_last_round_result_number': state_to_be_updated['last_round_result_number'],
            'strategic_current_query_results': state_to_be_updated['current_query_results'],
        }

