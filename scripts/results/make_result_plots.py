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



def main():
    ...


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main()
    ...

