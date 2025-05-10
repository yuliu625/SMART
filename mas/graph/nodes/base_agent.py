"""

"""

from mas.global_config import LLM_MAS_RETRIES
from mas.utils import JsonOutputParser

from langchain_core.runnables import Runnable
from pydantic import BaseModel
from typing import Type


class BaseAgent:
    def __init__(
        self,
        llm: Runnable,
        structured_output_format: Type[BaseModel] = None,  # 结构化输出格式的schema，默认使用pydantic。
    ):
        self.llm = llm
        self._structured_output_format = structured_output_format

    def request_llm(self, messages: list):
        for i in range(LLM_MAS_RETRIES):
            response = self.llm.invoke(messages)
            result = self._extract_json_from_response(response.content)
            if result:
                # 已经产生有效的结果，终止循环。
                break
        messages.append(response)
        return messages

    def _extract_json_from_response(self, response: str) -> dict | None:
        """这个方法使用我已经构建的复用工具来实现。"""
        if self._structured_output_format is None:
            return JsonOutputParser.extract_json_from_str(response)
        else:
            return JsonOutputParser.extract_json_from_str(
                response,
                schema_model=self._structured_output_format,
            )

