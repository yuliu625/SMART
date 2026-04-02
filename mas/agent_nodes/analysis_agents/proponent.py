"""
支持方，预设正标签。

multi-agent debate 中的 agent 因 ablation study ，不与 investigator 进行交互。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator
from mas.utils.document_merger import DocumentMerger

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING, Literal, cast
if TYPE_CHECKING:
    from mas.schemas.final_mas_state import FinalMASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from langchain_core.documents import Document
    from pydantic import BaseModel


class Proponent(BaseAgent):
    raise NotImplementedError

