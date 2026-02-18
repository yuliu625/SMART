"""
所有需要进行structured-output的数据类。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


# ==== RAG ====
## ==== Multi-Query Retriever ====
class RewrittenQueries(BaseModel):
    """
    重写后的查询。
    """
    queries: list[str] = Field(
        ...,
        min_length=3, max_length=5,  # 对于输出的数量进行限制。
        description="针对原始问题生成的不同角度的检索查询语句列表。",
    )


# ==== Analysis ====
## ==== Analyst ====
class AnalystRequest(BaseModel):
    """
    解析 Analyst 的决策意图。
    """
    agent_name: Literal[
        'investigator', 'rag',
    ] = Field(
        ...,
        description="rag: 仍需检索数据; investigator: 分析完毕提交最终结果。",
    )
    agent_message: str = Field(
        description="若是rag，仅填入关键词；若是investigator，填入完整分析报告。",
    )


# ==== Decision ====
## ==== Investigator ====
class InvestigatorRequest(BaseModel):
    """
    解析 Investigator 的决策意图。
    """
    agent_name: Literal[
        'analyst', 'adjudicator',
    ] = Field(
        ...,
        description="analyst: 要求Analyst进行调查; adjudicator: 完成全部的调查提交最终结果。",
    )
    agent_message: str = Field(
        description="若是analyst，填入要进行调查和分析的内容；若是adjudicator，提交完整的总结。",
    )
## ==== Adjudicator ====
class AdjudicatorDecision(BaseModel):
    """
    解析 Adjudicator 的最终决策结果。
    """
    has_risk: bool = Field(
        ...,
        description="目标公司是否存在风险的判断。",
    )
    decision: str = Field(
        description="最终决策的简短总结文本。",
    )
    confidence: float = Field(
        ...,
        ge=0.0, le=1.0,
        description="对于结论的置信度。",
    )

