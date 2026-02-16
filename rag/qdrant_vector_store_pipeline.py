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
# from rag.embedding.embedding_model_factory import EmbeddingModelFactory
# from rag.storing.chroma_vector_store_builder import ChromaVectorStoreBuilder

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class QdrantVectorStorePipeline:
    @staticmethod
    def make_vector_store_via_fastembed(
        # loading
        markdown_file_path: str | Path,
        # splitting
        headers_to_split_on: list[tuple[str, str]],
        # embedding
        # ollama_embedding_model_name: str,
        # ollama_embedding_model_context_length: int,
        # storing
        vector_store_path: str | Path,
    ):
        # loading
        document = TextLoadingMethods.load_text(
            text_path=markdown_file_path,
            # HARDCODED
            encoding='utf-8',
            is_autodetect_encoding=False,
        )
        # chunks
        documents = MarkdownSplittingMethods.split_markdown_by_header(
            document=document,
            headers_to_split_on=headers_to_split_on,
            # HARDCODED
            is_strip_headers=False,
        )
        raise NotImplementedError

