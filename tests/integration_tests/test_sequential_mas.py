"""
Tests for sequential workflow.
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.mas_factory import MASFactory
from mas.rag_factory import RAGFactory
from mas.utils.graph_visualizer import GraphVisualizer
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.io_methods import IOMethods

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_test_simple_rag():
    rag = RAGFactory.create_simple_rag_via_ollama(
        vector_store_persist_directory=r"D:\dataset\smart\tests\t_vector_store",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
    )
    return rag


def make_test_multi_query_rag():
    rag = RAGFactory.create_multi_query_rag_via_ollama_base_on_ollama_llm(
        vector_store_persist_directory=r"D:\dataset\smart\tests\t_vector_store",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
        llm_model_name='qwen2.5:1.5b',
        llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\rag\rewritter_system_prompt_template.j2",
    )
    return rag


class TestSequentialMASState:
    @pytest.mark.parametrize(
        "surveyor_main_llm_model_name, surveyor_main_llm_system_message_template_path, adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path, rag,", [
        ('qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2',
         make_test_simple_rag(),
         ),
        ('qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2',
         make_test_multi_query_rag(),
         ),
    ])
    def test_sequential_mas_structure(
        self,
        # Surveyor
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Adjudicator
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        # RAG
        rag,
    ):
        mas = MASFactory.create_sequential_mas_via_ollama(
            surveyor_main_llm_model_name=surveyor_main_llm_model_name,
            surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
            rag=rag,
        )
        mermaid_code = GraphVisualizer.get_mermaid_code(
            graph=mas,
        )
        logger.info(f"\nDesign Pattern: Sequential Workflow\nMermaid Code: \n{mermaid_code}")


