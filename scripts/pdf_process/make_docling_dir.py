"""
通过docling构建的markdown数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_docling import (
    build_pdf_pipeline_options,
    convert_pdf_via_docling,
    batch_convert_pdf_via_docling,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def default_batch_conver_pdf_via_docling(
    pdf_path: str | Path,
    result_dir: str | Path,
) -> None:
    ...


def main(

):
    ...


if __name__ == '__main__':
    # 默认转换方法。
    pdf_dir_ = r""
    result_dir_ = r""

