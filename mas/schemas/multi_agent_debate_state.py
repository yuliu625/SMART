"""
for multi-agent debate graph state.
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class MultiAgentDebateState(BaseModel):
    raise NotImplementedError

