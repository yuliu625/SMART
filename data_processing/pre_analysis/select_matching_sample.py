"""
选择配对样本的方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def merge_companies_and_total_assets(
    df_companies: pd.DataFrame,
    df_total_assets: pd.DataFrame,
) -> pd.DataFrame:
    df_ = pd.merge(df_companies, df_total_assets[['Stkcd', 'A001000000']], on='Stkcd')
    logger.trace("Merged companies and total assets df: \n", df_)
    return df_


def select_matching_sample_by_total_assets(
    df_st_with_total_assets: pd.DataFrame,
    df_not_st_with_total_assets: pd.DataFrame,
) -> pd.DataFrame:
    matched_list = []
    for _, st in df_st_with_total_assets.iterrows():
        # 尝试 1: 严格匹配同行业
        candidates = df_not_st_with_total_assets[df_not_st_with_total_assets['Nnindcd'] == st['Nnindcd']]

        # 尝试 2: 如果同行业没找到，匹配行业大类 (取代码前两位)
        if candidates.empty:
            st_category = str(st['Nnindcd'])[:2]
            candidates = df_not_st_with_total_assets[df_not_st_with_total_assets['Nnindcd'].str.startswith(st_category, na=False)]

        # 尝试 3: 如果还是没找到（极端情况），在全市场找规模最接近的
        if candidates.empty:
            candidates = df_not_st_with_total_assets

        # 在候选池中寻找资产规模最接近的一家
        # 注意：使用 .abs() 找到差值绝对值最小的索引
        idx = (candidates['A001000000'] - st['A001000000']).abs().idxmin()
        best_match = candidates.loc[idx]

        # 将结果存入列表
        matched_list.append(
            {
                'ST_Stkcd': st['Stkcd'],
                'ST_Name': st['Stknme'],
                'ST_Assets': st['A001000000'],
                'Control_Stkcd': best_match['Stkcd'],
                'Control_Name': best_match['Stknme'],
                'Control_Assets': best_match['A001000000'],
                'Match_Quality': 'Industry' if st['Nnindcd'] == best_match['Nnindcd'] else 'Category',
            }
        )
    df_matched = pd.DataFrame(matched_list)
    df_sample = pd.merge(
        df_not_st_with_total_assets, df_matched['Control_Stkcd'],
        left_on='Stkcd', right_on='Control_Stkcd'
    ).drop(columns='Control_Stkcd')
    return df_sample

