"""
构建展示公司的table。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
):
    st_companies_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=st_companies_path,
    )
    matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
        processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
    )
    # print(st_companies_df[['Stkcd', 'Conme_en', 'Nnindnme', 'OWNERSHIPTYPE', 'Markettype']].style.format(escape="latex").to_latex(
    #     # index=False,
    # ))
    print(
        st_companies_df[['Stkcd', 'Nnindnme', 'OWNERSHIPTYPE', 'Markettype']].style.hide(axis="index").format(
            escape="latex"
            ).to_latex(
            hrules=True,
        )
    )
    # print(matching_sample_df[['Stkcd', 'Conme_en', 'Nnindnme', 'OWNERSHIPTYPE', 'Markettype']].style.format(escape="latex").to_latex(
    #     # index=False,
    # ))
    print(
        matching_sample_df[['Stkcd', 'Nnindnme', 'OWNERSHIPTYPE', 'Markettype']].style.hide(axis="index").format(
            escape="latex"
            ).to_latex(
            hrules=True
        )
    )


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main(st_companies_path_, matching_sample_path_)

