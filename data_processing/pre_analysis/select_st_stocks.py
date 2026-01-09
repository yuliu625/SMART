"""
选择ST公司的方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_st_by_stock_name(
    df: pd.DataFrame,
    stock_name_column: str,
) -> pd.DataFrame:
    """
    默认筛选方法，通过Stock Name中的ST pattern。

    Args:
        df (pd.DataFrame): 符合CSMAR字段设置的数据集。需要提前的预处理。
        stock_name_column (str): CSMAR中的字段名。

    Returns:
        pd.DataFrame: 筛选后的数据集。
    """
    df_ = df[df[stock_name_column].str.contains('ST')]  # 官方规定为含有ST。
    logger.trace("CSMAR TRD Co:", df_)
    return df_


def select_and_save_st_by_stock_name(
    df: pd.DataFrame,
    stock_name_column: str,
    result_path: str,
) -> pd.DataFrame:
    df_ = df[df[stock_name_column].str.contains('ST')]
    logger.trace("CSMAR TRD Co:", df_)
    df_.to_excel(result_path, index=False)
    return df_

