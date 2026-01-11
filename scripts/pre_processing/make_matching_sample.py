"""
匹配样本选择。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
    read_processed_xlsx_from_csmar_fs_combas,
)
from data_processing.pre_analysis.select_matching_sample import (
    merge_companies_and_total_assets,
    select_matching_sample_by_total_assets,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_matching_sample_by_total_assets(
    processed_csmar_trd_co_st_xlsx_file_path: str | Path,
    processed_csmar_trd_co_not_st_xlsx_file_path: str | Path,
    processed_csmar_fs_combas_xlsx_file_path: str | Path,
    result_path: str | Path,
) -> None:
    df_st = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=processed_csmar_trd_co_st_xlsx_file_path,
    )
    df_not_st = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=processed_csmar_trd_co_not_st_xlsx_file_path,
    )
    df_total_assets = read_processed_xlsx_from_csmar_fs_combas(
        processed_csmar_fs_combas_xlsx_file_path=processed_csmar_fs_combas_xlsx_file_path,
    )
    df_st_with_total_assets = merge_companies_and_total_assets(
        df_companies=df_st,
        df_total_assets=df_total_assets,
    )
    df_not_st_with_total_assets = merge_companies_and_total_assets(
        df_companies=df_not_st,
        df_total_assets=df_total_assets,
    )
    df_matching_sample = select_matching_sample_by_total_assets(
        df_st_with_total_assets=df_st_with_total_assets,
        df_not_st_with_total_assets=df_not_st_with_total_assets,
    )
    df_matching_sample.to_excel(result_path, index=False)
    logger.success(f"Save matching sample to {result_path}")


def main(

):
    ...


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    not_st_companies_path_ = r"D:\dataset\smart\original_data\csmar\not_st_companies_in_2024.xlsx"
    total_assets_path_ = r"D:\dataset\smart\original_data\csmar\total_assets_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    make_matching_sample_by_total_assets(
        processed_csmar_trd_co_st_xlsx_file_path=st_companies_path_,
        processed_csmar_trd_co_not_st_xlsx_file_path=not_st_companies_path_,
        processed_csmar_fs_combas_xlsx_file_path=total_assets_path_,
        result_path=matching_sample_path_,
    )

