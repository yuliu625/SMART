"""
构建原始的数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import (
    read_xlsx_from_csmar_trd_co,
    read_processed_xlsx_from_csmar_trd_co,
)
from data_processing.pre_analysis.select_active_companies import select_active_companies
from data_processing.pre_analysis.select_a_share_companies import select_a_share_companies_by_market_type
from data_processing.pre_analysis.select_not_st_companies import select_csmar_not_st_companies_by_csmar_st_stock_code

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
    # 选择A股公司。
    df = select_a_share_companies_by_market_type(
        df=csmar_trd_co_df,
    )
    # 选择处于交易状态的公司。
    df = select_active_companies(
        df=df,
    )
    # 保存。
    df.to_excel(result_path, index=False)
    # 这里的保存以及不再有多于的字段说明记录。
    logger.success(f"Saved {result_path}")


def make_not_st_companies(
    processed_csmar_trd_co_all_xlsx_file_path: str | Path,
    processed_csmar_trd_co_st_xlsx_file_path: str | Path,
    result_path: str | Path,
) -> None:
    all_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=processed_csmar_trd_co_all_xlsx_file_path,
    )
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=processed_csmar_trd_co_st_xlsx_file_path,
    )
    df = select_csmar_not_st_companies_by_csmar_st_stock_code(
        all_companies_df=all_companies_df,
        st_companies_df=st_companies_df,
    )
    # 保存。
    df.to_excel(result_path, index=False)
    logger.success(f"Saved {result_path}")


def main(

):
    ...


if __name__ == '__main__':
    # 处理全部公司的数据。
    csmar_trd_co_new_file_path_ = r"D:\dataset\smart\original_data\csmar\TRD_Co_new.xlsx"
    all_companies_path_ = r"D:\dataset\smart\original_data\csmar\all_companies_in_2024.xlsx"
    make_target_companies_in_2024(
        csmar_trd_co_xlsx_file_path=csmar_trd_co_new_file_path_,
        result_path=all_companies_path_,
    )

    # 处理ST公司的数据。
    csmar_trd_co_st_file_path_ = r"D:\dataset\smart\original_data\csmar\TRD_Co_st.xlsx"
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    make_target_companies_in_2024(
        csmar_trd_co_xlsx_file_path=csmar_trd_co_st_file_path_,
        result_path=st_companies_path_,
    )

    # 处理非ST公司的数据。
    all_companies_path_ = r"D:\dataset\smart\original_data\csmar\all_companies_in_2024.xlsx"
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    not_st_companies_path_ = r"D:\dataset\smart\original_data\csmar\not_st_companies_in_2024.xlsx"
    make_not_st_companies(
        processed_csmar_trd_co_all_xlsx_file_path=all_companies_path_,
        processed_csmar_trd_co_st_xlsx_file_path=st_companies_path_,
        result_path=not_st_companies_path_,
    )

