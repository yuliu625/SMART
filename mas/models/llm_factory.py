"""
生成LLM的工厂。
"""

from langchain_openai import ChatOpenAI

import os

from typing import Annotated


class LLMFactory:
    def __init__(self):
        ...

    def get_qwen_llm(
        self,
        model: Annotated[str, "qwen系列模型的名字"] = 'qwen-max'
    ) -> ChatOpenAI:
        llm = ChatOpenAI(
            model=model,
            base_url=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
        )
        return llm


if __name__ == '__main__':
    pass
