"""

"""

from _old_or_discarded._mas.schemas import MASState

from langchain_core.vectorstores import VectorStoreRetriever


class SimpleQueryEngine:
    """

    """
    def __init__(
        self,
        retriever: VectorStoreRetriever,
    ):
        self.retriever = retriever

    def run(self, state: MASState):
        documents = self.retriever.invoke(state.current_message)
        return {
            f'{state.current_agent_name}_query_results': documents,
        }

