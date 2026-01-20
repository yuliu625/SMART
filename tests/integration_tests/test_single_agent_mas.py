"""
测试single agent的情况。
"""

from __future__ import annotations
import pytest
import asyncio
from loguru import logger

from mas.mas_factory import MASFactory
from mas.utils.graph_visualizer import GraphVisualizer

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestSingleAgentMAS:
    @pytest.mark.parametrize(
        "adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path", [
        ('qwen2.5:1.5b', r'', 'qwen2.5:1.5b', r''),
    ])
    def test_single_agent_mas_structure(
        self,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ):
        mas = MASFactory.create_single_agent_mas_via_ollama(
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
        )
        mermaid_code = GraphVisualizer.get_mermaid_code(
            graph=mas,
        )
        logger.info(f"\nMermaid Code: \n{mermaid_code}")

