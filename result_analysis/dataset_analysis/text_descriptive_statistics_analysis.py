"""
对文本进行描述统计分析。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def calculate_markdown_character_length(
    target_dir: str | Path,
) -> dict[str, int]:
    target_dir = Path(target_dir)
    markdown_file_path_list = list(target_dir.glob('*.md'))
    stats_dict = {
        markdown_file_path.stem: len(markdown_file_path.read_text(encoding='utf-8'))
        for markdown_file_path in markdown_file_path_list
    }
    return stats_dict

