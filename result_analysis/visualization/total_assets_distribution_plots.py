"""
构造总资产的分布图。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TotalAssetsDistributionPlots:
    @staticmethod
    def make_total_assets_distribution_plot(
        st_companies_total_assets_df: pd.DataFrame,
        matching_sample_total_assets_df: pd.DataFrame,
    ):
        figure = go.Figure()
        # Treatment Group
        figure.add_trace(go.Box(
            y=st_companies_total_assets_df['A001000000'],
            name='Treatment Group',
            marker_color='#636EFA',
            boxmean=True, # 显示平均值虚线
        ))
        # Control Group
        figure.add_trace(go.Box(
            y=matching_sample_total_assets_df['A001000000'],
            name='Control Group',
            marker_color='#EF553B',
            boxmean=True,
        ))
        figure.update_layout(
            title="Total Assets Distribution",
            yaxis_title="Total Assets",
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


