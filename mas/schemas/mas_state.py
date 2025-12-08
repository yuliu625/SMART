"""
整个MAS的graph的计算状态。
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.documents import Document
    from langchain_core.messages import AnyMessage


class MASState:
    ...

