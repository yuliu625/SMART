"""
PR Curve.
"""

from __future__ import annotations
from loguru import logger

from sklearn.metrics import precision_recall_curve
import plotly.graph_objects as go
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class PrecisionRecallCurvePlots:
    @staticmethod
    def make_precision_recall_curve_plot(
        df: pd.DataFrame,
    ) -> go.Figure:
        # 基于has_risk=True计算概率。
        precision, recall, thresholds = precision_recall_curve(df['label'], df['confidence'])
        # 制图。
        figure = go.Figure()
        # 绘制 PR 曲线
        figure.add_trace(
            go.Scatter(
                x=recall, y=precision,
                mode='lines',
                fill='tozeroy',
                name='PR Curve',
            )
        )
        # 辅助线：随机模型表现
        figure.add_shape(
            type='line',
            line=dict(dash='dash'),
            x0=0,
            x1=1,
            y0=0.5,
            y1=0.5,
        )
        figure.update_layout(
            title='Precision-Recall Curve',
            xaxis_title='Recall',
            yaxis_title='Precision',
            xaxis=dict(range=[0, 1]),
            yaxis=dict(range=[0, 1.05]),
        )
        return figure

