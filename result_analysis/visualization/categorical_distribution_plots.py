"""
构建行业分类的分布图。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class CategoricalDistributionPlots:
    @staticmethod
    def make_categorical_distribution_plot(
        st_companies_series: pd.Series,
        matching_sample_series: pd.Series,
    ):
        # 主图
        figure = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'domain'}, {'type': 'domain'}]],
            subplot_titles=['Treatment Group', 'Control Group'],
            horizontal_spacing=0.05,  # 2个子图水平间距。
        )
        # 子图1
        figure.append_trace(
            go.Pie(
                labels=st_companies_series.index,
                values=st_companies_series.values,
                name="Treatment Group",
                hole=0.4,  # 使用环形图，对比更清晰。
                textinfo='none',
                domain={'x': [0, 0.48], 'y': [0, 1]},
            ),
            row=1, col=1,
        )
        # 子图2
        figure.append_trace(
            go.Pie(
                labels=matching_sample_series.index,
                values=matching_sample_series.values,
                name="Control Group",
                hole=0.4,  # 使用环形图，对比更清晰。
                textinfo='none',
                domain={'x': [0.52, 1], 'y': [0, 1]},
            ),
            row=1, col=2,
        )
        # 布局优化
        figure.update_layout(
            showlegend=True,
            height=500,
            width=1000,
            legend=dict(
                font=dict(size=10),  # 缩小图例字体，防止图例过大
                orientation="v",
                yanchor="middle",  # 改为中间对齐
                y=0.5,
                xanchor="left",
                x=1.02,  # 紧贴右边界
                itemsizing='constant',  # 使图例图标保持固定大小
                traceorder="normal"
            ),
            margin=dict(t=80, b=20, l=20, r=150),
        )
        return figure

