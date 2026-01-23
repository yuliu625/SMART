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
    用于存储重写后的查询语句的数据类。
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
    Analyst下一步的决定。
    """
    agent_name: Literal[
        'investigator', 'rag',
    ] = Field(
        ...,
        description="指定下一个运行的agent的名字。investigator 代表完成分析。rag 代表需要去查询更多的信息。",
    )
    agent_message: str = Field(
        description="传递给下一个的agent的信息。当 agent_name==investigator 时代表最终的分析结论总结。当 agent_name==rag 时代表具体需要执行的查询。",
    )


# ==== Decision ====
## ==== Investigator ====
class InvestigatorRequest(BaseModel):
    """
    Investigator下一步的决定。
    """
    agent_name: Literal[
        'analyst', 'adjudicator',
    ] = Field(
        ...,
        description="指定下一个运行的agent的名字。analyst 代表要求Analyst进行调查。adjudicator 表示已经完成全部的调查。",
    )
    agent_message: str = Field(
        description="Investigator要求Analyst进行调查和分析的内容。",
    )
## ==== Adjudicator ====
class AdjudicatorDecision(BaseModel):
    """
    文本中需求提取的决策结果。
    """
    has_risk: bool = Field(
        ...,
        description="是否存在风险的判断。",
    )
    decision: str = Field(
        description="最终决策的简短总结文本。",
    )
    confidence: float = Field(
        ...,
        ge=0.0, le=1.0,
        description="对于结论的置信度。",
    )

