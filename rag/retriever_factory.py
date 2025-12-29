"""
retriever的工厂。
"""

from __future__ import annotations

# from langchain.retrievers import Retriever

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore, VectorStoreRetriever


class RetrieverFactory:
    @staticmethod
    def create_retriever(
        vector_store: VectorStore,
    ) -> VectorStoreRetriever:
        retriever = vector_store.as_retriever(
            search_type='mmr',
            search_kwargs={'k': 3, 'filter': {}},
        )
        return retriever

