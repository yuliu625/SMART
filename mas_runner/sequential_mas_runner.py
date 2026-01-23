"""
sequential workflow的自动运行。
"""

from __future__ import annotations
from loguru import logger

from mas.mas_factory import MASFactory
from mas.rag_factory import RagFactory
from mas.io_methods import IOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
