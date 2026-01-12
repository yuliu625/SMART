"""
复制pdf的工具方法。
"""

from __future__ import annotations
from loguru import logger

import shutil
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def copy_pdf_by_csmar_stock_code(
    target_pdf_name_list: list[str],
    source_dir: str | Path,
    target_dir: str | Path,
) -> None:
    # 路径相关预处理。
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Source_dir: {source_dir}. Target_dir: {target_dir}")
    logger.trace(f"target_pdf_name_list={target_pdf_name_list}")
    logger.info(f"Num of pdfs: {len(target_pdf_name_list)}")
    # 逐一处理每个文件。
    for pdf_name in target_pdf_name_list:
        # 正则查找每个文件。
        found_files = list(source_dir.glob(f"{pdf_name}*"))
        logger.debug(f"Found files: {found_files}")
        if len(found_files) == 0:
            logger.error(f"Not found {pdf_name}")
        # 实际能找到一个，进行复制。
        shutil.copy2(found_files[0], target_dir / f"{pdf_name}.pdf")
        # shutil.copy2(found_files[0], target_dir / found_files[0].name)
        logger.debug(f"Copied {pdf_name}.pdf")

