"""
构建初始的pdf数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)
from data_processing.utils.copy_pdf import copy_pdf_by_csmar_stock_code

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_original_pdf_dir(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    raw_pdf_dir: str | Path,
    target_dir: str | Path,
) -> None:
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    logger.info(f"Processing ST Companies {st_companies_path}")
    copy_pdf_by_csmar_stock_code(
        target_pdf_name_list=list(st_companies_df['Stkcd']),
        source_dir=raw_pdf_dir,
        target_dir=target_dir,
    )
    logger.success(f"Copied ST Companies {target_dir}")
    logger.info(f"Processing Matching Sample {matching_sample_path}")
    copy_pdf_by_csmar_stock_code(
        target_pdf_name_list=list(matching_sample_df['Stkcd']),
        source_dir=raw_pdf_dir,
        target_dir=target_dir,
    )
    logger.success(f"Copied Matching Sample {target_dir}")


def main(

):
    ...


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    raw_pdf_dir_ = r"D:\dataset\smart\original_data\cninfo"
    target_dir_ = r"D:\dataset\smart\original_data\sample"
    make_original_pdf_dir(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        raw_pdf_dir=raw_pdf_dir_,
        target_dir=target_dir_,
    )

