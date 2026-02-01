"""
基础数据相关，部分数据处理，构造基于CSMAR数据的总资产分布图。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)
from result_analysis.visualization.total_assets_distribution_plots import (
    TotalAssetsDistributionPlots,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_total_assets_distribution_plots(
    total_assets_path: str | Path,
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
) -> None:
    # read dataset
    total_assets_df = pd.read_excel(
        total_assets_path,
        dtype=dict(Stkcd=str)
    )
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    # select total assets
    st_companies_total_assets_df = total_assets_df[total_assets_df['Stkcd'].isin(st_companies_df['Stkcd'])].copy()
    matching_sample_total_assets_df = total_assets_df[total_assets_df['Stkcd'].isin(matching_sample_df['Stkcd'])].copy()
    # print(st_companies_total_assets_df)
    # print(matching_sample_total_assets_df)
    TotalAssetsDistributionPlots.make_total_assets_distribution_plot(
        st_companies_total_assets_df=st_companies_total_assets_df,
        matching_sample_total_assets_df=matching_sample_total_assets_df,
    ).write_image(
        result_path,
        scale=2,
    )


if __name__ == '__main__':
    total_assets_path_ = r"D:\dataset\smart\original_data\csmar\total_assets_in_2024.xlsx"
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    make_total_assets_distribution_plots(
        total_assets_path=total_assets_path_,
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        result_path='./total_assets_distribution.png',
    )
