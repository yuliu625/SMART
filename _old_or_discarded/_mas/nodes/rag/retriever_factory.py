"""

"""

from mas.nodes.prompts.prompt_template_factories import RAGPromptTemplateFactory
from mas.nodes.models import LLMFactory
from .multi_query_retriever import MultiQueryRetriever
from .mas_multi_query_retrievers import (
    ControlMultiQueryRetriever,
    FinancialMultiQueryRetriever,
    StrategicMultiQueryRetriever,
)

# from langchain.retrievers.multi_query import MultiQueryRetriever

from langchain_core.vectorstores import VectorStore


class RagRetrieverFactory:
    def __init__(
        self,
        vector_store: VectorStore,
        pdf_name: str,
    ):
        self.prompt_template_factory = RAGPromptTemplateFactory()
        self.llm_factory = LLMFactory()

        self.retriever = self.get_retriever(
            vector_store=vector_store,
            pdf_name=pdf_name,
        )

    def get_retriever(
        self,
        vector_store: VectorStore,
        pdf_name: str,
    ):
        retriever = vector_store.as_retriever(
            search_type='mmr',
            search_kwargs={'k': 3, 'filter': {'pdf_name': pdf_name}},
        )
        return retriever

    def get_simple_retriever(
        self,
    ):
        retriever = self.retriever
        return retriever

    def get_multi_query_retriever(
        self,
    ):
        multi_query_retriever = MultiQueryRetriever(
            retriever=self.retriever,
        )
        return multi_query_retriever

    # def get_control_multi_query_retriever(self):
    #     control_multi_query_retriever = ControlMultiQueryRetriever(
    #         retriever=self.retriever,
    #     )
    #     return control_multi_query_retriever
    #
    # def get_financial_multi_query_retriever(self):
    #     financial_multi_query_retriever = FinancialMultiQueryRetriever(
    #         retriever=self.retriever,
    #     )
    #     return financial_multi_query_retriever
    #
    # def get_strategic_multi_query_retriever(self):
    #     strategic_multi_query_retriever = StrategicMultiQueryRetriever(
    #         retriever=self.retriever,
    #     )
    #     return strategic_multi_query_retriever

