"""

"""

from ...prompts import PromptTemplateFactory
from ....models import LLMFactory
from .multi_query_retriever import MultiQueryRetriever
from mas.utils import VectorStoreLoader

# from langchain.retrievers.multi_query import MultiQueryRetriever

from langchain_core.vectorstores import VectorStore
from langchain_openai import ChatOpenAI


class RagRetrieverFactory:
    def __init__(
        self,
        vector_store: VectorStore,
        pdf_name: str,
    ):
        self.prompt_template_factory = PromptTemplateFactory()
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


