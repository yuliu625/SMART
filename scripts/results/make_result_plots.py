"""
构造实验结果的图像。
"""

from __future__ import annotations
from loguru import logger

from result_analysis.experiment_results_analysis.quantative_results_maker import (
    QuantativeResultsMaker,
)
from result_analysis.visualization.result_confusion_matrix_plots import (
    ConfusionMatrixPlots,
)
from result_analysis.visualization.result_confidence_distribution_plots import (
    ConfidenceDistributionPlots,
)
from result_analysis.visualization.result_precision_recall_curve import (
    PrecisionRecallCurvePlots,
)
from result_analysis.visualization.result_reliability_diagram import (
    ReliabilityDiagram,
)
from result_analysis.visualization.result_critical_case_analysis import (
    CriticalCaseAnalysis,
)

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    st_companies_path: str | Path,
    matching_sample_path: str | Path,
    target_dir: str | Path,
    result_dir: str | Path,
):
    target_dir = Path(target_dir)
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    df = QuantativeResultsMaker.make_quantative_results_df(
        st_companies_path=st_companies_path,
        matching_sample_path=matching_sample_path,
        target_dir=target_dir,
    )
    ConfusionMatrixPlots.make_confusion_matrix_plot(
        df=df.copy(),
    ).write_image(
        f"{result_dir}/confusion_matrix.png",
        scale=2,
    )
    logger.success(f"Saved Confusion Matrix.")
    ConfidenceDistributionPlots.make_confidence_distribution_plot(
        df=df.copy(),
    ).write_image(
        f"{result_dir}/confidence_distribution.png",
        scale=2,
    )
    logger.success(f"Saved Confidence Distribution.")
    PrecisionRecallCurvePlots.make_precision_recall_curve_plot(
        df=df.copy(),
    ).write_image(
        f"{result_dir}/precision_recall_curve.png",
        scale=2,
    )
    logger.success(f"Saved Precision Recall Curve.")
    ReliabilityDiagram.make_reliability_diagram(
        df=df.copy(),
    ).write_image(
        f"{result_dir}/reliability_diagram.png",
        scale=2,
    )
    logger.success(f"Saved Reliability Diagram.")
    CriticalCaseAnalysis.make_critical_case_analysis(
        df=df.copy(),
    ).write_image(
        f"{result_dir}/critical_case_analysis.png",
        scale=2,
    )
    logger.success(f"Saved Critical Case Analysis.")


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main(
        st_companies_path=st_companies_path_,
        matching_sample_path=matching_sample_path_,
        target_dir=r"D:\dataset\smart\experimental_results\qwen_25_7b_instruct\markdown_1\docling_1",
        result_dir=r"./",
    )

