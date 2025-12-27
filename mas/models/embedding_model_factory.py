"""
获取各种embedding-model的工厂。
"""

from __future__ import annotations

from langchain_core.embeddings import Embeddings

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class EmbeddingModelFactory:
    @staticmethod
    def create_embedding_model(

    ) -> Embeddings:
        ...

