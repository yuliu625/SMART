"""
对于 dashscope 的文件处理方法。

暂时只考虑一次性上传成果的情况。
"""

from __future__ import annotations
from loguru import logger

from data_processing.cache.openai_file_manager import OpenAIFileManager

from pathlib import Path
import os
import json

from typing import TYPE_CHECKING, Sequence
# if TYPE_CHECKING:


def upload_files(
    target_file_paths: Sequence[str | Path],
) -> list[dict]:
    # HARDCODED
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    api_key = os.getenv("DASHSCOPE_API_KEY")
    # upload files
    result = OpenAIFileManager.create_files(
        base_url=base_url,
        api_key=api_key,
        file_paths=target_file_paths,
        purpose='file-extract',  # 官方文档指定。
    )
    return result


def upload_files_and_save_results(
    target_file_paths: Sequence[str | Path],
    result_path: str | Path,
) -> list[dict]:
    # HARDCODED
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    api_key = os.getenv("DASHSCOPE_API_KEY")
    # upload files
    result = OpenAIFileManager.create_files(
        base_url=base_url,
        api_key=api_key,
        file_paths=target_file_paths,
        purpose='file-extract',  # 官方文档指定。
    )
    # save results
    result_path = Path(result_path)
    logger.info(f"Uploading result: \n{result}")
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=4),
        encoding='utf-8',
    )
    logger.success(f"Saved result to {result_path}")
    return result


def list_uploaded_files() -> list[dict]:
    # HARDCODED
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    api_key = os.getenv("DASHSCOPE_API_KEY")
    result = OpenAIFileManager.list_files(
        base_url=base_url,
        api_key=api_key,
    )
    return result

