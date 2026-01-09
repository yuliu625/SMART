"""
读取原始数据库中获取的数据的方法。
"""

from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def read_xlsx_from_csmar_trd_co(
    csmar_trd_co_xlsx_file_path: str,
) -> pd.DataFrame:
    """
    读取从CSMAR数据的xlsx数据。

    Args:
        csmar_trd_co_xlsx_file_path (str): CSMAR导出的xlsx数据集的路径。

    Returns:
        pd.DataFrame: 可以正常处理的df。
    """
    df = pd.read_excel(
        csmar_trd_co_xlsx_file_path,
        skiprows=[1, 2, ],  # 去除2行column说明。
        dtype=str,  # 禁用自动类型推断。全部column都为str。
    )
    return df

