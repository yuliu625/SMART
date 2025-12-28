"""
retriever的工厂。
"""

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore, VectorStoreRetriever


class RetrieverFactory:
    @staticmethod
    def create_retriever(
        vector_store: VectorStore,
    ) -> VectorStoreRetriever:
        ...

