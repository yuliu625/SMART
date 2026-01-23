"""
测试adjudicator。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
from mas.schemas.final_mas_state import FinalMASState
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestAdjudicator:
    ...

