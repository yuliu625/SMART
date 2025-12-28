"""
RAG子图使用的state。

RAG系统会有多种架构和实现方法需要测试，具体的有:
    - SimpleRAG
    - MultiQueryRAG
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.documents import Document
    from langchain_core.messages import AnyMessage


class SimpleRAGState(BaseModel):
    query: str = Field(
        description="查询的内容。",
    )
    results: list[Document] = Field(
        description="查询的结果。",
    )


class MultiQueryRAGState(BaseModel):
    query: str = Field(
        description="查询的内容。",
    )
    results: list[Document] = Field(
        description="查询的结果。",
    )


class MultiQueryRAGWithMemoryState(BaseModel):
    query: str = Field(
        description="查询的内容。",
    )
    result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    results: list[Document] = Field(
        description="查询的结果。",
    )

