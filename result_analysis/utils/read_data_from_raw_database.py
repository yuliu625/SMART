"""
从原始数据集读取数据的方法。

这里从外部导入使用data_processing.pre_analysis.read_data_from_raw_database.py中的方法。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
    read_processed_xlsx_from_csmar_fs_combas,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
