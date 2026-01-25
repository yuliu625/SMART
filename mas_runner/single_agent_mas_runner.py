"""
single agent的自动运行。
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
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        markdown_files_dir = Path(markdown_files_dir)
        markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
        for markdown_file_path in markdown_file_path_list:
            result_file_path = result_dir / f"{markdown_file_path.stem}.json"
            if not result_file_path.exists():
                # build MAS
                mas = MASFactory.create_single_agent_via_vllm(
                    adjudicator_main_llm_base_url=adjudicator_main_llm_base_url,
                    adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
                    adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                    adjudicator_formatter_llm_base_url=adjudicator_formatter_llm_base_url,
                    adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
                    adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                )
                state = IOMethods.load_single_agent_mas_state(
                    markdown_file_path=markdown_file_path,
                )
                result = await mas.ainvoke(
                    input=state,
                )
                IOMethods.save_single_agent_mas_state(
                    state=result,
                    result_path=result_file_path,
                )
                logger.success(f"Saved {result_file_path}.")

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
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        markdown_files_dir = Path(markdown_files_dir)
        markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
        for markdown_file_path in markdown_file_path_list:
            result_file_path = result_dir / f"{markdown_file_path.stem}.json"
            if not result_file_path.exists():
                # build MAS
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
                IOMethods.save_single_agent_mas_state(
                    state=result,
                    result_path=result_file_path,
                )
                logger.success(f"Saved {result_file_path}.")

