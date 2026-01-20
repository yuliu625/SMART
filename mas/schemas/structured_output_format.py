"""
所有需要进行structured-output的数据类。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


# ====RAG====
class RAGRewriteResponse(BaseModel):
    """

    """
    queries: list[str] = Field(
        description="将原始query进行重写后的多个query。",
        min_length=3, max_length=5,  # 对于输出的数量进行限制。
    )


# ==== Analysis ====
class AnalystRequest(BaseModel):
    """

    """
    agent_name: Literal[
        'investigator', 'rag',
    ] = Field(
        description="指定下一个运行的agent的名字。",
    )
    agent_message: str = Field(
        description="传递给下一个的agent的信息。",
    )


# ==== Decision ====
## ==== Investigator ====
class InvestigatorRequest(BaseModel):
    agent_name: Literal[
        'investigator',
    ]
## ==== Adjudicator ====
class AdjudicatorDecision(BaseModel):
    """
    文本中需求提取的决策结果。
    """
    decision: str = Field(
        description="最终决策的简短总结文本。"
    )
    has_risk: bool = Field(
        description="是否存在风险的判断。"
    )
    confidence: float = Field(
        description="对于结论的置信度。"
    )


# confidence
class ConfidenceOutput(BaseModel):
    content: str
    confidence: float

