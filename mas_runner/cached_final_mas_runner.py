"""
使用 cache 加速 MAS 的自动运行。

实验运行的时，约定 embedding-model 使用 qdrant 集成的 fastembed 运行。

特殊情况:
    - 该 runner 硬编码 graph 超级步最大限制为 100 次。
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas.cached_mas_factory import CachedMASFactory
from mas.qdrant_rag_factory import QdrantRAGFactory
from mas.cached_io_methods import CachedIOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


async def semaphore_wrapper(
    semaphore: asyncio.Semaphore,
    func,
    *args,
    **kwargs,
):
    async with semaphore:
        return await func(*args, **kwargs)


class CachedFinalMASRunner:
    @staticmethod
    async def run_final_mas_with_simple_rag(
        # IO
        surveyor_cache_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
    ):
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        surveyor_cache_dir = Path(surveyor_cache_dir)
        surveyor_cache_path_list = list(surveyor_cache_dir.glob('*.txt'))
        vector_store_dir = Path(vector_store_dir)
        for surveyor_cache_path in surveyor_cache_path_list:
            result_file_path = result_dir / f"{surveyor_cache_path.stem}.json"
            vector_store_path = vector_store_dir / f"{surveyor_cache_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                await CachedFinalMASRunner.single_run_final_mas_with_simple_rag(
                    # IO
                    surveyor_cache_path=surveyor_cache_path,
                    vector_store_path=vector_store_path,
                    result_file_path=result_file_path,
                    # MAS configurations
                    llm_base_url=llm_base_url,
                    surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                    investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                    investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                    adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                    adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                    analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                    analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                    # RAG configurations
                    collection_name=collection_name,
                    embedding_model_name_or_path=embedding_model_name_or_path,
                    batch_size=batch_size,
                    # Retriever
                    search_configs=search_configs,
                )

    @staticmethod
    async def run_final_mas_with_multi_query_rag(
        # IO
        surveyor_cache_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
        rewriter_llm_model_name: str,
        rewriter_llm_system_message_template_path: str,
    ):
        # 路径处理。
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        surveyor_cache_dir = Path(surveyor_cache_dir)
        surveyor_cache_path_list = list(surveyor_cache_dir.glob('*.txt'))
        vector_store_dir = Path(vector_store_dir)
        for surveyor_cache_path in surveyor_cache_path_list:
            result_file_path = result_dir / f"{surveyor_cache_path.stem}.json"
            vector_store_path = vector_store_dir / f"{surveyor_cache_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                await CachedFinalMASRunner.single_run_final_mas_with_multi_query_rag(
                    # IO
                    surveyor_cache_path=surveyor_cache_path,
                    vector_store_path=vector_store_path,
                    result_file_path=result_file_path,
                    # MAS configurations
                    llm_base_url=llm_base_url,
                    surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                    investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                    investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                    adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                    adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                    analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                    analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                    # RAG configurations
                    collection_name=collection_name,
                    embedding_model_name_or_path=embedding_model_name_or_path,
                    batch_size=batch_size,
                    # Retriever
                    search_configs=search_configs,
                    rewriter_llm_model_name=rewriter_llm_model_name,
                    rewriter_llm_system_message_template_path=rewriter_llm_system_message_template_path,
                )

    @staticmethod
    async def single_run_final_mas_with_simple_rag(
        # IO
        surveyor_cache_path: str | Path,
        vector_store_path: str | Path,
        result_file_path: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
    ):
        try:
            # build rag
            rag = QdrantRAGFactory.create_simple_rag(
                client_disk_path=vector_store_path,
                collection_name=collection_name,
                embedding_model_name_or_path=embedding_model_name_or_path,
                batch_size=batch_size,
                search_configs=search_configs,
            )
            # build mas
            mas = CachedMASFactory.create_cached_final_mas(
                llm_base_url=llm_base_url,
                surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                rag=rag,
            )
            state = CachedIOMethods.load_cached_final_mas_state(
                surveyor_cache_path=surveyor_cache_path,
            )
            result = await mas.ainvoke(
                input=state,
                # HARDCODED
                config=dict(recursion_limit=100),
            )
            CachedIOMethods.save_cached_final_mas_state(
                state=result,
                result_path=result_file_path,
            )
            logger.success(f"Saved {result_file_path}.")
        except Exception as e:
            logger.error(e)

    @staticmethod
    async def single_run_final_mas_with_multi_query_rag(
        # IO
        surveyor_cache_path: str | Path,
        vector_store_path: str | Path,
        result_file_path: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
        rewriter_llm_model_name: str,
        rewriter_llm_system_message_template_path: str,
    ):
        try:
            # build rag
            rag = QdrantRAGFactory.create_multi_query_rag(
                client_disk_path=vector_store_path,
                collection_name=collection_name,
                embedding_model_name_or_path=embedding_model_name_or_path,
                batch_size=batch_size,
                search_configs=search_configs,
                llm_base_url=llm_base_url,
                rewriter_llm_model_name=rewriter_llm_model_name,
                rewriter_llm_system_message_template_path=rewriter_llm_system_message_template_path,
            )
            # build mas
            mas = CachedMASFactory.create_cached_final_mas(
                llm_base_url=llm_base_url,
                surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                rag=rag,
            )
            state = CachedIOMethods.load_cached_final_mas_state(
                surveyor_cache_path=surveyor_cache_path,
            )
            result = await mas.ainvoke(
                input=state,
                # HARDCODED
                config=dict(recursion_limit=100),
            )
            CachedIOMethods.save_cached_final_mas_state(
                state=result,
                result_path=result_file_path,
            )
            logger.success(f"Saved {result_file_path}.")
        except Exception as e:
            logger.error(e)

    @staticmethod
    async def batch_run_final_mas_with_simple_rag(
        # Runtime
        max_concurrent: int,
        # IO
        surveyor_cache_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
    ):
        # runtime
        semaphore = asyncio.Semaphore(max_concurrent)
        tasks = []
        # path processing
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        surveyor_cache_dir = Path(surveyor_cache_dir)
        surveyor_cache_path_list = list(surveyor_cache_dir.glob('*.txt'))
        vector_store_dir = Path(vector_store_dir)
        # make tasks
        for surveyor_cache_path in surveyor_cache_path_list:
            result_file_path = result_dir / f"{surveyor_cache_path.stem}.json"
            vector_store_path = vector_store_dir / f"{surveyor_cache_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                tasks.append(
                    semaphore_wrapper(
                        semaphore=semaphore,
                        func=CachedFinalMASRunner.single_run_final_mas_with_simple_rag,
                        # IO
                        surveyor_cache_path=surveyor_cache_path,
                        vector_store_path=vector_store_path,
                        result_file_path=result_file_path,
                        # MAS configurations
                        llm_base_url=llm_base_url,
                        surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                        investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                        investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                        adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                        adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                        analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                        analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                        # RAG configurations
                        collection_name=collection_name,
                        embedding_model_name_or_path=embedding_model_name_or_path,
                        batch_size=batch_size,
                        # Retriever
                        search_configs=search_configs,
                    )
                )
        # batch run experiments
        await asyncio.gather(*tasks, return_exceptions=False)

    @staticmethod
    async def batch_run_final_mas_with_multi_query_rag(
        # Runtime
        max_concurrent: int,
        # IO
        surveyor_cache_dir: str | Path,
        vector_store_dir: str | Path,
        result_dir: str | Path,
        # MAS configurations
        llm_base_url: str,
        surveyor_main_llm_system_message_template_path: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_system_message_template_path: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG configurations
        collection_name: str,
        embedding_model_name_or_path: str,
        batch_size: int,
        # Retriever
        search_configs: dict,
        rewriter_llm_model_name: str,
        rewriter_llm_system_message_template_path: str,
    ):
        # runtime
        semaphore = asyncio.Semaphore(max_concurrent)
        tasks = []
        # path processing
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)
        surveyor_cache_dir = Path(surveyor_cache_dir)
        surveyor_cache_path_list = list(surveyor_cache_dir.glob('*.txt'))
        vector_store_dir = Path(vector_store_dir)
        # make tasks
        for surveyor_cache_path in surveyor_cache_path_list:
            result_file_path = result_dir / f"{surveyor_cache_path.stem}.json"
            vector_store_path = vector_store_dir / f"{surveyor_cache_path.stem}"
            if not vector_store_path.exists():
                logger.error(f"Vector store {vector_store_path} does not exist")
                continue
            if not result_file_path.exists():
                tasks.append(
                    semaphore_wrapper(
                        semaphore=semaphore,
                        func=CachedFinalMASRunner.single_run_final_mas_with_multi_query_rag,
                        # IO
                        surveyor_cache_path=surveyor_cache_path,
                        vector_store_path=vector_store_path,
                        result_file_path=result_file_path,
                        # MAS configurations
                        llm_base_url=llm_base_url,
                        surveyor_main_llm_system_message_template_path=surveyor_main_llm_system_message_template_path,
                        investigator_main_llm_system_message_template_path=investigator_main_llm_system_message_template_path,
                        investigator_formatter_llm_system_message_template_path=investigator_formatter_llm_system_message_template_path,
                        adjudicator_main_llm_system_message_template_path=adjudicator_main_llm_system_message_template_path,
                        adjudicator_formatter_llm_system_message_template_path=adjudicator_formatter_llm_system_message_template_path,
                        analyst_main_llm_system_message_template_path=analyst_main_llm_system_message_template_path,
                        analyst_formatter_llm_system_message_template_path=analyst_formatter_llm_system_message_template_path,
                        # RAG configurations
                        collection_name=collection_name,
                        embedding_model_name_or_path=embedding_model_name_or_path,
                        batch_size=batch_size,
                        # Retriever
                        search_configs=search_configs,
                        rewriter_llm_model_name=rewriter_llm_model_name,
                        rewriter_llm_system_message_template_path=rewriter_llm_system_message_template_path,
                    )
                )
        # batch run experiments
        await asyncio.gather(*tasks, return_exceptions=False)

