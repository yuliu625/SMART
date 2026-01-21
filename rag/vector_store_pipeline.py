"""
Sources:

References:

Synopsis:

Notes:

"""

from __future__ import annotations
from loguru import logger

from rag.loading.load_text import TextLoadingMethods
from rag.splitting.split_markdown import MarkdownSplittingMethods
from rag.embedding.embedding_model_factory import EmbeddingModelFactory
from rag.storing.chroma_vector_store_builder import ChromaVectorStoreBuilder

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ChromaVectorStorePipeline:
    @staticmethod
    def make_vector_store(

    ):
        ...

