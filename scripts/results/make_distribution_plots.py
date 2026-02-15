"""
基础数据相关，构造基于CSMAR数据的分布图。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)
from result_analysis.dataset_analysis.csmar_descriptive_statistics_analysis import (
    calculate_csmar_categorical_distribution,
    calculate_csmar_market_type_distribution,
    calculate_csmar_ownership_type_distribution,
)
from result_analysis.visualization.categorical_distribution_plots import (
    CategoricalDistributionPlots,
)
from result_analysis.visualization.market_type_distribution_plots import (
    MarketTypeDistributionPlots,
)
from result_analysis.visualization.ownership_type_distribution_plots import (
    OwnershipTypeDistributionPlots,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_categorical_distribution_plots(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
) -> None:
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    st_companies_series = calculate_csmar_categorical_distribution(
        df=st_companies_df,
        is_normalize=False,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    matching_sample_series = calculate_csmar_categorical_distribution(
        df=matching_sample_df,
        is_normalize=False,
    )
    # print(st_companies_series)
    # print(matching_sample_series)
    CategoricalDistributionPlots.make_categorical_distribution_plot(
        st_companies_series=st_companies_series,
        matching_sample_series=matching_sample_series,
    ).write_image(
        result_path,
        scale=2,
    )


def make_market_type_distribution_plots(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
) -> None:
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    st_companies_series = calculate_csmar_market_type_distribution(
        df=st_companies_df ,
        is_normalize=False,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    matching_sample_series = calculate_csmar_market_type_distribution(
        df=matching_sample_df,
        is_normalize=False,
    )
    MarketTypeDistributionPlots.make_market_type_distribution_plot(
        st_companies_series=st_companies_series,
        matching_sample_series=matching_sample_series,
    ).write_image(
        result_path,
        scale=2,
    )


def make_ownership_type_distribution_plots(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
) -> None:
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    st_companies_series = calculate_csmar_ownership_type_distribution(
        df=st_companies_df ,
        is_normalize=False,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    matching_sample_series = calculate_csmar_ownership_type_distribution(
        df=matching_sample_df,
        is_normalize=False,
    )
    OwnershipTypeDistributionPlots.make_ownership_type_distribution_plot(
        st_companies_series=st_companies_series,
        matching_sample_series=matching_sample_series,
    ).write_image(
        result_path,
        scale=2,
    )


def main() -> None:
    ...


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    make_categorical_distribution_plots(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        result_path=r"./categorical_distribution_plot.png",
    )
    make_market_type_distribution_plots(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        result_path=r"./market_type_distribution_plot.png",
    )
    make_ownership_type_distribution_plots(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        result_path=r"./ownership_type_distribution_plot.png",
    )

