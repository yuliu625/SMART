"""
收集各种条件下的运行结果。

包含直接返回收集结果，以及直接完成序列化。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.experiment_results_analysis.quantative_results_maker import (
    QuantativeResultsMaker,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def collect_and_save_experiment_results(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    target_dir: str | Path,
    result_path: str | Path,
):
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=target_dir,
        result_path=result_path,
    )
    logger.success(f"Saved {result_path}")


def main(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
):
    # benchmark
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\benchmark",
        result_path=r"D:\dataset\smart\results\benchmark.xlsx",
    )
    # sequential workflow
    ## dense
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\sequential_workflow_simple_rag\dense",
        result_path=r"D:\dataset\smart\results\sequential_workflow_simple_rag_dense.xlsx",
    )
    ## sparse
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\sequential_workflow_simple_rag\sparse",
        result_path=r"D:\dataset\smart\results\sequential_workflow_simple_rag_sparse.xlsx",
    )
    ## multi-vector
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\sequential_workflow_simple_rag\multi_vector",
        result_path=r"D:\dataset\smart\results\sequential_workflow_simple_rag_multi_vector.xlsx",
    )
    ## hybrid
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\sequential_workflow_simple_rag\hybrid",
        result_path=r"D:\dataset\smart\results\sequential_workflow_simple_rag_hybrid.xlsx",
    )
    ## all
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\sequential_workflow_simple_rag\all",
        result_path=r"D:\dataset\smart\results\sequential_workflow_simple_rag_all.xlsx",
    )

    # mas
    ## simple rag & hybrid
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\mas_simple_rag\hybrid",
        result_path=r"D:\dataset\smart\results\mas_simple_rag_hybrid.xlsx",
    )
    ## simple rag & all
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\mas_simple_rag\all",
        result_path=r"D:\dataset\smart\results\mas_simple_rag_all.xlsx",
    )
    ## multi-query & hybrid
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\mas_multi_query_rag\hybrid",
        result_path=r"D:\dataset\smart\results\mas_multi_query_rag_hybrid.xlsx",
    )
    ## multi-query & all
    QuantativeResultsMaker.make_and_save_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=r"D:\dataset\smart\experiment_results\mas_multi_query_rag\all",
        result_path=r"D:\dataset\smart\results\mas_multi_query_rag_all.xlsx",
    )


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
    )

