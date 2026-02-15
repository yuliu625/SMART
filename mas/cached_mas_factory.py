"""
各种MAS的工厂。

注意:
    为了可以直接执行，以及方便实验:
        - 策略模式: 完全以可序列化的方式构造。
        - 硬编码: 对实验无影响的参数直接使用了硬编码。

优化:
    - 缓存: 构建需要配套的:
        - cached graph
        - cached io methods
        配合运行。
    - OpenAI API: 默认使用 openai 协议，兼容问题通过 gateway 工具解决。
"""

from __future__ import annotations
from loguru import logger

# Graphs
from mas.graphs.cached_graph_factory import CachedGraphFactory
# Schemas  暂时不进行封装。
from mas.schemas.single_agent_state import SingleAgentState
from mas.schemas.sequential_workflow_state import SequentialWorkflowState
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


class CachedMASFactory:
    @staticmethod
    def create_cached_single_agent(
        adjudicator_main_llm_base_url: str,
        adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        adjudicator_formatter_llm_base_url: str,
        adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
    ) -> CompiledStateGraph:
        raise NotImplementedError("以外部方法独立实现 benchmark 。")
        graph = CachedGraphFactory.create_cached_single_agent_graph(
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
    def create_cached_sequential_workflow(
        llm_base_url: str,
        # Surveyor
        # surveyor_main_llm_base_url: str,
        # surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Investigator
        # Adjudicator
        # adjudicator_main_llm_base_url: str,
        # adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        # adjudicator_formatter_llm_base_url: str,
        # adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph = CachedGraphFactory.create_cached_sequential_workflow_graph(
            # Surveyor
            surveyor_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='surveyor-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            surveyor_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=surveyor_main_llm_system_message_template_path,
                ).format(),
            ),
            # Adjudicator
            adjudicator_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='adjudicator-llm',
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
                base_url=llm_base_url,
                # HARDCODED
                model_name='formatter-llm',
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
            # RAG
            rag=rag,
        )
        return graph

    @staticmethod
    def create_cached_final_mas(
        llm_base_url: str,
        # Surveyor
        # surveyor_main_llm_base_url: str,
        # surveyor_main_llm_model_name: str,
        surveyor_main_llm_system_message_template_path: str,
        # Investigator
        # investigator_main_llm_base_url: str,
        # investigator_main_llm_model_name: str,
        investigator_main_llm_system_message_template_path: str,
        # investigator_formatter_llm_base_url: str,
        # investigator_formatter_llm_model_name: str,
        investigator_formatter_llm_system_message_template_path: str,
        # Adjudicator
        # adjudicator_main_llm_base_url: str,
        # adjudicator_main_llm_model_name: str,
        adjudicator_main_llm_system_message_template_path: str,
        # adjudicator_formatter_llm_base_url: str,
        # adjudicator_formatter_llm_model_name: str,
        adjudicator_formatter_llm_system_message_template_path: str,
        # Analyst
        # analyst_main_llm_base_url: str,
        # analyst_main_llm_model_name: str,
        analyst_main_llm_system_message_template_path: str,
        # analyst_formatter_llm_base_url: str,
        # analyst_formatter_llm_model_name: str,
        analyst_formatter_llm_system_message_template_path: str,
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph = CachedGraphFactory.create_cached_final_mas_graph(
            # Surveyor
            surveyor_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='surveyor-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            surveyor_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=surveyor_main_llm_system_message_template_path,
                ).format(),
            ),
            # Investigator
            investigator_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='investigator-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            investigator_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=investigator_main_llm_system_message_template_path,
                ).format(),
            ),
            investigator_formatter_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='formatter-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
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
            adjudicator_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='adjudicator-llm',
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
                base_url=llm_base_url,
                # HARDCODED
                model_name='formatter-llm',
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
            # Analyst
            analyst_main_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='analyst-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
                model_configs={},
            ),
            analyst_main_llm_system_message=cast(
                SystemMessage,
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=analyst_main_llm_system_message_template_path,
                ).format(),
            ),
            analyst_formatter_llm=LocalLLMFactory.create_openai_llm(
                base_url=llm_base_url,
                # HARDCODED
                model_name='formatter-llm',
                # HARDCODED
                temperature=None,
                max_tokens=None,
                logprobs=None,
                use_responses_api=None,
                max_retries=None,
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

