"""
构造RAG的工厂。
"""

from __future__ import annotations
from loguru import logger

from mas.rag_nodes.simple_rag import SimpleRAG
from mas.rag_nodes.multi_query_rag import MultiQueryRAG

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage


class RAGFactory:
    @staticmethod
    def create_simple_rag(
        vector_store: VectorStore,
        search_configs: dict,
    ):
        simple_rag = SimpleRAG(
            vector_store=vector_store,
            search_configs=search_configs,
        )
        return simple_rag

    @staticmethod
    def create_multi_query_rag(
        vector_store: VectorStore,
        search_configs: dict,
        structured_llm: BaseChatModel,
        structured_llm_system_message: SystemMessage,
    ):
        multi_query_rag = MultiQueryRAG(
            vector_store=vector_store,
            search_configs=search_configs,
            structured_llm=structured_llm,
            structured_llm_system_message=structured_llm_system_message,
        )
        return multi_query_rag

