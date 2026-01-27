"""
PDF文件页数的分布图。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class PageNumberDistributionPlots:
    @staticmethod
    def make_page_number_distribution_plot(
        st_companies_df: pd.DataFrame,
        matching_sample_df: pd.DataFrame,
    ):
        figure = go.Figure()
        # Treatment Group
        figure.add_trace(go.Box(
            y=st_companies_df['page_number'],
            name='Treatment Group',
            marker_color='#636EFA',
            boxmean=True, # 显示平均值虚线
        ))
        # Control Group
        figure.add_trace(go.Box(
            y=matching_sample_df['page_number'],
            name='Control Group',
            marker_color='#EF553B',
            boxmean=True,
        ))
        figure.update_layout(
            title="PDF Page Number Distribution",
            yaxis_title="Page Number",
            template="plotly_white",
            legend=dict(
                orientation="h",  # 设置为水平排列
                yanchor="bottom",  # 锚点在底部
                y=1.02,  # 放在绘图区上方（1.0代表绘图区顶端）
                xanchor="right",  # 锚点在右侧
                x=1  # 与绘图区右侧对齐
            )
        )
        return figure

