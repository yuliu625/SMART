"""
完全的MAS的测试。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.mas_factory import MASFactory
from mas.chroma_rag_factory import ChromaRAGFactory
from mas.utils.graph_visualizer import GraphVisualizer
from mas.schemas.final_mas_state import FinalMASState
from mas.io_methods import IOMethods

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_test_simple_rag():
    rag = ChromaRAGFactory.create_simple_rag_via_ollama(
        vector_store_persist_directory=r"D:\dataset\smart\tests\000004",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
    )
    return rag


def make_test_multi_query_rag():
    rag = ChromaRAGFactory.create_multi_query_rag_via_ollama_base_on_ollama_llm(
        vector_store_persist_directory=r"D:\dataset\smart\tests\000004",
        embedding_model_model_name='nomic-embed-text',
        embedding_model_num_ctx=8192,
        search_configs={},
        llm_model_name='qwen2.5:1.5b',
        llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\rag\rewritter_system_prompt_template.j2",
    )
    return rag


class TestFinalMas:
    @pytest.mark.parametrize(
        "surveyor_main_llm_model_name, surveyor_main_llm_system_message_template_path, investigator_main_llm_model_name, investigator_main_llm_system_message_template_path,investigator_formatter_llm_model_name,investigator_formatter_llm_system_message_template_path,adjudicator_main_llm_model_name,adjudicator_main_llm_system_message_template_path,adjudicator_formatter_llm_model_name,adjudicator_formatter_llm_system_message_template_path,analyst_main_llm_model_name,analyst_main_llm_system_message_template_path,analyst_formatter_llm_model_name,analyst_formatter_llm_system_message_template_path,rag,", [
        ('qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_formatter_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2',
         make_test_simple_rag()),
    ])
    def test_final_mas_structure(
        self,
        # Surveyor
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Investigator
        investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        # Adjudicator
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG
        rag,
    ) -> None:
        mas = MASFactory.create_final_mas_via_ollama(
            surveyor_main_llm_model_name=surveyor_main_llm_model_name,
            surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
            investigator_main_llm_model_name=investigator_main_llm_model_name,
            investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
            investigator_formatter_llm_model_name=investigator_formatter_llm_model_name,
            investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
            analyst_main_llm_model_name=analyst_main_llm_model_name,
            analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
            analyst_formatter_llm_model_name=analyst_formatter_llm_model_name,
            analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
            rag=rag,
        )
        mermaid_code = GraphVisualizer.get_mermaid_code(
            graph=mas,
        )
        logger.info(f"\nDesign Pattern: MAS\nMermaid Code: \n{mermaid_code}")

    @pytest.mark.parametrize(
        "surveyor_main_llm_model_name, surveyor_main_llm_system_message_template_path, investigator_main_llm_model_name, investigator_main_llm_system_message_template_path, investigator_formatter_llm_model_name, investigator_formatter_llm_system_message_template_path, adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path, analyst_main_llm_model_name, analyst_main_llm_system_message_template_path,analyst_formatter_llm_model_name,analyst_formatter_llm_system_message_template_path, rag, markdown_file_path, result_path", [
        ('qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_formatter_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2',
        'qwen2.5:1.5b',
        r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2',
         make_test_simple_rag(),
         r"D:\dataset\smart\tests\docling_1\000004.md",
         r"D:\dataset\smart\tests\final_mas_000004.json",
         ),
    ])
    @pytest.mark.asyncio
    async def test_final_mas_with_load_and_save(
        self,
        # Surveyor
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Investigator
        investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        # Adjudicator
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG
        rag,
        markdown_file_path: str,
        result_path: str,
    ) -> None:
        mas = MASFactory.create_final_mas_via_ollama(
            surveyor_main_llm_model_name=surveyor_main_llm_model_name,
            surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
            investigator_main_llm_model_name=investigator_main_llm_model_name,
            investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
            investigator_formatter_llm_model_name=investigator_formatter_llm_model_name,
            investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
            analyst_main_llm_model_name=analyst_main_llm_model_name,
            analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
            analyst_formatter_llm_model_name=analyst_formatter_llm_model_name,
            analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
            rag=rag,
        )
        state = IOMethods.load_final_mas_state(
            markdown_file_path=markdown_file_path,
        )
        result = await mas.ainvoke(
            input=state,
            config=dict(recursion_limit=100),
        )
        logger.info(f"\nMAS Result: \n{result}")
        IOMethods.save_final_mas_state(state=result, result_path=result_path)

