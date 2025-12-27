"""
决策模块会使用的条件边。
"""

from __future__ import annotations

from mas.schemas.mas_state import MASState

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


def is_need_validation(
    state: MASState,
) -> bool:
    ...


def get_next_agent_name(
    state: MASState,
) -> Literal['investigator', 'analyst']:
    ...


