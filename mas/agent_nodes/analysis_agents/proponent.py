"""
支持方，预设正标签。

multi-agent debate 中的 agent 因 ablation study ，不与 investigator 进行交互。
"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
