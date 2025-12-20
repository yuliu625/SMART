"""
所有需要进行structured-output的数据类。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import Literal


# ====RAG====
class RAGRewriteResponse(BaseModel):
    items: list[str] = Field(
        description="multi-query-RAG中，进行query重写的agent生成的结果。",
        min_length=3, max_length=5,
    )


# ====analysis & decision====
class AnalystRequest(BaseModel):
    agent_name: Literal[
        'arbiter', 'analyst',
    ] = Field(
        description="指定下一个运行的agent的名字。"
    )
    agent_message: str = Field(
        description="传递给下一个的agent的信息。"
    )


class InvestigatorRequest(BaseModel):
    agent_name: Literal[
        'investigator',
    ]


# ====decision====
class ArbiterDecision(BaseModel):
    decision: str = Field(
        description="最终的决定。"
    )
    risk: bool = Field(
        description="是否存在风险的判断。"
    )
    confidence: float = Field(
        description="对于仲裁结果的置信度。"
    )


class ConfidenceOutput(BaseModel):
    content: str
    confidence: float

