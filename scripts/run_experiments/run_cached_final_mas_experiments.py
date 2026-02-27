"""
Design Pattern: MAS.
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas_runner.cached_final_mas_runner import (
    CachedFinalMASRunner,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def get_common_io_configs() -> dict:
    io_configs = dict(
        surveyor_cache_dir=r"",
        vector_store_dir=r"",
    )
    return io_configs


def get_common_final_mas_configs() -> dict:
    mas_configs = dict(
        llm_base_url='http://127.0.0.1:4000',
        surveyor_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2",
    )
    return mas_configs


def get_common_simple_rag_configs() -> dict:
    simple_rag_configs = dict(
        collection_name='default',
        embedding_model_name_or_path=r"D:\model\BAAI\bge-m3",
        batch_size=1,
    )
    return simple_rag_configs


def get_common_multi_query_rag_configs() -> dict:
    multi_query_rag_configs = dict(
        collection_name='default',
        embedding_model_name_or_path=r"D:\model\BAAI\bge-m3",
        batch_size=8,
        # llm_base_url='http://127.0.0.1:4000',
        rewriter_llm_model_name='formatter-llm',
        rewriter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\rag\rewriter_system_prompt_template.j2",
    )
    return multi_query_rag_configs


def get_common_search_configs() -> dict:
    search_configs = dict(
        collection_name='default',
        limit=3,
        dense_limit=5,
        sparse_limit=5,
        multi_vector_limit=5,
        # search_method='hybrid',
    )
    return search_configs


async def run_dense_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    raise NotImplementedError("没有必要进行的实验。")


async def run_sparse_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    raise NotImplementedError("没有必要进行的实验。")


async def run_multi_vector_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    raise NotImplementedError("没有必要进行的实验。")


async def run_hybrid_search_and_simple_rag_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'hybrid'
    # batch run
    ## simple rag
    await CachedFinalMASRunner.batch_run_final_mas_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_final_mas_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Hybrid Search Simple RAG Complete")


async def run_all_search_and_simple_rag_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'all'
    # batch run
    ## simple rag
    await CachedFinalMASRunner.batch_run_final_mas_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_final_mas_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"ALL Search Simple RAG Complete")


async def run_hybrid_search_and_multi_query_rag_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'hybrid'
    # batch run
    ## multi-query rag
    await CachedFinalMASRunner.batch_run_final_mas_with_multi_query_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_final_mas_configs(),
        **get_common_multi_query_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Hybrid Search Multi-Query RAG Complete")


async def run_all_search_and_multi_query_rag_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'all'
    # batch run
    ## multi-query rag
    await CachedFinalMASRunner.batch_run_final_mas_with_multi_query_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_final_mas_configs(),
        **get_common_multi_query_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"ALL Search Multi-Query RAG Complete")


async def main() -> None:
    # hybrid
    ## simple rag
    await run_hybrid_search_and_simple_rag_experiments(
        max_concurrent=2,
        result_dir=r"",
    )
    ## multi-query rag
    await run_hybrid_search_and_multi_query_rag_experiments(
        max_concurrent=2,
        result_dir=r"",
    )
    # all
    ## simple rag
    await run_all_search_and_simple_rag_experiments(
        max_concurrent=2,
        result_dir=r"",
    )
    ## multi-query rag
    await run_all_search_and_multi_query_rag_experiments(
        max_concurrent=2,
        result_dir=r"",
    )


if __name__ == '__main__':
    asyncio.run(main())

