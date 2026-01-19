"""
Sources:

References:

Synopsis:

Notes:

"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

class LocalLlmFactory:
    @staticmethod
    def create_openai_llm(

    ) -> BaseChatModel:
        ...

    @staticmethod
    def create_ollama_llm(

    ) -> BaseChatModel:
        ...

    @staticmethod
    def create_huggingface_llm(

    ) -> BaseChatModel:
        ...

