"""

"""

from _data_processing import MetadataTools
from mas.nodes.models import EmbeddingModelFactory

from langchain_chroma import Chroma

from pathlib import Path


class ImageVectorStoreIndexer:
    """

    """
    def __init__(
        self,
        image_vector_store_dir: str | Path,
    ):
        self.image_vector_store_dir = Path(image_vector_store_dir)
        self.image_vector_store_dir.mkdir(exist_ok=True, parents=True)

    def run(
        self,
        image_pdf_dir: str | Path,
        loading_method: str,
        embedding_method: str,
    ) -> None:
        image_pdf_dir = Path(image_pdf_dir)
        image_paths = list(image_pdf_dir.glob('*.png'))
        self.add_images_to_vector_store(
            image_paths=image_paths,
            loading_method=loading_method,
            embedding_method=embedding_method
        )
        print(f"added image {image_pdf_dir.name} to {self.image_vector_store_dir / f"{embedding_method}--{loading_method}"}")

    def add_images_to_vector_store(
        self,
        image_paths: list[Path],
        embedding_method: str,
        loading_method: str = 'none',
    ) -> None:
        embedding_model_factory = EmbeddingModelFactory()
        embedding_model = embedding_model_factory.get_embedding_model_by_key(
            model_key=embedding_method,
        )
        vector_store = Chroma(
            embedding_function=embedding_model,
            persist_directory=str(self.image_vector_store_dir / f"{embedding_method}--{loading_method}"),
        )
        vector_store.add_images(
            uris=[str(image_path) for image_path in image_paths],
            metadatas=[self.get_metadata(image_path, embedding_method) for image_path in image_paths]
        )

    def get_metadata(
        self,
        image_path: str | Path,
        embedding_method: str,
    ) -> dict:
        image_path = Path(image_path)
        metadata_tools = MetadataTools()
        metadata = metadata_tools.get_full_image_metadata(
            image_path=image_path,
            embedding_method=embedding_method,
        )
        return metadata

