"""

"""

from pydantic import BaseModel, Field
from typing import Literal


class RequestAgent(BaseModel):
    agent_name: Literal[
        'arbiter', 'validator',
        'document_reader',
        'control_analyst', 'financial_analyst', 'strategic_analyst',
    ] = Field(
        description="某个agent对于下一个请求的agent的名字。"
    )
    message: str = Field(description="某个agent对于下一个请求的agent的内容。")


class ArbiterDecision(BaseModel):
    decision: str = Field(description="最终的决定。")
    risk: bool = Field(description="是否存在风险的判断。")
    confidence: float = Field(description="对于仲裁结果的置信度。")


class ConfidenceOutput(BaseModel):
    content: str
    confidence: float

