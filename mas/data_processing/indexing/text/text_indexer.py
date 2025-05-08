"""

"""


class TextIndexer:
    """
    指定冷启动的vector_store，给出embedding_model，生成对应的embedding。
    """
    def __init__(
        self,
        embedding_model,
    ):
        ...

    def run(
        self,
    ):
        ...

    def generate_embedding_for_document_store(
            self,
            vector_store,
            embedding_model,
    ):
        ...
