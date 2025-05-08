"""

"""

from langchain_community.embeddings.huggingface import HuggingFaceEmbedding


def get_embedding_model():
    embedding_model = HuggingFaceEmbedding(
        # model_name=r"D:\model\nomic-ai\colnomic-embed-multimodal-7b",
        model_name=r"D:\model\nomic-ai\nomic-embed-text-v1.5",
        trust_remote_code=True
    )
    return embedding_model


if __name__ == '__main__':
    pass
