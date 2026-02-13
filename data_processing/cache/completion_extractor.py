"""
从原始响应中提取目标结果的方法。
"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING, Mapping
# if TYPE_CHECKING:


class CompletionExtractor:
    @staticmethod
    def extract_content(
        completion: Mapping,
    ) -> str:
        ...

