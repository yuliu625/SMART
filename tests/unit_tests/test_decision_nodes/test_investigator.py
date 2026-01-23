"""
测试investigator。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.schemas.final_mas_state import FinalMASState
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestInvestigator:
    ...

