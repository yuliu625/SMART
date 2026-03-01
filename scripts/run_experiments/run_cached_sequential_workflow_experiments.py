"""
Design Pattern: sequential workflow.

对于 sequential workflow ，默认只进行 simple RAG 下各种 retrieval methods 的对比。
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas_runner.cached_sequential_workflow_runner import (
    CachedSequentialWorkflowRunner,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def get_common_io_configs() -> dict:
    io_configs = dict(
        surveyor_cache_dir=r"/home/liuyu/liuyu_nfs_data/smart_cache/surveyor_cache",
        general_query_path=r"/home/liuyu/workspace/code/smart_/mas/prompts/rag/general_query_human_prompt_template.j2",
        vector_store_dir=r"/home/liuyu/liuyu_nfs_data/smart_bge_m3_vector_store",
    )
    return io_configs


def get_common_sequential_workflow_configs() -> dict:
    sequential_workflow_config = dict(
        llm_base_url='http://127.0.0.1:4000',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart_/mas/prompts/sequential_workflow/surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart_/mas/prompts/sequential_workflow/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart_/mas/prompts/sequential_workflow/adjudicator_formatter_llm_system_prompt_template.j2",
    )
    return sequential_workflow_config


def get_common_simple_rag_configs() -> dict:
    simple_rag_configs = dict(
        collection_name='default',
        embedding_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        batch_size=1,
    )
    return simple_rag_configs


def get_common_multi_query_rag_configs() -> dict:
    multi_query_rag_configs = dict(
        collection_name='default',
        embedding_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        batch_size=8,
        # llm_base_url='http://127.0.0.1:4000',
        rewriter_llm_model_name='formatter-llm',
        rewriter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart_/mas/prompts/rag/rewriter_system_prompt_template.j2",
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
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'dense'
    # batch run
    ## simple rag
    await CachedSequentialWorkflowRunner.batch_run_cached_sequential_workflow_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_sequential_workflow_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Dense Search Simple RAG Complete")


async def run_sparse_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'sparse'
    # batch run
    ## simple rag
    await CachedSequentialWorkflowRunner.batch_run_cached_sequential_workflow_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_sequential_workflow_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Sparse Search Simple RAG Complete")


async def run_multi_vector_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'multi_vector'
    # batch run
    ## simple rag
    await CachedSequentialWorkflowRunner.batch_run_cached_sequential_workflow_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_sequential_workflow_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Multi-Vector Search Simple RAG Complete")


async def run_hybrid_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'hybrid'
    # batch run
    ## simple rag
    await CachedSequentialWorkflowRunner.batch_run_cached_sequential_workflow_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_sequential_workflow_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"Hybrid Search Simple RAG Complete")


async def run_all_search_experiments(
    max_concurrent: int,
    result_dir: str,
):
    search_configs = get_common_search_configs()
    search_configs['search_method'] = 'all'
    # batch run
    ## simple rag
    await CachedSequentialWorkflowRunner.batch_run_cached_sequential_workflow_with_simple_rag(
        max_concurrent=max_concurrent,
        result_dir=result_dir,
        **get_common_io_configs(),
        **get_common_sequential_workflow_configs(),
        **get_common_simple_rag_configs(),
        search_configs=search_configs,
    )
    logger.success(f"All Search Simple RAG Complete")


async def main():
    # dense
    await run_dense_search_experiments(
        max_concurrent=10,
        result_dir=r"/home/liuyu/liuyu_nfs_data/new_smart_sequential_workflow_simple_rag/dense",
    )
    # sparse
    await run_sparse_search_experiments(
        max_concurrent=10,
        result_dir=r"/home/liuyu/liuyu_nfs_data/new_smart_sequential_workflow_simple_rag/sparse",
    )
    # multi-vector
    await run_multi_vector_search_experiments(
        max_concurrent=10,
        result_dir=r"/home/liuyu/liuyu_nfs_data/new_smart_sequential_workflow_simple_rag/multi_vector",
    )
    # hybrid
    await run_hybrid_search_experiments(
        max_concurrent=10,
        result_dir=r"/home/liuyu/liuyu_nfs_data/new_smart_sequential_workflow_simple_rag/hybrid",
    )
    # all
    await run_all_search_experiments(
        max_concurrent=10,
        result_dir=r"/home/liuyu/liuyu_nfs_data/new_smart_sequential_workflow_simple_rag/all",
    )


if __name__ == '__main__':
    asyncio.run(main())

