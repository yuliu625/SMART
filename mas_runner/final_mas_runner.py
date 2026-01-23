"""
实际构建MAS的自动运行。
"""

from __future__ import annotations
from loguru import logger

from mas.mas_factory import MASFactory
from mas.rag_factory import RAGFactory
from mas.io_methods import IOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class FinalMASRunner:
    @staticmethod
    async def run_via_vllm(
        # IO
        markdown_files_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        surveyor_main_llm_base_url: str,
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_base_url: str,
        investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_base_url: str,
        investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_base_url: str,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_base_url: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_base_url: str,
        analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_base_url: str,
        analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
    ) -> None:
        ...

    @staticmethod
    async def run_via_ollama(
        # IO
        markdown_files_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
    ) -> None:
        ...

