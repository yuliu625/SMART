"""
测试Analyst。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.schemas.final_mas_state import FinalMASState
# from mas.models.local_llm_factory import LocalLLMFactory
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestAnalyst:
    ...

