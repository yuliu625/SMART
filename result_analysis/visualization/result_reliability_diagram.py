"""
可靠性校准图。
"""

from __future__ import annotations
from loguru import logger

import plotly.graph_objects as go
from sklearn.calibration import calibration_curve
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ReliabilityDiagram:
    @staticmethod
    def make_reliability_diagram(
        df: pd.DataFrame,
    ) -> go.Figure:
        # 计算校准曲线
        # pos_label=True 表示我们关注有风险的校准情况
        prob_true, prob_pred = calibration_curve(df['label'], df['confidence'], n_bins=10)
        # 制图。
        figure = go.Figure()
        # 绘制校准曲线
        figure.add_trace(
            go.Scatter(
                x=prob_pred, y=prob_true,
                mode='lines+markers',
                name='Model Calibration',
            ),
        )
        # 绘制完美校准线 (y=x)
        figure.add_trace(
            go.Scatter(
                x=[0, 1], y=[0, 1],
                mode='lines',
                line=dict(dash='dash', color='gray'),
                name='Perfectly Calibrated',
            ),
        )
        figure.update_layout(
            title='Reliability Diagram (Calibration Curve)',
            xaxis_title='Mean Predicted Confidence',
            yaxis_title='Fraction of Positives (Actual Risk)',
            width=700, height=500,
            legend=dict(
                orientation="h",  # 水平排列
                yanchor="bottom",
                y=1.02,  # 放在绘图区上方（1.0是顶端）
                xanchor="right",
                x=1  # 对齐到右侧
            ),
            margin=dict(t=100),
        )
        return figure

