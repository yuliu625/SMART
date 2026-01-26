"""
完全的MAS的测试。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.mas_factory import MASFactory
from mas.rag_factory import RAGFactory
from mas.utils.graph_visualizer import GraphVisualizer
from mas.schemas.final_mas_state import FinalMASState
from mas.io_methods import IOMethods

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_test_simple_rag():
    rag = RAGFactory.create_simple_rag_via_ollama(
        vector_store_persist_directory=r"D:\dataset\smart\tests\000004",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
    )
    return rag


def make_test_multi_query_rag():
    rag = RAGFactory.create_multi_query_rag_via_ollama_base_on_ollama_llm(
        vector_store_persist_directory=r"D:\dataset\smart\tests\000004",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
        llm_model_name='qwen2.5:1.5b',
        llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\rag\rewritter_system_prompt_template.j2",
    )
    return rag


class TestFinalMas:
    def test_final_mas_structure(
        self,
    ) -> None:
        ...

    @pytest.mark.asyncio
    async def test_final_mas_with_load_and_save(
        self,
    ) -> None:
        ...

