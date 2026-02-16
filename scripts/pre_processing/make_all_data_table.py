"""
将所有相关 field 放在一张表中。以便进行后续分析。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
    read_processed_xlsx_from_csmar_fs_combas,
)
from result_analysis.dataset_analysis.text_descriptive_statistics_analysis import (
    calculate_markdown_character_length,
    calculate_pdf_page_number,
)
from result_analysis.utils.select_target_records import (
    select_target_records_by_id,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_all_in_one_table(
    all_companies_path: str | Path,
    total_assets_path: str | Path,
    pdf_dir: str | Path,
    markdown_dir: str | Path,
    result_path: str | Path,
):
    # treatment group and control group df
    all_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=all_companies_path,
    )
    all_companies_df = all_companies_df[['Stkcd', 'Nnindnme', 'Markettype', 'OWNERSHIPTYPE']]
    logger.debug(f"\nAll companies df: \n{all_companies_df}")
    # total assets df
    total_assets_df = pd.read_excel(
        total_assets_path,
        dtype=dict(Stkcd=str)
    )
    sample_total_assets_df = total_assets_df[total_assets_df['Stkcd'].isin(all_companies_df['Stkcd'])].copy()
    sample_total_assets_df = sample_total_assets_df[['Stkcd', 'A001000000']]
    logger.debug(f"\nAll total_assets_df: \n{sample_total_assets_df}")
    # pdf
    # page_number_stats_dict = calculate_pdf_page_number(
    #     target_dir=pdf_dir,
    # )
    # page_number_df = pd.DataFrame(
    #     list(page_number_stats_dict.items()),
    #     columns=['Stkcd', 'page_number'],
    # )
    # logger.debug(f"\nPage Number df: \n{page_number_df}")
    # markdown
    # markdown_stats_dict = calculate_markdown_character_length(
    #     target_dir=markdown_dir,
    # )
    # character_length_df = pd.DataFrame(
    #     list(markdown_stats_dict.items()),
    #     columns=['Stkcd', 'character_length'],
    # )
    # logger.debug(f"\nCharacter length df: \n{character_length_df}")
    # result
    result_df = pd.merge(all_companies_df, sample_total_assets_df, on='Stkcd', how='inner',)
    # result_df = pd.merge(result_df, page_number_df, on='Stkcd', how='inner',)
    # result_df = pd.merge(result_df, character_length_df, on='Stkcd', how='inner',)
    logger.debug(f"\nResult df: \n{result_df}")
    result_df.to_excel(
        result_path,
        index=False,
    )
    logger.success(f"Saved {result_path}")


if __name__ == '__main__':
    all_companies_path_ = r"D:\dataset\smart\original_data\csmar\all_companies_in_2024.xlsx"
    total_assets_path_ = r"D:\dataset\smart\original_data\csmar\total_assets_in_2024.xlsx"
    pdf_dir_ = r"D:\dataset\smart\experimental_datasets\sample_1"
    markdown_dir_ = r"D:\dataset\smart\data_pipeline_cache\markdown_1\docling_1"
    make_all_in_one_table(
        all_companies_path=all_companies_path_,
        total_assets_path=total_assets_path_,
        pdf_dir=pdf_dir_,
        markdown_dir=markdown_dir_,
        result_path=r"D:\dataset\smart\original_data/all_data_all_in_one.xlsx",
    )

