"""
Design Pattern: sequential workflow.
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


def get_common_sequential_workflow_configs() -> dict:
    sequential_workflow_config = dict(
        llm_base_url='http://127.0.0.1:4000',
        surveyor_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\sequential_workflow\surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\sequential_workflow\adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\sequential_workflow\adjudicator_formatter_llm_system_prompt_template.j2",
    )
    return sequential_workflow_config


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
        batch_size=1,
        llm_base_url='http://127.0.0.1:4000',
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


async def run_dense_search_experiments():
    ...


async def run_sparse_search_experiments():
    ...


async def run_multi_vector_search_experiments():
    ...


async def run_hybrid_search_experiments():
    ...


async def run_all_search_experiments():
    ...


async def main():
    ...


if __name__ == '__main__':
    asyncio.run(main())

