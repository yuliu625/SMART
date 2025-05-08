"""
测试获取embedding-model映射信息的正确。
"""

from mas.models import EmbeddingModelInfoManager


def test_embedding_model_info_manager(model_key: str = 'model_1'):
    embedding_model_info_manager = EmbeddingModelInfoManager()
    a_name = embedding_model_info_manager.get_name(model_key)
    a_dim = embedding_model_info_manager.get_dim(model_key)
    a_path = embedding_model_info_manager.get_path(model_key)
    print(a_name, a_dim, a_path)


if __name__ == '__main__':
    test_embedding_model_info_manager()
