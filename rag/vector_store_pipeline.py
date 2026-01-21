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

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ChromaVectorStorePipeline:
    @staticmethod
    def make_vector_store_via_ollama(
        # loading
        markdown_file_path: str | Path,
        # splitting
        headers_to_split_on: list[tuple[str, str]],
        # embedding
        ollama_embedding_model_name: str,
        ollama_embedding_model_context_length: int,
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
        # embedding model
        embedding_model = EmbeddingModelFactory.create_ollama_embedding_model(
            model_name=ollama_embedding_model_name,
            num_ctx=ollama_embedding_model_context_length,
            # HARDCODED
            repeat_penalty=None,
            temperature=None,
            stop_tokens=None,
            top_k=None,
            top_p=None,
        )
        # storing
        ChromaVectorStoreBuilder.build_new_vector_store_via_default_method(
            persist_directory=vector_store_path,
            embedding_function=embedding_model,
            documents=documents,
        )
        logger.success(f"Vector store built in {vector_store_path}")

    @staticmethod
    def make_vector_store_via_huggingface(
        markdown_file_path: str | Path,
    ):
        ...

