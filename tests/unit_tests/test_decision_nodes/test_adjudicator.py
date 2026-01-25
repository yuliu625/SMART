"""
测试adjudicator。

该测试几乎等同integration tests中的single agent test。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
from mas.schemas.final_mas_state import FinalMASState
from mas.schemas.sequential_workflow_state import SequentialWorkflowState
from mas.schemas.single_agent_state import SingleAgentState
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestAdjudicator:
    ...

