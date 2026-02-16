"""
实验运行的vllm的配置。
"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


# Qwen/Qwen2.5-1.5B-Instruct
# http://127.0.0.1:8970/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-1.5B-Instruct',
    host='127.0.0.1',
    port=8970,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen2.5-3B-Instruct
# http://127.0.0.1:8971/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-3B-Instruct',
    host='127.0.0.1',
    port=8971,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen2.5-7B-Instruct
# http://127.0.0.1:8972/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct',
    host='127.0.0.1',
    port=8972,
    gpu_memory_utilization=0.2,
    tensor_parallel_size=1,
    max_model_len=32768,
    # max_num_batched_tokens=131072,
    max_num_seqs=1,
    # lora_modules=None,
)
# Qwen/Qwen2.5-14B-Instruct
# http://127.0.0.1:8973/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-14B-Instruct',
    host='127.0.0.1',
    port=8973,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen2.5-32B-Instruct
# http://127.0.0.1:8974/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-32B-Instruct',
    host='127.0.0.1',
    port=8974,
    gpu_memory_utilization=0.9,
    tensor_parallel_size=1,
    max_model_len=65536,
    # max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen2.5-72B-Instruct
# http://127.0.0.1:8975/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-72B-Instruct',
    host='127.0.0.1',
    port=8975,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)

# Qwen/Qwen2.5-7B-Instruct-1M
# http://127.0.0.1:8976/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-7B-Instruct-1M',
    host='127.0.0.1',
    port=8976,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)

# Qwen/Qwen2.5-14B-Instruct-1M
# http://127.0.0.1:8977/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen2.5-14B-Instruct-1M',
    host='127.0.0.1',
    port=8977,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)


# Qwen/Qwen3-1.7B
# http://127.0.0.1:8978/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen/Qwen3-1.7B',
    host='127.0.0.1',
    port=8978,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen3-4B
# http://127.0.0.1:8979/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen/Qwen3-4B',
    host='127.0.0.1',
    port=8979,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen3-8B
# http://127.0.0.1:8980/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen/Qwen3-8B',
    host='127.0.0.1',
    port=8980,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen3-14B
# http://127.0.0.1:8981/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen/Qwen3-14B',
    host='127.0.0.1',
    port=8981,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)
# Qwen/Qwen3-32B
# http://127.0.0.1:8982/v1/chat/completions
dict(
    mode='serve',
    model_name_or_path=r'/home/liuyu/liuyu_nfs_data/model/Qwen/Qwen/Qwen3-32B',
    host='127.0.0.1',
    port=8982,
    gpu_memory_utilization=0.1,
    tensor_parallel_size=4,
    max_model_len=1010000,
    max_num_batched_tokens=131072,
    max_num_seqs=1,
    lora_modules=None,
)

