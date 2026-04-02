"""
multi-agent debate 下专用的 condition edges 。

独立设置这些条件是因为 decision module 和 analysis module 在这种 design pattern下是混合的。
"""

from __future__ import annotations
from loguru import logger

from mas.schemas.multi_agent_debate_state import MultiAgentDebateState

from typing import TYPE_CHECKING, Literal, cast
# if TYPE_CHECKING:


# ==== for proponent ====
def is_need_transfer_to_opponent(
    state: MultiAgentDebateState,
) -> Literal['adjudicator', 'opponent']:
    raise NotImplementedError


# ==== for opponent ====
def is_need_transfer_to_proponent(
    state: MultiAgentDebateState,
) -> Literal['adjudicator', 'proponent']:
    raise NotImplementedError

