"""

"""

from ...states import MASState

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
        documents = self.retriever.invoke(state.current_query)
        return {
            'current_query_results': documents,
        }

