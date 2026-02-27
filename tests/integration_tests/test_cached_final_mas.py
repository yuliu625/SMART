"""
Tests for final mas.
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.cached_mas_factory import CachedMASFactory
from mas.qdrant_rag_factory import QdrantRAGFactory
from mas.cached_io_methods import CachedIOMethods

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


@pytest.fixture(name='llm_base_url')
def make_llm_base_url():
    return r"http://127.0.0.1:4000"


@pytest.fixture(name='search_configs')
def make_search_configs():
    search_configs = dict(
        collection_name='default',
        limit=3,
        dense_limit=3,
        sparse_limit=3,
        multi_vector_limit=3,
        search_method='hybrid',
    )
    return search_configs


@pytest.fixture(name='simple_rag')
def make_simple_rag(
    search_configs: dict,
):
    rag = QdrantRAGFactory.create_simple_rag(
        client_disk_path=r"D:\dataset\smart\data_pipeline_cache\vector_store\000004",
        collection_name='default',
        embedding_model_name_or_path=r"D:\model\BAAI\bge-m3",
        batch_size=1,
        search_configs=search_configs,
    )
    return rag


@pytest.fixture(name='multi_query_rag')
def make_multi_query_rag(
    search_configs: dict,
):
    rag = QdrantRAGFactory.create_multi_query_rag(
        client_disk_path=r"D:\dataset\smart\data_pipeline_cache\vector_store\000004",
        collection_name='default',
        embedding_model_name_or_path=r"D:\model\BAAI\bge-m3",
        batch_size=1,
        search_configs=search_configs,
        llm_base_url='http://127.0.0.1:4000',
        rewriter_llm_model_name='formatter-llm',
        rewriter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\rag\rewriter_system_prompt_template.j2",
    )
    return rag


@pytest.mark.asyncio
async def test_cached_final_mas_with_simple_rag(
    llm_base_url,
    simple_rag,
):
    # build mas
    mas = CachedMASFactory.create_cached_final_mas(
        llm_base_url=llm_base_url,
        surveyor_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_system_message_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2",
        rag=simple_rag,
    )
    state = CachedIOMethods.load_cached_final_mas_state(
        surveyor_cache_path=r"D:\dataset\smart\data_pipeline_cache\surveyor_cache\000004.txt",
    )
    # for quick test
    state.remaining_validation_rounds = 2
    state.remaining_retrieve_rounds = 2
    result = await mas.ainvoke(
        input=state,
        # HARDCODED
        config=dict(recursion_limit=100),
    )
    CachedIOMethods.save_cached_final_mas_state(
        state=result,
        result_path=r"D:\dataset\smart\tests\qdrant_final_mas\simple_rag_hybrid.json",
    )

