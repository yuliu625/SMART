"""
构建原始的数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import read_xlsx_from_csmar_trd_co
from data_processing.pre_analysis.select_active_companies import select_active_companies
from data_processing.pre_analysis.select_a_share_companies import select_a_share_companies_by_market_type

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_target_companies_in_2024(
    csmar_trd_co_xlsx_file_path: str | Path,
    result_path: str | Path,
) -> None:
    csmar_trd_co_df = read_xlsx_from_csmar_trd_co(
        csmar_trd_co_xlsx_file_path=csmar_trd_co_xlsx_file_path,
    )
    df = select_a_share_companies_by_market_type(
        df=csmar_trd_co_df,
    )
    df = select_active_companies(
        df=df,
    )
    df.to_excel(result_path, index=False)
    logger.success(f"Saved {result_path}")


def main(

):
    ...


if __name__ == '__main__':
    csmar_trd_co_file_path_ = r""

