"""
测试single agent的情况。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.mas_factory import MASFactory
from mas.utils.graph_visualizer import GraphVisualizer
from mas.schemas.single_agent_state import SingleAgentState
from mas.io_methods import IOMethods

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestSingleAgentMAS:
    @pytest.mark.parametrize(
        "adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path", [
        ('qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_formatter_llm_system_prompt_template.j2'),
    ])
    def test_single_agent_structure(
        self,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ):
        mas = MASFactory.create_single_agent_via_ollama(
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
        )
        mermaid_code = GraphVisualizer.get_mermaid_code(
            graph=mas,
        )
        logger.info(f"\nMermaid Code: \n{mermaid_code}")

    @pytest.mark.parametrize(
        "adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path", [
        ('qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_formatter_llm_system_prompt_template.j2'),
    ])
    @pytest.mark.asyncio
    async def test_single_agent(
        self,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ):
        mas = MASFactory.create_single_agent_via_ollama(
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
        )
        result = await mas.ainvoke(
            input=SingleAgentState(
                decision_shared_messages=[
                    HumanMessage(content="你觉得明天下雨的几率有多大？")
                ],
            )
        )
        logger.info(f"\nMAS Result: \n{result}")

    @pytest.mark.parametrize(
        "adjudicator_main_llm_model_name, adjudicator_main_llm_system_message_template_path, adjudicator_formatter_llm_model_name, adjudicator_formatter_llm_system_message_template_path, markdown_file_path, result_path", [
        ('qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_main_llm_system_prompt_template.j2',
         'qwen2.5:1.5b',
         r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_formatter_llm_system_prompt_template.j2',
         r"D:\dataset\smart\tests\docling_1\000004.md",
         r"D:\dataset\smart\tests\single_agent_000004.json",),
    ])
    @pytest.mark.asyncio
    async def test_single_agent_with_load_and_save(
        self,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        markdown_file_path: str,
        result_path: str,
    ):
        mas = MASFactory.create_single_agent_via_ollama(
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
        )
        state = IOMethods.load_single_agent_mas_state(
            markdown_file_path=markdown_file_path,
        )
        result = await mas.ainvoke(
            input=state,
        )
        logger.info(f"\nMAS Result: \n{result}")
        IOMethods.save_single_agent_mas_state(state=result, result_path=result_path)

