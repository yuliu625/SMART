"""
RAG构造器。

rag包中的外部导入全部在该层进行封装，不扩散到mas包中。

约定:
    - 基于chroma进行构建。
    - 只运行导入，不运行以构造的形式加载。

Notes:
    - 特殊情况: 因为:
            - 想要将rag的导入封装在rag_nodes中;
            - multi-query rag需要llm。
        因此:
            - rag包中的参数完全反序列化，mas相关未处理。
"""

from __future__ import annotations
from loguru import logger

# 当前包的具体化定义。
from mas.rag_nodes.chroma_rag_nodes.simple_rag import SimpleRAG
from mas.rag_nodes.chroma_rag_nodes.multi_query_rag import MultiQueryRAG
# RAG包的导入。
from rag.embedding.embedding_model_factory import EmbeddingModelFactory
from rag.storing.chroma_vector_store_builder import ChromaVectorStoreBuilder

from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage


class ChromaRAGBuilder:
    @staticmethod
    def build_simple_rag_via_ollama(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        embedding_model_repeat_penalty: float | None,
        embedding_model_temperature: float | None,
        embedding_model_stop_tokens: list[str] | None,
        embedding_model_top_k: int | None,
        embedding_model_top_p: float | None,
        # Retriever
        search_configs: dict,
    ):
        vector_store = ChromaVectorStoreBuilder.load_vector_store(
            persist_directory=vector_store_persist_directory,
            embedding_function=EmbeddingModelFactory.create_ollama_embedding_model(
                model_name=embedding_model_model_name,
                num_ctx=embedding_model_num_ctx,
                repeat_penalty=embedding_model_repeat_penalty,
                temperature=embedding_model_temperature,
                stop_tokens=embedding_model_stop_tokens,
                top_k=embedding_model_top_k,
                top_p=embedding_model_top_p,
            ),
        )
        simple_rag = SimpleRAG(
            vector_store=vector_store,
            search_configs=search_configs,
        )
        return simple_rag

    @staticmethod
    def build_simple_rag_via_huggingface(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        embedding_model_is_multi_process: bool,
        embedding_model_cache_folder: str | None,
        embedding_model_is_show_progress: bool,
        # Retriever
        search_configs: dict,
    ):
        vector_store = ChromaVectorStoreBuilder.load_vector_store(
            persist_directory=vector_store_persist_directory,
            embedding_function=EmbeddingModelFactory.create_huggingface_embedding_model(
                model_name_or_path=embedding_model_model_name_or_path,
                model_kwargs=embedding_model_model_kwargs,
                encode_kwargs=embedding_model_encode_kwargs,
                query_encode_kwargs=embedding_model_query_encode_kwargs,
                is_multi_process=embedding_model_is_multi_process,
                cache_folder=embedding_model_cache_folder,
                is_show_progress=embedding_model_is_show_progress,
            ),
        )
        simple_rag = SimpleRAG(
            vector_store=vector_store,
            search_configs=search_configs,
        )
        return simple_rag

    @staticmethod
    def build_multi_query_rag_via_ollama(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        embedding_model_repeat_penalty: float | None,
        embedding_model_temperature: float | None,
        embedding_model_stop_tokens: list[str] | None,
        embedding_model_top_k: int | None,
        embedding_model_top_p: float | None,
        # Retriever
        search_configs: dict,
        structured_llm: BaseChatModel,
        structured_llm_system_message: SystemMessage,
    ):
        vector_store = ChromaVectorStoreBuilder.load_vector_store(
            persist_directory=vector_store_persist_directory,
            embedding_function=EmbeddingModelFactory.create_ollama_embedding_model(
                model_name=embedding_model_model_name,
                num_ctx=embedding_model_num_ctx,
                repeat_penalty=embedding_model_repeat_penalty,
                temperature=embedding_model_temperature,
                stop_tokens=embedding_model_stop_tokens,
                top_k=embedding_model_top_k,
                top_p=embedding_model_top_p,
            ),
        )
        multi_query_rag = MultiQueryRAG(
            vector_store=vector_store,
            search_configs=search_configs,
            structured_llm=structured_llm,
            structured_llm_system_message=structured_llm_system_message,
        )
        return multi_query_rag

    @staticmethod
    def build_multi_query_rag_via_huggingface(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        embedding_model_is_multi_process: bool,
        embedding_model_cache_folder: str | None,
        embedding_model_is_show_progress: bool,
        # Retriever
        search_configs: dict,
        structured_llm: BaseChatModel,
        structured_llm_system_message: SystemMessage,
    ):
        vector_store = ChromaVectorStoreBuilder.load_vector_store(
            persist_directory=vector_store_persist_directory,
            embedding_function=EmbeddingModelFactory.create_huggingface_embedding_model(
                model_name_or_path=embedding_model_model_name_or_path,
                model_kwargs=embedding_model_model_kwargs,
                encode_kwargs=embedding_model_encode_kwargs,
                query_encode_kwargs=embedding_model_query_encode_kwargs,
                is_multi_process=embedding_model_is_multi_process,
                cache_folder=embedding_model_cache_folder,
                is_show_progress=embedding_model_is_show_progress,
            ),
        )
        multi_query_rag = MultiQueryRAG(
            vector_store=vector_store,
            search_configs=search_configs,
            structured_llm=structured_llm,
            structured_llm_system_message=structured_llm_system_message,
        )
        return multi_query_rag

