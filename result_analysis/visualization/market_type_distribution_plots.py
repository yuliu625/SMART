"""
构建市场类型的分布图。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class MarketTypeDistributionPlots:
    @staticmethod
    def make_market_type_distribution_plot(
        st_companies_series: pd.Series,
        matching_sample_series: pd.Series,
    ):
        # CSMAR的定义。
        market_mapping = {
            '1': "上证A股 (不含科创板)",
            '2': "上证B股",
            '4': "深证A股 (不含创业板)",
            '8': "深证B股",
            '16': "创业板",
            '32': "科创板",
            '64': "北证A股"
        }
        # legend展示优化
        # st_labels = st_companies_series.index.map(market_mapping)
        # matching_labels = matching_sample_series.index.map(market_mapping)
        # 颜色
        # color_palette = px.colors.qualitative.Pastel
        # all_labels = list(market_mapping.values())
        # color_map = {label: color_palette[i % len(color_palette)] for i, label in enumerate(all_labels)}
        # st_colors = [color_map[label] for label in st_labels]
        # matching_colors = [color_map[label] for label in matching_labels]
        def preprocess_series(s, mapping):
            # 将数字索引换成中文
            s.index = s.index.map(mapping)
            # 这一步极其重要：确保即使某组数据里没有“科创板”，也会补个 0，保证两图维度完全一致
            all_categories = list(mapping.values())
            return s.reindex(all_categories).fillna(0)

        st_companies_series = preprocess_series(st_companies_series, market_mapping)
        matching_sample_series = preprocess_series(matching_sample_series, market_mapping)
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
                # labels=st_labels,
                values=st_companies_series.values,
                name="Treatment Group",
                hole=0.4,  # 使用环形图，对比更清晰。
                # marker=dict(colors=st_colors),
                textinfo='none',
                domain={'x': [0, 0.48], 'y': [0, 1]},
            ),
            row=1, col=1,
        )
        # 子图2
        figure.append_trace(
            go.Pie(
                labels=matching_sample_series.index,
                # labels=matching_labels,
                values=matching_sample_series.values,
                name="Control Group",
                hole=0.4,  # 使用环形图，对比更清晰。
                # marker=dict(colors=matching_colors),
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

