"""
构建可以量化分析结果的方法。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.utils.read_data_from_raw_database import (
    read_processed_xlsx_from_csmar_trd_co,
)
from result_analysis.experiment_results_analysis.result_collector import ResultCollector

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class QuantativeResultsMaker:
    @staticmethod
    def make_true_label_df(
        st_companies_df: pd.DataFrame,
        matching_sample_df: pd.DataFrame,
    ) -> pd.DataFrame:
        pos_df = st_companies_df[['Stkcd']].copy()
        neg_df = matching_sample_df[['Stkcd']].copy()
        pos_df['label'] = True
        neg_df['label'] = False
        label_df = pd.concat([pos_df, neg_df], ignore_index=True,)
        return label_df

    @staticmethod
    def make_quantative_results_df(
        st_companies_path: str | Path,
        matching_sample_path: str | Path,
        target_dir: str | Path,
    ) -> pd.DataFrame:
        st_companies_df = read_processed_xlsx_from_csmar_trd_co(
            processed_csmar_trd_co_xlsx_file_path=st_companies_path,
        )
        matching_sample_df = read_processed_xlsx_from_csmar_trd_co(
            processed_csmar_trd_co_xlsx_file_path=matching_sample_path,
        )
        result_dict_list = ResultCollector.collect_decision_results(
            target_dir=target_dir,
        )
        result_df = pd.DataFrame(result_dict_list)
        label_df = QuantativeResultsMaker.make_true_label_df(
            st_companies_df=st_companies_df,
            matching_sample_df=matching_sample_df,
        )
        result_df = pd.merge(label_df, result_df, on='Stkcd', how='inner',)
        return result_df

    @staticmethod
    def make_and_save_quantative_results_df(
        st_companies_path: str | Path,
        matching_sample_path: str | Path,
        target_dir: str | Path,
        result_path: str | Path,
    ) -> pd.DataFrame:
        result_df = QuantativeResultsMaker.make_quantative_results_df(
            st_companies_path=st_companies_path,
            matching_sample_path=matching_sample_path,
            target_dir=target_dir,
        )
        result_df.to_xlsx(result_path, index=False)
        return result_df

