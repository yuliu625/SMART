"""
Design Pattern: MAS.
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas_runner.final_mas_runner import FinalMASRunner

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


async def run_qwen_25_7b_instruct_with_nomic(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    # await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
    #     # IO
    #     markdown_files_dir=markdown_files_dir,
    #     vector_store_dir=vector_store_dir,
    #     result_dir=result_dir,
    #     # MAS configurations
    #     surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
    #     investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
    #     investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
    #     adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
    #     adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
    #     analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
    #     analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
    #     # RAG configurations
    #     embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
    #     embedding_model_model_kwargs=dict(trust_remote_code=True, ),
    #     embedding_model_encode_kwargs=dict(prompt='search_document: '),
    #     embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
    #     # Retriever
    #     search_configs=dict(),
    # )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(prompt='search_document: '),
        embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
        rag_llm_base_url=r'http://127.0.0.1:8972/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def run_qwen_25_7b_instruct_with_bge(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    # await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
    #     # IO
    #     markdown_files_dir=markdown_files_dir,
    #     vector_store_dir=vector_store_dir,
    #     result_dir=result_dir,
    #     # MAS configurations
    #     surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
    #     investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
    #     investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
    #     adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
    #     adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
    #     analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
    #     analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
    #     # RAG configurations
    #     embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
    #     embedding_model_model_kwargs=dict(trust_remote_code=True, ),
    #     embedding_model_encode_kwargs=dict(),
    #     embedding_model_query_encode_kwargs=dict(),
    #     # Retriever
    #     search_configs=dict(),
    # )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        rag_llm_base_url=r'http://127.0.0.1:8972/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def run_qwen_25_7b_instruct_with_jina(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    # await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
    #     # IO
    #     markdown_files_dir=markdown_files_dir,
    #     vector_store_dir=vector_store_dir,
    #     result_dir=result_dir,
    #     # MAS configurations
    #     surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
    #     investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
    #     investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
    #     adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    #     adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
    #     adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
    #     analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
    #     analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
    #     analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
    #     analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
    #     # RAG configurations
    #     embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/jinaai/jina-embeddings-v4",
    #     embedding_model_model_kwargs=dict(trust_remote_code=True, ),
    #     embedding_model_encode_kwargs=dict(),
    #     embedding_model_query_encode_kwargs=dict(),
    #     # Retriever
    #     search_configs=dict(),
    # )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8972/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/jinaai/jina-embeddings-v4",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        rag_llm_base_url=r'http://127.0.0.1:8972/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def run_qwen_25_7b_instruct_1m_with_nomic(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(prompt='search_document: '),
        embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
        # Retriever
        search_configs=dict(),
    )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(prompt='search_document: '),
        embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
        rag_llm_base_url=r'http://127.0.0.1:8976/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def run_qwen_25_7b_instruct_1m_with_bge(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        # Retriever
        search_configs=dict(),
    )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        rag_llm_base_url=r'http://127.0.0.1:8976/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def run_qwen_25_7b_instruct_1m_with_jina(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_simple_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/jinaai/jina-embeddings-v4",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        # Retriever
        search_configs=dict(),
    )
    # Multi-Query RAG
    await FinalMASRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/surveyor_main_llm_system_prompt_template.j2",
        investigator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_main_llm_system_prompt_template.j2",
        investigator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        investigator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        investigator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/investigator_formatter_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/adjudicator_formatter_llm_system_prompt_template.j2",
        analyst_main_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_main_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_main_llm_system_prompt_template.j2",
        analyst_formatter_llm_base_url=r'http://127.0.0.1:8976/v1',
        analyst_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        analyst_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/final_mas/analyst_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/jinaai/jina-embeddings-v4",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        rag_llm_base_url=r'http://127.0.0.1:8976/v1',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def main():
    # qwen2.5-7b-instruct
    # markdown1
    # nomic
    ## pymupdf1
    await run_qwen_25_7b_instruct_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/nomic/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/nomic/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/nomic/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/nomic/markdown_1/docling_2',
    )
    ## vlm1
    # await run_qwen_25_7b_instruct_with_nomic(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/vlm_1',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_1',
    # )
    ## vlm2
    # await run_qwen_25_7b_instruct_with_nomic(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/vlm_2',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_2',
    # )
    # bge
    ## pymupdf1
    await run_qwen_25_7b_instruct_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/bge/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/bge/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/bge/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/bge/markdown_1/docling_2',
    )
    ## vlm1
    # await run_qwen_25_7b_instruct_with_bge(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/vlm_1',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_1',
    # )
    ## vlm2
    # await run_qwen_25_7b_instruct_with_bge(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/vlm_2',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_2',
    # )
    # jina
    ## pymupdf1
    await run_qwen_25_7b_instruct_with_jina(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jina/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/jina/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_with_jina(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jina/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/jina/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_with_jina(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jina/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/jina/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_with_jina(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jina/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/jina/markdown_1/docling_2',
    )
    ## vlm1
    # await run_qwen_25_7b_instruct_with_jina(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jian/markdown_1/vlm_1',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_1',
    # )
    ## vlm2
    # await run_qwen_25_7b_instruct_with_jina(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
    #     vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/jina/markdown_1/vlm_2',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results_mas/qwen_25_7b_instruct/markdown_1/vlm_2',
    # )


if __name__ == '__main__':
    asyncio.run(main())


