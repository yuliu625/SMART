"""
计算混淆矩阵的结果。
"""

from __future__ import annotations
from loguru import logger

from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def calculate_confusion_matrix(
    final_df: pd.DataFrame,
):
    confusion_matrix_result = confusion_matrix(
        final_df['label'],
        final_df['has_risk'],
    )
    return confusion_matrix_result

