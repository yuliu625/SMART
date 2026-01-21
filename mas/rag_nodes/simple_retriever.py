"""
最基础的retriever。

该实现根据当前MAS的需要重写了process_state方法。
"""

from __future__ import annotations
from loguru import logger

from rag.langgraph_retrievers.simple_retriever import SimpleRetriever

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
