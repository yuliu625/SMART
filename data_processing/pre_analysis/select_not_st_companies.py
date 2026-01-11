"""
选择不是ST公司的方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_csmar_not_st_companies_by_csmar_st_stock_code(
    all_companies_df: pd.DataFrame,
    st_companies_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    通过排除ST公司的方法，选择非ST公司。

    Args:
        all_companies_df:
        st_companies_df:

    Returns:

    """
    not_st_companies_df = all_companies_df[~all_companies_df['Stkcd'].isin(st_companies_df['Stkcd'])]
    logger.trace(f"CSMAR NOT ST: \n", not_st_companies_df)
    return not_st_companies_df

