"""
测试LLM和embedding_model是否可以正常请求。
"""

from mas.utils import LLMFactory, VLMFactory, EmbeddingModelFactory


def test_llm():
    llm_factory = LLMFactory()
    llm = llm_factory.get_qwen_llm()


def test_vlm():
    vlm_factory = VLMFactory()
    vlm = vlm_factory.get_qwen_vlm()


def test_embedding_model():
    embedding_model_factory = EmbeddingModelFactory()


if __name__ == '__main__':
    pass
