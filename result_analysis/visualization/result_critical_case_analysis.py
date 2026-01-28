"""
关键样本筛选。
"""

from __future__ import annotations
from loguru import logger

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class CriticalCaseAnalysis:
    @staticmethod
    def make_critical_case_analysis(
        df: pd.DataFrame,
    ) -> go.Figure:
        # 1. 定义样本类型
        def classify_case(row):
            if row['label'] == row['has_risk']:
                return 'Correct'
            elif row['label'] == False and row['has_risk'] == True:
                return 'False Alarm (Type I)'
            else:
                return 'Missed Risk (Type II)'
        df['case_type'] = df.apply(classify_case, axis=1)
        # 2. 绘制交互式散点图
        # x轴用 id 或者 index，y轴用 confidence
        figure = px.scatter(
            df,
            x=df.index,
            y='confidence',
            color='case_type',
            symbol='case_type',
            hover_data=['id', 'label', 'has_risk'],
            color_discrete_map={
                'Correct': '#636EFA',
                'False Alarm (Type I)': '#EF553B',  # 红色警告
                'Missed Risk (Type II)': '#FFA15A',  # 橙色警告
            },
            title='Critical Case Analysis: Confidence vs Accuracy',
        )
        # 添加一条高置信度阈值线（例如 0.8 以上报错就很严重）
        figure.add_hline(y=0.8, line_dash="dot", annotation_text="High Confidence Zone",)
        figure.update_layout(
            xaxis_title='Sample Index',
            yaxis_title='System Confidence',
        )
        return figure

