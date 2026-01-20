"""
各种MAS的工厂。

完全以可序列化的方式构造，可直接执行。
"""

from __future__ import annotations
from loguru import logger

# Graphs
from mas.graphs.graph_factory import GraphFactory
# LLM
from mas.models.local_llm_factory import LocalLLMFactory
# Prompts
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph


class MASFactory:
    @staticmethod
    def create_single_agent_mas(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_sequential_mas(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_multi_agent_debate_mas(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_final_mas(

    ) -> CompiledStateGraph:
        raise NotImplementedError

