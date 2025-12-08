"""

"""

from mas.nodes.models import YuFakeEmbeddingModel
from _data_processing import MetadataTools

from langchain_chroma import Chroma

from pathlib import Path


class ImageDocumentStoreProcessor:
    """

    """
    def __init__(
        self,
        image_document_store_dir: str | Path,
    ):
        self.image_document_store_dir = Path(image_document_store_dir)
        self.image_document_store_dir.mkdir(exist_ok=True, parents=True)

    def run(
        self,
        image_pdf_dir: str | Path,
        loading_method: str = 'none',
    ) -> None:
        image_pdf_dir = Path(image_pdf_dir)
        image_paths = list(image_pdf_dir.glob('*.png'))
        self.add_images_to_vector_store(image_paths)
        print(f"added image {image_pdf_dir.name} to {self.image_document_store_dir / loading_method}")

    def add_images_to_vector_store(
        self,
        image_paths: list[Path],
        loading_method: str = 'none',
    ) -> None:
        vector_store = Chroma(
            embedding_function=YuFakeEmbeddingModel(),
            persist_directory=str(self.image_document_store_dir / loading_method),
        )
        vector_store.add_images(
            uris=[str(image_path) for image_path in image_paths],
            metadatas=[self.get_metadata(image_path) for image_path in image_paths]
        )

    def get_metadata(
        self,
        image_path: str | Path,
    ) -> dict:
        image_path = Path(image_path)
        metadata_tools = MetadataTools()
        metadata = metadata_tools.get_image_metadata(image_path=image_path)
        return metadata

