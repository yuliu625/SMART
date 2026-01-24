"""
构造rag的工厂。

配合mas_factory使用。

避免繁琐设置，这里直接约定用LLM时，仅使用vllm。
"""

from __future__ import annotations
from loguru import logger

# RAG
from mas.rag_nodes.chroma_rag_builder import ChromaRAGBuilder
# 依赖MAS相关工具
from mas.models.local_llm_factory import LocalLLMFactory
from mas.prompts.prompt_template_loader import PromptTemplateLoader
# MAS需要的定义
from mas.schemas.structured_output_format import RewrittenQueries

from pathlib import Path

from typing import TYPE_CHECKING, cast
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage


class RAGFactory:
    @staticmethod
    def create_simple_rag_via_ollama(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        # Retriever
        search_configs: dict,
    ):
        # 传递参数。默认部分不常用参数。
        rag = ChromaRAGBuilder.build_simple_rag_via_ollama(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name=embedding_model_model_name,
            embedding_model_num_ctx=embedding_model_num_ctx,
            # HARDCODED
            embedding_model_repeat_penalty=None,
            embedding_model_temperature=None,
            embedding_model_stop_tokens=None,
            embedding_model_top_k=None,
            embedding_model_top_p=None,

            search_configs=search_configs,
        )
        return rag

    @staticmethod
    def create_simple_rag_via_huggingface(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        embedding_model_is_multi_process: bool,
        embedding_model_cache_folder: str | None,
        embedding_model_is_show_progress: bool,
        # Retriever
        search_configs: dict,
    ):
        # 仅传递参数。
        rag = ChromaRAGBuilder.build_simple_rag_via_huggingface(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name_or_path=embedding_model_model_name_or_path,
            embedding_model_model_kwargs=embedding_model_model_kwargs,
            embedding_model_encode_kwargs=embedding_model_encode_kwargs,
            embedding_model_query_encode_kwargs=embedding_model_query_encode_kwargs,
            embedding_model_is_multi_process=embedding_model_is_multi_process,
            embedding_model_cache_folder=embedding_model_cache_folder,
            embedding_model_is_show_progress=embedding_model_is_show_progress,
            search_configs=search_configs,
        )
        return rag

    @staticmethod
    def create_multi_query_rag_via_ollama(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        # Retriever
        search_configs: dict,
        # LLM
        llm_base_url: str,
        llm_model_name: str,
        llm_system_message_template_path: str,
        # structured_output_format: type[BaseModel],
    ):
        structured_llm = LocalLLMFactory.create_openai_llm(
            base_url=llm_base_url,
            model_name=llm_model_name,
            # HARDCODED
            temperature=None,
            max_tokens=None,
            logprobs=None,
            use_responses_api=None,
            max_retries=None,
            model_configs={},
        ).with_structured_output(
            # HARDCODED
            schema=RewrittenQueries,
        ).with_retry(
            # HARDCODED
            stop_after_attempt=3,
        )
        rag = ChromaRAGBuilder.build_multi_query_rag_via_ollama(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name=embedding_model_model_name,
            embedding_model_num_ctx=embedding_model_num_ctx,
            # HARDCODED
            embedding_model_repeat_penalty=None,
            embedding_model_temperature=None,
            embedding_model_stop_tokens=None,
            embedding_model_top_k=None,
            embedding_model_top_p=None,

            search_configs=search_configs,
            # LLM
            structured_llm=cast(
                'BaseChatModel',
                structured_llm,
            ),
            structured_llm_system_message=cast(
                'SystemMessage',
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=llm_system_message_template_path,
                ).format(),
            ),
        )
        return rag

    # ==== 本地测试使用。 ====
    @staticmethod
    def create_multi_query_rag_via_ollama_base_on_ollama_llm(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name: str,
        embedding_model_num_ctx: int | None,
        # Retriever
        search_configs: dict,
        # LLM
        llm_model_name: str,
        llm_system_message_template_path: str,
        # structured_output_format: type[BaseModel],
    ):
        structured_llm = LocalLLMFactory.create_ollama_llm(
            model_name=llm_model_name,
            # HARDCODED
            reasoning=None,
            temperature=0.7,
            num_predict=None,
            model_configs={},
        ).with_structured_output(
            # HARDCODED
            schema=RewrittenQueries,
        ).with_retry(
            # HARDCODED
            stop_after_attempt=3,
        )
        rag = ChromaRAGBuilder.build_multi_query_rag_via_ollama(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name=embedding_model_model_name,
            embedding_model_num_ctx=embedding_model_num_ctx,
            # HARDCODED
            embedding_model_repeat_penalty=None,
            embedding_model_temperature=None,
            embedding_model_stop_tokens=None,
            embedding_model_top_k=None,
            embedding_model_top_p=None,

            search_configs=search_configs,
            # LLM
            structured_llm=cast(
                'BaseChatModel',
                structured_llm,
            ),
            structured_llm_system_message=cast(
                'SystemMessage',
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=llm_system_message_template_path,
                ).format(),
            ),
        )
        return rag

    @staticmethod
    def create_multi_query_rag_via_huggingface(
        # Vector Store
        vector_store_persist_directory: str | Path,
        # Embedding Model
        embedding_model_model_name_or_path: str,
        embedding_model_model_kwargs: dict,
        embedding_model_encode_kwargs: dict,
        embedding_model_query_encode_kwargs: dict,
        embedding_model_is_multi_process: bool,
        embedding_model_cache_folder: str | None,
        embedding_model_is_show_progress: bool,
        # Retriever
        search_configs: dict,
        # LLM
        llm_base_url: str,
        llm_model_name: str,
        llm_system_message_template_path: str,
        # structured_output_format: type[BaseModel],
    ):
        structured_llm = LocalLLMFactory.create_openai_llm(
            base_url=llm_base_url,
            model_name=llm_model_name,
            # HARDCODED
            temperature=None,
            max_tokens=None,
            logprobs=None,
            use_responses_api=None,
            max_retries=None,
            model_configs={},
        ).with_structured_output(
            # HARDCODED
            schema=RewrittenQueries,
        ).with_retry(
            # HARDCODED
            stop_after_attempt=3,
        )
        rag = ChromaRAGBuilder.build_multi_query_rag_via_huggingface(
            vector_store_persist_directory=vector_store_persist_directory,
            embedding_model_model_name_or_path=embedding_model_model_name_or_path,
            embedding_model_model_kwargs=embedding_model_model_kwargs,
            embedding_model_encode_kwargs=embedding_model_encode_kwargs,
            embedding_model_query_encode_kwargs=embedding_model_query_encode_kwargs,
            embedding_model_is_multi_process=embedding_model_is_multi_process,
            embedding_model_cache_folder=embedding_model_cache_folder,
            embedding_model_is_show_progress=embedding_model_is_show_progress,
            search_configs=search_configs,
            # LLM
            # LLM
            structured_llm=cast(
                'BaseChatModel',
                structured_llm,
            ),
            structured_llm_system_message=cast(
                'SystemMessage',
                PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                    system_message_prompt_template_path=llm_system_message_template_path,
                ).format(),
            ),
        )
        return rag

