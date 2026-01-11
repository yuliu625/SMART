"""
描述统计分析方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def calculate_csmar_market_type_distribution(
    df: pd.DataFrame,
    is_normalize: bool,
) -> pd.Series:
    """
    查看公司所属的市场类型。

    Args:
        df:
        is_normalize:

    Returns:

    """
    market_type_distribution = df['MarketType'].value_counts(normalize=is_normalize)
    logger.trace(f"Market Type Distribution: \n", market_type_distribution)
    return market_type_distribution


def calculate_csmar_categorical_distribution(
    df: pd.DataFrame,
    is_normalize: bool,
) -> pd.Series:
    """
    查看公司所处的行业。

    根据: 2012版证监会行业分类名称。

    Args:
        df:
        is_normalize:

    Returns:

    """
    category_distribution = df['Nnindnme'].value_counts(normalize=is_normalize)
    logger.trace(f"Categorical Distribution: \n", category_distribution)
    return category_distribution


def calculate_csmar_ownership_type_distribution(
    df: pd.DataFrame,
    is_normalize: bool,
) -> pd.Series:
    """
    查看 上市公司经营性质。

    Args:
        df:
        is_normalize:

    Returns:

    """
    ownership_type_distribution = df['OWNERSHIPTYPE'].value_counts(normalize=is_normalize)
    logger.trace(f"Ownership Type Distribution: \n", ownership_type_distribution)
    return ownership_type_distribution

