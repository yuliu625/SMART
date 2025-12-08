"""

"""

from .text_indexer import TextIndexer

from pathlib import Path


class TextBatchIndexer:
    """

    """
    def __init__(
        self,
        base_dir: str | Path,
    ):
        self.base_dir = Path(base_dir)

    def batch_process(
        self,
        embedding_methods: list[str],
        loading_methods: list[str],
    ):
        for embedding_method in embedding_methods:
            for loading_method in loading_methods:
                self.run_a_indexer(
                    base_dir=self.base_dir,
                    embedding_method=embedding_method,
                    loading_method=loading_method,
                )

    def run_a_indexer(
        self,
        base_dir: str | Path,
        loading_method: str,
        embedding_method: str,
    ):
        text_indexer = TextIndexer(base_dir=base_dir)
        text_indexer.run(
            loading_method=loading_method,
            embedding_method=embedding_method,
        )

