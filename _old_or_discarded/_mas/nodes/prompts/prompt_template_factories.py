"""
为了对比实验，各种类型的prompt-template-factory。
"""

from __future__ import annotations

from .base_prompt_template_factory import BasePromptTemplateFactory

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class AllPromptTemplateFactory(BasePromptTemplateFactory):
    def __init__(
        self,
    ):
        super().__init__()
        self.set_sub_dir('all')


class RAGPromptTemplateFactory(BasePromptTemplateFactory):
    def __init__(
        self,
    ):
        super().__init__()
        self.set_sub_dir('rag')

