"""
通过docling构建的markdown数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_docling import (
    set_pdf_pipeline,
    convert_pdf_via_docling,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

