"""
生成LLM的工厂。
"""


import os

from typing import Annotated


class LLMFactory:
    def __init__(self):
        ...

    # def get_qwen_llm(
    #     self,
    #     model: Annotated[str, "qwen系列模型的名字"] = 'qwen-max'
    # ) -> OpenAILike:
    #     llm = OpenAILike(
    #         model=model,
    #         api_base=os.environ['DASHSCOPE_API_BASE_URL'],
    #         api_key=os.environ['DASHSCOPE_API_KEY'],
    #         is_chat_model=True,
    #         is_function_calling_model=True,
    #     )
    #     return llm


if __name__ == '__main__':
    pass
