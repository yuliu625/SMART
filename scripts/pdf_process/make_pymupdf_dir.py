"""
通过pymupdf构建的markdown数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_pymupdf4llm import (
    convert_pdf_via_pymupdf4llm,
    convert_pdf_via_pymupdf4llm_with_images
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

