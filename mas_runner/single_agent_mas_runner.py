"""
运行器的构建。
"""

from __future__ import annotations
from loguru import logger

from mas.mas_factory import MASFactory
from mas.io_methods import IOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SingleAgentMASRunner:
    @staticmethod
    async def run_via_vllm(
        # IO
        markdown_files_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        adjudicator_main_llm_base_url: str,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_base_url: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ) -> None:
        ...

    @staticmethod
    async def run_via_ollama(
        # IO
        markdown_files_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ) -> None:
        # build MAS
        mas = MASFactory.create_single_agent_mas_via_ollama(
            adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
            adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
            adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
            adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
        )

