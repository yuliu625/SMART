"""
构造基本文本特征分布图。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)
from result_analysis.dataset_analysis.text_descriptive_statistics_analysis import (
    calculate_markdown_character_length,
    calculate_pdf_page_number,
)
from result_analysis.utils.select_target_records import (
    select_target_records_by_id,
)
from result_analysis.visualization.character_length_distribution_plots import (
    CharacterLengthDistributionPlots,
)
from result_analysis.visualization.page_number_distribution_plots import (
    PageNumberDistributionPlots,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_character_length_distribution_plots(
    target_dir: str | Path,
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
):
    stats_dict = calculate_markdown_character_length(
        target_dir=target_dir,
    )
    character_length_df = pd.DataFrame(
        list(stats_dict.items()),
        columns=['Stkcd', 'character_length'],
    )
    logger.trace(f"\nAll: \n{character_length_df}")
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    st_companies_character_length_df = select_target_records_by_id(
        original_df=character_length_df,
        target_ids=st_companies_df['Stkcd'],
        target_id_name='Stkcd',
        target_field_name='character_length',
    )
    logger.trace(f"\nST: \n{st_companies_character_length_df}")
    matching_sample_character_length_df = select_target_records_by_id(
        original_df=character_length_df,
        target_ids=matching_sample_df['Stkcd'],
        target_id_name='Stkcd',
        target_field_name='character_length',
    )
    logger.trace(f"\nMATCHING: \n{matching_sample_character_length_df}")
    CharacterLengthDistributionPlots.make_character_length_distribution_plot(
        st_companies_df=st_companies_character_length_df,
        matching_sample_df=matching_sample_character_length_df,
    ).write_image(
        result_path,
        scale=2,
    )


def make_page_number_distribution_plots(
    target_dir: str | Path,
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    result_path: str | Path,
):
    stats_dict = calculate_pdf_page_number(
        target_dir=target_dir,
    )
    page_number_df = pd.DataFrame(
        list(stats_dict.items()),
        columns=['Stkcd', 'page_number'],
    )
    logger.trace(f"\nAll: \n{page_number_df}")
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    st_companies_page_number_df = select_target_records_by_id(
        original_df=page_number_df,
        target_ids=st_companies_df['Stkcd'],
        target_id_name='Stkcd',
        target_field_name='page_number',
    )
    logger.trace(f"\nST: \n{st_companies_page_number_df}")
    matching_sample_page_number_df = select_target_records_by_id(
        original_df=page_number_df,
        target_ids=matching_sample_df['Stkcd'],
        target_id_name='Stkcd',
        target_field_name='page_number',
    )
    logger.trace(f"\nMATCHING: \n{matching_sample_page_number_df}")
    PageNumberDistributionPlots.make_page_number_distribution_plot(
        st_companies_df=st_companies_page_number_df,
        matching_sample_df=matching_sample_page_number_df,
    ).write_image(
        result_path,
        scale=2,
    )


if __name__ == '__main__':
    # Character Length
    make_character_length_distribution_plots(
        target_dir=r"D:\dataset\smart\data_pipeline_cache\markdown_1\docling_1",
        st_companies_path=r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx",
        matching_sample_path=r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx",
        result_path=r"./character_length_distribution_plot.png",
    )
    # Page Number
    make_page_number_distribution_plots(
        target_dir=r"D:\dataset\smart\experimental_datasets\sample_1",
        st_companies_path=r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx",
        matching_sample_path=r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx",
        result_path=r"./page_number_distribution_plot.png",
    )

