"""
构造 rag 的工厂。

预期:
    - 配合 cached_mas_factory 使用。

构造:
    - 对应 qdrant 的 embedding model ，目前仅使用实现的完整功能的 bge-m3 。
    - 使用 gateway 统一 LLM 层管理。
"""

from __future__ import annotations
from loguru import logger

# RAG
from mas.rag_nodes.qdrant_rag_builder import QdrantRAGBuilder
# 依赖MAS相关工具
from mas.models.local_llm_factory import LocalLLMFactory
from mas.prompts.prompt_template_loader import PromptTemplateLoader
# MAS需要的定义
from mas.schemas.structured_output_format import RewrittenQueries

from pathlib import Path

from typing import TYPE_CHECKING, cast
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage


class QdrantRAGFactory:
    @staticmethod
    def create_simple_rag(
        # Client
        client_disk_path: str | Path,
        collection_name: str,
        # Qdrant Text Embedding Model
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
    ):
        rag = QdrantRAGBuilder.build_simple_rag(
            client_disk_path=client_disk_path,
            collection_name=collection_name,
            embedding_model_name_or_path=embedding_model_name_or_path,
            batch_size=batch_size,
            search_configs=search_configs,
        )
        return rag

    @staticmethod
    def create_multi_query_rag(
        # Client
        client_disk_path: str | Path,
        collection_name: str,
        # Qdrant Text Embedding Model
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
        llm_base_url: str,
        rewriter_llm_model_name: str,
        rewriter_llm_system_message_template_path: str,
    ):
        llm = LocalLLMFactory.create_openai_llm(
            base_url=llm_base_url,
            model_name=rewriter_llm_model_name,
            # HARDCODED
            temperature=0.0,
            max_tokens=None,
            logprobs=None,
            use_responses_api=None,
            max_retries=None,
            model_configs=dict(),
        )
        rewriter_llm = llm.with_structured_output(
            schema=RewrittenQueries,
        ).with_retry(
            stop_after_attempt=3,
        )
        rewriter_llm_system_message = PromptTemplateLoader.load_system_message_prompt_template_from_j2(
            system_message_prompt_template_path=rewriter_llm_system_message_template_path,
        ).format()
        rag = QdrantRAGBuilder.build_multi_query_rag(
            client_disk_path=client_disk_path,
            collection_name=collection_name,
            embedding_model_name_or_path=embedding_model_name_or_path,
            batch_size=batch_size,
            search_configs=search_configs,
            structured_llm=rewriter_llm,
            structured_llm_system_message=rewriter_llm_system_message,
        )
        return rag

