"""
检验数据集的正常情况。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pre_analysis.read_data_from_raw_database import read_processed_xlsx_from_csmar_trd_co
from data_processing.utils.check_file_existence import check_original_pdf_existence

from pathlib import Path
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def check_csmar_pdf_existence(
    processed_csmar_trd_co_xlsx_file_path: str | Path,
    pdf_dir: str | Path,
) -> None:
    processed_csmar_trd_co_df: pd.DataFrame = read_processed_xlsx_from_csmar_trd_co(
        csmar_trd_co_xlsx_file_path=processed_csmar_trd_co_xlsx_file_path,
    )
    target_name_list: list[str] = list(
        processed_csmar_trd_co_df['Stkcd']
    )
    check_original_pdf_existence(
        target_name_list=target_name_list,
        pdf_dir=pdf_dir,
    )


def main(

):
    ...


if __name__ == '__main__':
    # 查看全部公司的pdf文件。
    all_companies_path_ = r"D:\dataset\smart\original_data\csmar\all_companies_in_2024.xlsx"
    pdf_dir_ = r"D:\dataset\smart\original_data\cninfo"
    check_csmar_pdf_existence(
        processed_csmar_trd_co_xlsx_file_path=all_companies_path_,
        pdf_dir=pdf_dir_,
    )

    # 查看ST公司的pdf文件。
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    pdf_dir_ = r"D:\dataset\smart\original_data\cninfo"
    check_csmar_pdf_existence(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path_,
        pdf_dir=pdf_dir_,
    )

