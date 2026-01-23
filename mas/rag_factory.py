"""
构造rag的工厂。

配合mas_factory使用。
"""

from __future__ import annotations
from loguru import logger

# RAG
from rag_nodes.chroma_rag_builder import ChromaRAGBuilder
# 依赖MAS相关工具
from mas.models.local_llm_factory import LocalLLMFactory

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class RagFactory:
    @staticmethod
    def create_simple_rag_via_ollama(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        # Retriever
        search_configs: dict,
    ):
        rag = ChromaRAGBuilder.build_simple_rag_via_ollama(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name=embedding_model_model_name,
            embedding_model_num_ctx=embedding_model_num_ctx,
            # HARDCODED
            embedding_model_repeat_penalty=None,
            embedding_model_temperature=None,
            embedding_model_stop_tokens=None,
            embedding_model_top_k=None,
            embedding_model_top_p=None,

            search_configs=search_configs,
        )
        return rag

    @staticmethod
    def create_simple_rag_via_huggingface(
        vector_store_persist_directory: str | Path,
    ):
        raise NotImplementedError

    @staticmethod
    def create_multi_query_rag_via_ollama(
        vector_store_persist_directory: str,
    ):
        raise NotImplementedError

    @staticmethod
    def create_multi_query_rag_via_huggingface(
        vector_store_persist_directory: str,
    ):
        raise NotImplementedError

