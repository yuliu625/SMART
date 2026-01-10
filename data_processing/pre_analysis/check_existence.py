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
    file_type: str,
):
    ...

