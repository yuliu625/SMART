"""
构造可视化平衡检验结果。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.visualization.love_plots import (
    LovePlots,
)

from tableone import TableOne
import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_love_plot(
    all_in_one_df_path: str | Path,
    all_companies_df_path: str | Path,
    result_path: str | Path,
):
    all_in_one_df = pd.read_excel(
        all_in_one_df_path,
        dtype=dict(Stkcd=str),
    )
    all_companies_df = pd.read_excel(
        all_companies_df_path,
        dtype=dict(Stkcd=str),
    )
    table_before = TableOne(
        all_companies_df,
        columns=['A001000000',],
        categorical=[],
        groupby='is_risk',
        pval=True, smd=True,
    )
    logger.debug(f"\ntable_before: \n{table_before.tabulate(tablefmt='github')}")
    table_after = TableOne(
        all_in_one_df,
        columns=['A001000000',],
        categorical=[],
        groupby='is_risk',
        pval=True, smd=True,
    )
    logger.debug(f"\ntable_after: \n{table_after.tabulate(tablefmt='github')}")
    LovePlots.make_love_plot(
        table_before=table_before,
        table_after=table_after,
    ).write_image(
        result_path,
        scale=2,
    )


if __name__ == '__main__':
    make_love_plot(
        all_in_one_df_path=r"D:\dataset\smart\original_data\all_in_one.xlsx",
        all_companies_df_path=r"D:\dataset\smart\original_data\all_data_all_in_one.xlsx",
        result_path="./love_plots.png",
    )

