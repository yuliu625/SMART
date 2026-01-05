"""
选择A股上市的公司。
"""

from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_a_share_companies_by_market_type(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    通过市场类型选择，选择A股公司。

    Args:
        df (pd.DataFrame): 符合CSMAR字段设置的数据集。需要提前的预处理。

    Returns:
        pd.DataFrame: 筛选后的数据集。
    """
    df_ = df[df['Markettype'].isin(['1', '4', '16', '32', '64'])]
    return df_


def select_a_share_companies_by_currency(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    通过交易货币，选择A股公司。

    这个方法作为辅助验证，因为B股可能以其他货币进行交易。

    Args:
        df (pd.DataFrame): 符合CSMAR字段设置的数据集。需要提前的预处理。

    Returns:
        pd.DataFrame: 筛选后的数据集。
    """
    df_ = df[df['Curtrd'] == 'CNY']
    return df_

