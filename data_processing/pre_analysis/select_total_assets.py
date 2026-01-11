"""
从资产负债表中获取公司总资产。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_total_assets(
    df: pd.DataFrame,
    target_date: str,
) -> pd.DataFrame:
    df_ = (
        df.query("Accper == @target_date and Typrep == 'A'")  # 目标统计日期。只要年报，不要合并报表。
        .sort_values(['Stkcd', 'DeclareDate'])  # 确保更正日期升序
        .drop_duplicates(subset=['Stkcd'], keep='last')  # 只保留最新披露的那条
        .loc[:, ['Stkcd', 'ShortName', 'Accper', 'A001000000']]  # 精确投影所需列
    )
    logger.trace("Total Assets: \n", df_)
    return df_


def select_and_save_total_assets(
    df: pd.DataFrame,
    target_date: str,
    result_path: str,
) -> pd.DataFrame:
    df_ = (
        df.query("Accper == @target_date and Typrep == 'A'")  # 目标统计日期。只要年报，不要合并报表。
        .sort_values(['Stkcd', 'DeclareDate'])  # 确保更正日期升序
        .drop_duplicates(subset=['Stkcd'], keep='last')  # 只保留最新披露的那条
        .loc[:, ['Stkcd', 'ShortName', 'Accper', 'A001000000']]  # 精确投影所需列
    )
    logger.trace("Total Assets: \n", df_)
    df_.to_excel(result_path, index=False)
    logger.success(f"Save to {result_path}")
    return df_

