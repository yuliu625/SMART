"""
置信度分布图。
"""

from __future__ import annotations
from loguru import logger

import plotly.graph_objects as go
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ConfidenceDistributionPlots:
    @staticmethod
    def make_confidence_distribution_plot(
        df: pd.DataFrame,
    ) -> go.Figure:
        # 标记预测是否正确
        df['is_correct'] = (df['label'] == df['has_risk']).map(
            {True: 'Correct', False: 'Incorrect'}
        )

        figure = go.Figure()
        for res in ['Correct', 'Incorrect']:
            figure.add_trace(
                go.Violin(
                    y=df[df['is_correct'] == res]['confidence'],
                    name=res,
                    box_visible=True,
                    meanline_visible=True,
                )
            )
        figure.update_layout(
            title='Confidence Distribution: Correct vs Incorrect',
            yaxis_title='Confidence Score',
            xaxis_title='Prediction Result',
            legend=dict(
                orientation="h",  # 水平排列
                yanchor="bottom",
                y=1.02,  # 放在绘图区上方（1.0是顶端）
                xanchor="right",
                x=1  # 对齐到右侧
            ),
            margin=dict(t=100)
        )
        return figure

