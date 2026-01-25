"""
Design Pattern: sequential workflow.
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas_runner.sequential_workflow_runner import SequentialWorkflowRunner

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


async def run_qwen_25_7b_instruct_1m_with_nomic(
    markdown_files_dir: str | Path,
    vector_store_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # Simple RAG
    await SequentialWorkflowRunner.run_via_vllm_with_huggingface_simple_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        general_query_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/general_query_human_prompt_template.j2",
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
        embedding_model_model_kwargs=dict(trust_remote_code=True,),
        embedding_model_encode_kwargs=dict(prompt='search_document: '),
        embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
        # Retriever
        search_configs=dict(),
    )
    # Multi-Query RAG
    await SequentialWorkflowRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        general_query_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/general_query_human_prompt_template.j2",
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/nomic-ai/nomic-embed-text-v1.5",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(prompt='search_document: '),
        embedding_model_query_encode_kwargs=dict(prompt='search_query: '),
        rag_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
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
    await SequentialWorkflowRunner.run_via_vllm_with_huggingface_simple_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        general_query_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/general_query_human_prompt_template.j2",
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_model_kwargs=dict(trust_remote_code=True,),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        # Retriever
        search_configs=dict(),
    )
    # Multi-Query RAG
    await SequentialWorkflowRunner.run_via_vllm_with_huggingface_multi_query_rag(
        # IO
        markdown_files_dir=markdown_files_dir,
        general_query_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/general_query_human_prompt_template.j2",
        vector_store_dir=vector_store_dir,
        result_dir=result_dir,
        # MAS configurations
        surveyor_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        surveyor_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        surveyor_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/surveyor_main_llm_system_prompt_template.j2",
        adjudicator_main_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        adjudicator_formatter_llm_model_name=r"/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M",
        adjudicator_formatter_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/sequential_workflow/adjudicator_formatter_llm_system_prompt_template.j2",
        # RAG configurations
        embedding_model_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_model_kwargs=dict(trust_remote_code=True, ),
        embedding_model_encode_kwargs=dict(),
        embedding_model_query_encode_kwargs=dict(),
        rag_llm_base_url=r'http://127.0.0.1:8976/v1/chat/completions',
        rag_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        rag_llm_system_message_template_path=r"/home/liuyu/workspace/code/smart/mas/prompts/rag/rewritter_system_prompt_template.j2",
        # Retriever
        search_configs=dict(),
    )


async def main():
    # markdown1
    # nomic
    ## pymupdf1
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_2',
    )
    ## vlm1
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/vlm_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_1',
    )
    ## vlm2
    await run_qwen_25_7b_instruct_1m_with_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/vlm_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_2',
    )
    # bge
    ## pymupdf1
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_2',
    )
    ## vlm1
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/vlm_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_1',
    )
    ## vlm2
    await run_qwen_25_7b_instruct_1m_with_bge(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
        vector_store_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/bge/markdown_1/vlm_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_2',
    )


if __name__ == '__main__':
    asyncio.run(main())

