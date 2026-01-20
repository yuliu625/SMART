"""
对于当前MAS的IO方法。

针对mas.schemas中的定义。
"""

from __future__ import annotations
from loguru import logger

from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.schemas.final_mas_state import FinalMASState

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class IOMethods:
    @staticmethod
    def load_single_agent_mas_state(

    ) -> SingleAgentMASState:
        ...

    @staticmethod
    def save_single_agent_mas_state(

    ) -> SingleAgentMASState:
        ...

    @staticmethod
    def load_sequential_mas_state(

    ) -> SequentialMASState:
        raise NotImplementedError

    @staticmethod
    def save_sequential_mas_state(

    ) -> SequentialMASState:
        raise NotImplementedError

    @staticmethod
    def load_final_mas_state(

    ) -> FinalMASState:
        raise NotImplementedError

    @staticmethod
    def save_final_mas_state(

    ) -> FinalMASState:
        raise NotImplementedError

