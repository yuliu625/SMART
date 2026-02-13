"""
上传文件到 dashscope 。
"""

from __future__ import annotations
from loguru import logger

from data_processing.cache.dashscope_file_manager import (
    upload_files_and_save_results,
)

from pathlib import Path

from typing import TYPE_CHECKING, Sequence
# if TYPE_CHECKING:


def upload_markdown_files(
    target_dir: str | Path,
    result_path: str | Path,
) -> list[dict]:
    # path processing
    target_dir = Path(target_dir)
    result_path = Path(result_path)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    # markdown files
    markdown_file_paths = list(target_dir.glob('*.md'))
    result = upload_files_and_save_results(
        target_file_paths=markdown_file_paths,
        result_path=result_path,
    )
    return result


if __name__ == '__main__':
    upload_markdown_files(
        target_dir=r"D:\dataset\smart\data_pipeline_cache\markdown_1\docling_1",
        result_path=r"./file_ids.json",
    )

