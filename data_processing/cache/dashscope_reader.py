"""
Sources:
    https://github.com/yuliu625/Yu-Deep-Learning-Toolkit/natural_language_processing/llm_reader/dashscope_reader.py

References:
    https://help.aliyun.com/zh/model-studio/long-context-qwen-long

Synopsis:
    针对 DashScope 平台的长文本处理方法。

Notes:
    对于极长文本，dashscope 需要上传文件并处理。

    默认支持的模型为 qwen-long ，目前做对于该模型的适配。
"""

from __future__ import annotations
from loguru import logger

from openai import OpenAI

import os
from pathlib import Path
import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pydantic import BaseModel


class QwenLongReader:
    @staticmethod
    def read_file(
        file_id: str,
        system_message_content: str,
        human_message_content: str,
        result_path: str | Path,
    ) -> BaseModel:
        # 构造client，使用OpenAI Client兼容方法。
        client = OpenAI(
            # HARDCODED
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
        )
        completion = client.chat.completions.create(
            # HARDCODED
            model="qwen-long",
            messages=[
                # System1: instruction
                {'role': 'system', 'content': system_message_content},
                # System2: file content
                {'role': 'system', 'content': f'fileid://{file_id}'},
                # Human Message: task
                {'role': 'user', 'content': human_message_content},
            ],
        )
        logger.trace(f"completion: \n{completion}")
        # 路径处理。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # save result
        result_path.write_text(
            json.dumps(completion.model_dump(), ensure_ascii=False, indent=4),
            encoding='utf-8',
        )
        return completion

