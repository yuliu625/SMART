"""
各种MAS的工厂。

注意:
    为了可以直接执行，以及方便实验:
        - 策略模式: 完全以可序列化的方式构造。
        - 硬编码: 对实验无影响的参数直接使用了硬编码。
"""

from __future__ import annotations
from loguru import logger

# Graphs
from mas.graphs.graph_factory import GraphFactory
# Schemas  暂时不进行封装。
from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.schemas.final_mas_state import FinalMASState
# Structured Output  暂时不进行封装。
from mas.schemas.structured_output_format import (
    AdjudicatorDecision,
)
# LLM
from mas.models.local_llm_factory import LocalLLMFactory
# Prompts
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING, cast
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph


class MASFactory:
    @staticmethod
    def create_single_agent_mas_via_vllm(
        adjudicator_main_llm_base_url: str,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_base_url: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ) -> CompiledStateGraph:
        graph = GraphFactory.create_single_agent_mas_graph(
            adjudicator_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=adjudicator_main_llm_base_url,
                model_name=adjudicator_main_llm_model_name,
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            adjudicator_main_llm_system_message=cast(SystemMessage, PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
            ).format()),
            adjudicator_formatter_llm=LocalLLMFactory.create_openai_llm(
                base_url=adjudicator_formatter_llm_base_url,
                model_name=adjudicator_formatter_llm_model_name,
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            adjudicator_formatter_llm_system_message=cast(SystemMessage, PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
            ).format()),
            adjudicator_structured_output_format=AdjudicatorDecision,  # HARDCODED
        )
        return graph

    @staticmethod
    def create_single_agent_mas_via_ollama(
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ) -> CompiledStateGraph:
        graph = GraphFactory.create_single_agent_mas_graph(
            adjudicator_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_main_llm_model_name,
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_main_llm_system_message=cast(SystemMessage, PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
            ).format()),
            adjudicator_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_formatter_llm_model_name,
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_formatter_llm_system_message=cast(SystemMessage, PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
            ).format()),
            adjudicator_structured_output_format=AdjudicatorDecision,  # HARDCODED
        )
        return graph

    @staticmethod
    def create_sequential_mas_via_vllm(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_sequential_mas_via_ollama(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_multi_agent_debate_mas_via_vllm(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_multi_agent_debate_mas_via_ollama(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_final_mas_via_vllm(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_final_mas_via_ollama(

    ) -> CompiledStateGraph:
        raise NotImplementedError

