"""
Confusion Matrix Visualization.
"""

from __future__ import annotations
from loguru import logger

import plotly.graph_objects as go
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ConfusionMatrixPlots:
    @staticmethod
    def make_confusion_matrix_plot(
        final_df: pd.DataFrame,
    ) -> go.Figure:
        # 使用sklearn进行计算confusion matrix。
        confusion_matrix_result = confusion_matrix(
            final_df['label'],
            final_df['has_risk'],
        )
        figure = go.Figure(
            data=go.Heatmap(
                data=confusion_matrix_result,
                x=['Predicted False', 'Predicted True'],
                y=['Actual False', 'Actual True'],
                colorscale='Blues',
                text=confusion_matrix_result,
                texttemplate="%{text}",  # 直接在方格内显示数字
                showscale=False
            )
        )
        figure.update_layout(
            title='Confusion Matrix',
            width=500,
            height=500,
        )
        return figure

