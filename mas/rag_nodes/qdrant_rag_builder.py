"""
基于 qdrant 的 RAG 构造器。

约定:
    - ChatOpenAI: llm 相关统一使用 openAI Client 。
    - retriever: 传入 retriever 实现 RAG 构造 。
    - bge-m3: 仅实现基于自定义的 qdrant embedding model 实现的 bge-m3 进行构造。
"""

from __future__ import annotations
from loguru import logger

# 当前包的具体化定义。
from mas.rag_nodes.qdrant_rag_nodes.simple_rag import SimpleRAG
from mas.rag_nodes.qdrant_rag_nodes.multi_query_rag import MultiQueryRAG
# RAG包的导入。
from rag.embedding.qdrant_embedding_models.bge_m3_embedding_model import BGEM3EmbeddingModel
from rag.storing.qdrant_client_builder import QdrantClientBuilder

from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage


class QdrantRAGBuilder:
    @staticmethod
    def build_simple_rag(
        # Client
        client_disk_path: str | Path,
        collection_name: str,
        # Qdrant Text Embedding Model
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
    ):
        # client
        client = QdrantClientBuilder.load_client_from_disk(
            path=client_disk_path,
            collection_name=collection_name,
        )
        # bge-m3
        embedding_model = BGEM3EmbeddingModel(
            model_name_or_path=embedding_model_name_or_path,
            batch_size=batch_size,
        )
        # RAG
        rag = SimpleRAG(
            client=client,
            qdrant_embedding_model=embedding_model,
            search_configs=search_configs,
        )
        return rag

    @staticmethod
    def build_multi_query_rag(
        # Client
        client_disk_path: str | Path,
        collection_name: str,
        # Qdrant Text Embedding Model
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
        structured_llm: BaseChatModel,
        structured_llm_system_message: SystemMessage,
    ):
        # client
        client = QdrantClientBuilder.load_client_from_disk(
            path=client_disk_path,
            collection_name=collection_name,
        )
        # bge-m3
        embedding_model = BGEM3EmbeddingModel(
            model_name_or_path=embedding_model_name_or_path,
            batch_size=batch_size,
        )
        # HACK: 在这里构建 structured 相关。
        # RAG
        rag = MultiQueryRAG(
            client=client,
            qdrant_embedding_model=embedding_model,
            search_configs=search_configs,
            structured_llm=structured_llm,
            structured_llm_system_message=structured_llm_system_message,
        )
        return rag

