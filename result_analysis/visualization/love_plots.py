"""
平衡性检验结果可视化。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
import plotly.graph_objects as go

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class LovePlots:
    @staticmethod
    def make_love_plot(
        table_before,
        table_after,
    ):
        def get_smd_series(t_obj):
            df = t_obj.tableone

            # 1. 定位 SMD 列
            target_col = None
            for col in df.columns:
                if isinstance(col, tuple) and len(col) > 1:
                    if "SMD" in str(col[1]).upper():
                        target_col = col
                        break
                elif "SMD" in str(col).upper():
                    target_col = col
                    break

            if target_col is None:
                raise ValueError("未找到 SMD 列。")

            # 2. 关键修复：处理空字符串
            # errors='coerce' 会把无法转换的字符串（如 ''）变成 NaN
            smd_values = pd.to_numeric(df[target_col], errors='coerce')

            # 3. 剔除空值并按变量名去重
            # tableone 的索引通常是 (变量名, 类别) 的 MultiIndex 或简单 Index
            # level=0 对应变量名
            return smd_values.dropna().groupby(level=0).first()

            # 提取数据，转为浮点数，并按变量名（第一级行索引）去重
            # tableone 结果中类别变量会重复显示 SMD，这里取每组变量的第一个即可
            series = df[target_col].astype(float)
            return series.groupby(level=0).first()

        smd_before = get_smd_series(table_before)
        smd_after = get_smd_series(table_after)

        # 合并数据用于绘图
        smd_data = pd.DataFrame(
            {
                'Variable': smd_before.index,
                'Before': smd_before.values,
                'After': smd_after.values
            }
        ).sort_values(by='Before', ascending=True)

        figure = go.Figure()
        # 添加匹配前的点
        figure.add_trace(
            go.Scatter(
                x=smd_data['Before'], y=smd_data['Variable'],
                mode='markers', name='Before Matching',
                marker=dict(color='red', size=10, symbol='circle')
            )
        )
        # 添加匹配后的点
        figure.add_trace(
            go.Scatter(
                x=smd_data['After'], y=smd_data['Variable'],
                mode='markers', name='After Matching',
                marker=dict(color='blue', size=10, symbol='square')
            )
        )
        # 添加 0.1 的参考线
        figure.add_vline(x=0.1, line_dash="dash", line_color="gray", annotation_text="Threshold (0.1)")
        figure.add_vline(x=0, line_color="black")
        # 布局美化
        figure.update_layout(
            title='Covariate Balance Check (Love Plot)',
            xaxis_title='Standardized Mean Difference (SMD)',
            yaxis_title='Variables',
            template='plotly_white',
            height=600,
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
            hovermode='closest',
        )
        return figure

