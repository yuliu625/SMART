"""
制表使用，基于confusion matrix进行制表。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.experiment_results_analysis.calculate_confusion_matrix import (
    calculate_confusion_matrix,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def collect_confusion_matrix_results(
    result_path: str | Path,
) -> dict:
    ...


def main(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
):
    # final_df = QuantativeResultsMaker.make_quantative_results_df(
    #     st_companies_path=r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx",
    #     matching_sample_path=r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx",
    #     target_dir=r"D:\dataset\smart\experimental_results\qwen_25_7b_instruct\markdown_1\docling_1",
    # )
    # print(final_df.to_dict(orient="records"))
    ...


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
    )

