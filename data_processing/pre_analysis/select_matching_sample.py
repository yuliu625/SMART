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
    # 复制一份候选池，避免修改原始 DataFrame
    pool = df_not_st_with_total_assets.copy()

    for _, st in df_st_with_total_assets.iterrows():
        # 如果候选池已经空了，跳出循环
        if pool.empty:
            break

        # 尝试 1: 严格匹配同行业
        candidates = pool[pool['Nnindcd'] == st['Nnindcd']]

        # 尝试 2: 行业大类
        if candidates.empty:
            st_category = str(st['Nnindcd'])[:2]
            candidates = pool[pool['Nnindcd'].astype(str).str.startswith(st_category)]

        # 尝试 3: 全市场
        if candidates.empty:
            candidates = pool

        # 寻找资产规模最接近的一家
        idx = (candidates['A001000000'] - st['A001000000']).abs().idxmin()
        best_match = pool.loc[idx] # 注意这里直接从 pool 取，确保索引一致

        # 将结果存入列表
        matched_list.append({
            'ST_Stkcd': st['Stkcd'],
            'ST_Name': st['Stknme'],
            'ST_Assets': st['A001000000'],
            'Control_Stkcd': best_match['Stkcd'],
            'Control_Name': best_match['Stknme'],
            'Control_Assets': best_match['A001000000'],
            'Match_Quality': 'Industry' if st['Nnindcd'] == best_match['Nnindcd'] else 'Category',
        })

        # 关键步骤: 从 pool 中剔除已选中的样本。
        pool = pool.drop(idx)
    df_matched = pd.DataFrame(matched_list)
    df_sample = pd.merge(
        df_not_st_with_total_assets, df_matched['Control_Stkcd'],
        left_on='Stkcd', right_on='Control_Stkcd'
    ).drop(columns='Control_Stkcd')
    return df_sample

