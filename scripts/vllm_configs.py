"""
实验运行的vllm的配置。
"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


# Qwen/Qwen2.5-7B-Instruct-1M
# http://localhost:12345/v1/chat/completions
dict(
    mode='serve',
    model=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
    host='127.0.0.1',
    port=12345,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=600000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)

