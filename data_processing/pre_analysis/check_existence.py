"""
检查文件的存在情况。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pandas as pd


def check_original_pdf_existence(
    target_name_list: list[str],
    pdf_dir: str | Path,
) -> None:
    # 匹配所有一级目录下的pdf文件。
    pdf_path_list: list[Path] = list(
        Path(pdf_dir).rglob("*.pdf")
    )
    # 获取pdf_name，只需要前6位stock code。
    pdf_name_list: list[str] = [pdf_path.stem[:6] for pdf_path in pdf_path_list]
    # 遍历所有的目标文件，查询是否在本地实际文件中存在。
    for target_name in target_name_list:
        if target_name not in pdf_name_list:
            logger.warning(f"PDF file {target_name} not exist.")

