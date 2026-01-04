"""
选择处于正常交易状态的公司。
"""

from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_active_companies(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    通过公司活动情况，选择处于交易的公司。

    Args:
        df:

    Returns:

    """
    df_ = df[df['Statco'].isin(['A'])]  # 也可以增加'N'。
    return df_

