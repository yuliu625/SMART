"""
构建vector store的方法。
"""

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore


class VectorStoreFactory:
    @staticmethod
    def create_vector_store(

    ) -> VectorStore:
        ...

