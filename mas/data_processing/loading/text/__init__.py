"""
从原始的pdf文档，转换为list[Document]。

文本方法:
    - pdf --识别文本--> single document --划分--> documents
"""

from .text_batch_processor import TextBatchProcessor

