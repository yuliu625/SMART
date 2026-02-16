"""
构造 rag 的工厂。

配合 cached_mas_factory 使用。

使用 gateway 统一 LLM 层管理。
"""

from __future__ import annotations
from loguru import logger

# RAG

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


class QdrantRagFactory:
    ...

