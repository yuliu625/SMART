"""

"""

from mas.global_config import LLM_MAS_RETRIES
from mas.utils import JsonOutputParser

from langchain_core.runnables import Runnable
from pydantic import BaseModel
from typing import Type, Annotated


class BaseAgent:
    def __init__(
        self,
        llm_chain: Annotated[Runnable, "llm-chain，具有system-prompt的llm，以chat-history的list进行invoke"],
        is_need_structured_output: bool = False,
        structured_output_format: Annotated[Type[BaseModel], "结构化输出格式的schema，默认使用pydantic。"] = None,
    ):
        self.llm_chain = llm_chain
        self._is_need_structured_output = is_need_structured_output
        self._structured_output_format = structured_output_format

    def request_llm(self, messages: list):
        content = ""
        for i in range(LLM_MAS_RETRIES):
            response = self.llm_chain.invoke(messages)
            content = response.content
            if not self._is_need_structured_output:
                # 如果不需要结构化输出，请求一次就够了。
                break
            # 需要结构化输出，尝试解析。
            result = self._extract_json_from_response(content)
            if result:
                # 已经产生有效的结果，终止循环。
                break
        messages.append(response)
        return messages

    def _extract_json_from_response(self, response: str) -> dict | None:
        """这个方法使用我已经构建的复用工具来实现。"""
        if self._structured_output_format is None:
            # 如果未指定结构化输出，尝试提取markdown中的内容。无论怎么样都会运行，可用不使用提取结果。
            return JsonOutputParser.extract_json_from_str(response)
        else:
            # 进行提取，提取的结果会以python可以处理的格式返回。
            return JsonOutputParser.extract_json_from_str(
                response,
                schema_model=self._structured_output_format,
            )

