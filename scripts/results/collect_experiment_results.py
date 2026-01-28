"""
收集各种条件下的运行结果。

包含直接返回收集结果，以及直接完成序列化。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.experiment_results_analysis.quantative_results_maker import (
    QuantativeResultsMaker,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
):
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"",
        result_path=r"",
    )


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
    )

