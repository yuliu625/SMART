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
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    for pdf_name in target_pdf_name_list:
        found_files = list(source_dir.glob(f"{pdf_name}*"))
        shutil.copy2(found_files[0], target_dir / f"{pdf_name}.pdf")

