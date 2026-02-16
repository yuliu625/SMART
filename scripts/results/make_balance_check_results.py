"""
量化平衡性，生成平衡性检验表。
"""

from __future__ import annotations
from loguru import logger

from tableone import TableOne
import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_balance_check_table(
    all_in_one_df_path: str | Path,
    columns: list[str],
    categorical: list[str],
    result_path: str | Path,
):
    all_in_one_df = pd.read_excel(
        all_in_one_df_path,
        dtype=dict(Stkcd=str),
    )
    # HARDCODED
    # columns = ['Nnindnme', 'Markettype', 'OWNERSHIPTYPE', 'A001000000', 'page_number', 'character_length',]
    # categorical = ['Nnindnme', 'Markettype', 'OWNERSHIPTYPE',]
    # columns = ['A001000000', 'page_number', 'character_length',]
    # categorical = []
    groupby = 'is_risk'
    table = TableOne(
        all_in_one_df,
        columns=columns,
        categorical=categorical,
        groupby=groupby,
        pval=True, smd=True,
    )
    logger.debug(f"\nTable: \n{table.tabulate(tablefmt='github')}")
    logger.info(f"\nTable LaTeX Code: \n{table.tabulate(tablefmt='latex')}")


if __name__ == '__main__':
    # with categorical
    make_balance_check_table(
        all_in_one_df_path=r"D:\dataset\smart\original_data\all_in_one.xlsx",
        columns = ['Nnindnme', 'Markettype', 'OWNERSHIPTYPE', 'A001000000', 'page_number', 'character_length',],
        categorical = ['Nnindnme', 'Markettype', 'OWNERSHIPTYPE',],
        result_path=r"./balance_check_result.xlsx.",
    )
    # w/o categorical
    make_balance_check_table(
        all_in_one_df_path=r"D:\dataset\smart\original_data\all_in_one.xlsx",
        columns=['A001000000', 'page_number', 'character_length', ],
        categorical = [],
        result_path=r"./balance_check_result.xlsx.",
    )

