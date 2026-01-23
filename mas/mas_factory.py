"""
各种MAS的工厂。

注意:
    为了可以直接执行，以及方便实验:
        - 策略模式: 完全以可序列化的方式构造。
        - 硬编码: 对实验无影响的参数直接使用了硬编码。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.decision_agents.investigator import Investigator
# Graphs
from mas.graphs.graph_factory import GraphFactory
# Schemas  暂时不进行封装。
from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.schemas.final_mas_state import FinalMASState
# Structured Output  暂时不进行封装。
from mas.schemas.structured_output_format import (
    # Decision
    InvestigatorRequest,
    ## Final Result
    AdjudicatorDecision,
    # Analysis
    AnalystRequest,
    # RAG
    RewrittenQueries,
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
            adjudicator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
                ).format(),
            ),
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
            adjudicator_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            adjudicator_structured_output_format=AdjudicatorDecision,
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
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
                ).format(),
            ),
            adjudicator_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_formatter_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            adjudicator_structured_output_format=AdjudicatorDecision,
        )
        return graph

    @staticmethod
    def create_sequential_mas_via_vllm(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_sequential_mas_via_ollama(
        # Surveyor
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Adjudicator
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        # RAG
        rag,
    ) -> CompiledStateGraph:
        mas = GraphFactory.create_sequential_mas_graph(
            # Surveyor
            surveyor_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=surveyor_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            surveyor_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=surveyor_main_llm_system_message_template_path,
                ).format(),
            ),
            # Adjudicator
            adjudicator_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
                ).format(),
            ),
            adjudicator_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_formatter_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            adjudicator_structured_output_format=AdjudicatorDecision,
            # RAG
            rag=rag,
        )
        return mas

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
        # Surveyor
        surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Investigator
        investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        # Adjudicator
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph = GraphFactory.create_final_mas_graph(
            # Surveyor
            surveyor_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=surveyor_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            surveyor_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=surveyor_main_llm_system_message_template_path,
                ).format(),
            ),
            # Investigator
            investigator_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=investigator_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            investigator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=investigator_main_llm_system_message_template_path,
                ).format(),
            ),
            investigator_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=investigator_formatter_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            investigator_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=investigator_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            investigator_structured_output_format=InvestigatorRequest,
            # Adjudicator
            adjudicator_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_main_llm_system_message_template_path,
                ).format(),
            ),
            adjudicator_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=adjudicator_formatter_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            adjudicator_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=adjudicator_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            adjudicator_structured_output_format=AdjudicatorDecision,
            # Analyst
            analyst_main_llm=LocalLLMFactory.create_ollama_llm(
                model_name=analyst_main_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            analyst_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=analyst_main_llm_system_message_template_path,
                ).format(),
            ),
            analyst_formatter_llm=LocalLLMFactory.create_ollama_llm(
                model_name=analyst_formatter_llm_model_name,
                # HARDCODED
                reasoning=None,
                temperature=0.7,
                num_predict=None,
                model_configs={},
            ),
            analyst_formatter_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=analyst_formatter_llm_system_message_template_path,
                ).format(),
            ),
            # HARDCODED
            analyst_structured_output_format=AnalystRequest,
            # RAG
            rag=rag,
        )
        return graph

