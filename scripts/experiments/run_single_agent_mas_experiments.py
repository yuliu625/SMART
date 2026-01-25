"""
Design Patter: single agent.
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas_runner.single_agent_mas_runner import SingleAgentMASRunner

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

# ==== 批量运行预测试。 ====
async def test_run_ollama(
    markdown_files_dir: str | Path,
    result_dir: str | Path,
):
    # 仅测试使用。
    await SingleAgentMASRunner.run_via_ollama(
        markdown_files_dir=markdown_files_dir,
        result_dir=result_dir,
        adjudicator_main_llm_model_name=r'qwen2.5:1.5b',
        adjudicator_main_llm_system_message_template_path=r"/mas/prompts/single_agent\adjudicator_main_llm_system_prompt_template.j2",
        adjudicator_formatter_llm_model_name=r'qwen2.5:1.5b',
        adjudicator_formatter_llm_system_message_template_path=r"/mas/prompts/single_agent\adjudicator_formatter_llm_system_prompt_template.j2",
    )


# ==== 正式通过vllm运行。 ====
async def run_qwen_25_7b_instruct_1m(
    markdown_files_dir: str | Path,
    result_dir: str | Path,
):
    await SingleAgentMASRunner.run_via_vllm(
        # IO
        markdown_files_dir=markdown_files_dir,
        result_dir=result_dir,
        # MAS configurations
        adjudicator_main_llm_base_url=r'http://localhost:12345/v1/chat/completions',
        adjudicator_main_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_main_llm_system_message_template_path=r'/home/liuyu/workspace/code/smart/mas/prompts/single_agent/adjudicator_main_llm_system_prompt_template.j2',
        adjudicator_formatter_llm_base_url=r'http://localhost:12345/v1/chat/completions',
        adjudicator_formatter_llm_model_name=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
        adjudicator_formatter_llm_system_message_template_path=r'/home/liuyu/workspace/code/smart/mas/prompts/single_agent/adjudicator_formatter_llm_system_prompt_template.j2',
    )


async def main():
    # markdown1
    ## pymupdf1
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/pymupdf_2',
    )
    ## docling1
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_1',
    )
    ## docling2
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/docling_2',
    )
    ## vlm1
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_1',
    )
    ## vlm2
    await run_qwen_25_7b_instruct_1m(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_results/markdown_1/vlm_2',
    )


if __name__ == '__main__':
    # 仅ollama测试。
    # asyncio.run(run_ollama_test(
    #     markdown_files_dir=r"",
    #     result_dir=r"",
    # ))
    # 正式运行。
    asyncio.run(main())

