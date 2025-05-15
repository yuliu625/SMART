"""

"""

from pydantic import BaseModel, Field


class RequestAgent(BaseModel):
    agent_name: str = Field(description="某个agent对于下一个请求的agent的名字。")
    message: str = Field(description="某个agent对于下一个请求的agent的内容。")


class ConfidenceOutput(BaseModel):
    content: str
    confidence: float

