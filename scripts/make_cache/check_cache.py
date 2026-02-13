"""
检查各种 cache 的情况。
"""

from __future__ import annotations
from loguru import logger

from data_processing.cache.dashscope_file_manager import (
    list_uploaded_files,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def check_uploaded_files():
    uploaded_files = list_uploaded_files()
    logger.info(f"Uploaded file number: {len(uploaded_files)}")
    logger.info(f"Uploaded files: {uploaded_files}")


if __name__ == '__main__':
    check_uploaded_files()

