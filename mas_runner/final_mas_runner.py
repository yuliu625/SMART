"""
实际构建MAS的自动运行。

实验运行的时，约定embedding-model使用huggingface运行。

特殊情况:
    - 该runner硬编码graph超级步最大限制为100次。
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
    async def run_via_vllm_with_huggingface_simple_rag(
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
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        # Retriever
        search_configs: dict,
    ) -> None:
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        markdown_files_dir = Path(markdown_files_dir)
        markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
        vector_store_dir = Path(vector_store_dir)
        for markdown_file_path in markdown_file_path_list:
            result_file_path = result_dir / f"{markdown_file_path.stem}.json"
            vector_store_path = vector_store_dir / f"{markdown_file_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                # build rag
                rag = RAGFactory.create_simple_rag_via_huggingface(
                    vector_store_persist_directory=vector_store_dir,
                    embedding_model_model_name_or_path=embedding_model_model_name_or_path,
                    embedding_model_model_kwargs=embedding_model_model_kwargs,
                    embedding_model_encode_kwargs=embedding_model_encode_kwargs,
                    embedding_model_query_encode_kwargs=embedding_model_query_encode_kwargs,
                    search_configs=search_configs,
                    # HARDCODED
                    embedding_model_is_multi_process=False,
                    embedding_model_cache_folder=None,
                    embedding_model_is_show_progress=True,
                )
                # build mas
                mas = MASFactory.create_final_mas_via_vllm(
                    surveyor_main_llm_base_url=surveyor_main_llm_base_url,
                    surveyor_main_llm_model_name=surveyor_main_llm_model_name,
                    surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                    investigator_main_llm_base_url=investigator_main_llm_base_url,
                    investigator_main_llm_model_name=investigator_main_llm_model_name,
                    investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                    investigator_formatter_llm_base_url=investigator_formatter_llm_base_url,
                    investigator_formatter_llm_model_name=investigator_formatter_llm_model_name,
                    investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                    adjudicator_main_llm_base_url=adjudicator_main_llm_base_url,
                    adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
                    adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                    adjudicator_formatter_llm_base_url=adjudicator_formatter_llm_base_url,
                    adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
                    adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                    analyst_main_llm_base_url=analyst_main_llm_base_url,
                    analyst_main_llm_model_name=analyst_main_llm_model_name,
                    analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                    analyst_formatter_llm_base_url=analyst_formatter_llm_base_url,
                    analyst_formatter_llm_model_name=analyst_formatter_llm_model_name,
                    analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                    rag=rag,
                )
                state = IOMethods.load_final_mas_state(
                    markdown_file_path=markdown_file_path,
                )
                result = await mas.ainvoke(
                    input=state,
                    # HARDCODED
                    config=dict(recursion_limit=100),
                )
                IOMethods.save_final_mas_state(
                    state=result,
                    result_path=result_file_path,
                )
                logger.success(f"Saved {result_file_path}.")

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
        raise NotImplementedError

    @staticmethod
    async def run_via_vllm_with_huggingface_multi_query_rag(
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
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        rag_llm_base_url: str,
        rag_llm_model_name: str,
        rag_llm_system_message_template_path: str,
        # Retriever
        search_configs: dict,
    ) -> None:
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        markdown_files_dir = Path(markdown_files_dir)
        markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
        vector_store_dir = Path(vector_store_dir)
        for markdown_file_path in markdown_file_path_list:
            result_file_path = result_dir / f"{markdown_file_path.stem}.json"
            vector_store_path = vector_store_dir / f"{markdown_file_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                # build rag
                rag = RAGFactory.create_multi_query_rag_via_huggingface_base_on_vllm_llm(
                    vector_store_persist_directory=vector_store_dir,
                    embedding_model_model_name_or_path=embedding_model_model_name_or_path,
                    embedding_model_model_kwargs=embedding_model_model_kwargs,
                    embedding_model_encode_kwargs=embedding_model_encode_kwargs,
                    embedding_model_query_encode_kwargs=embedding_model_query_encode_kwargs,
                    search_configs=search_configs,
                    llm_base_url=rag_llm_base_url,
                    llm_model_name=rag_llm_model_name,
                    llm_system_message_template_path=rag_llm_system_message_template_path,
                    # HARDCODED
                    embedding_model_is_multi_process=False,
                    embedding_model_cache_folder=None,
                    embedding_model_is_show_progress=True,
                )
                # build mas
                mas = MASFactory.create_final_mas_via_vllm(
                    surveyor_main_llm_base_url=surveyor_main_llm_base_url,
                    surveyor_main_llm_model_name=surveyor_main_llm_model_name,
                    surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                    investigator_main_llm_base_url=investigator_main_llm_base_url,
                    investigator_main_llm_model_name=investigator_main_llm_model_name,
                    investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                    investigator_formatter_llm_base_url=investigator_formatter_llm_base_url,
                    investigator_formatter_llm_model_name=investigator_formatter_llm_model_name,
                    investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                    adjudicator_main_llm_base_url=adjudicator_main_llm_base_url,
                    adjudicator_main_llm_model_name=adjudicator_main_llm_model_name,
                    adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                    adjudicator_formatter_llm_base_url=adjudicator_formatter_llm_base_url,
                    adjudicator_formatter_llm_model_name=adjudicator_formatter_llm_model_name,
                    adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                    analyst_main_llm_base_url=analyst_main_llm_base_url,
                    analyst_main_llm_model_name=analyst_main_llm_model_name,
                    analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                    analyst_formatter_llm_base_url=analyst_formatter_llm_base_url,
                    analyst_formatter_llm_model_name=analyst_formatter_llm_model_name,
                    analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                    rag=rag,
                )
                state = IOMethods.load_final_mas_state(
                    markdown_file_path=markdown_file_path,
                )
                result = await mas.ainvoke(
                    input=state,
                    # HARDCODED
                    config=dict(recursion_limit=100),
                )
                IOMethods.save_final_mas_state(
                    state=result,
                    result_path=result_file_path,
                )
                logger.success(f"Saved {result_file_path}.")

