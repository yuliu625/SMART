"""

"""

from mas.data_processing.loading.image.image_document_store_processor import ImageDocumentStoreProcessor


def test_image_document_store_manager():
    image_document_store_manager = ImageDocumentStoreProcessor(
        image_document_store_dir=r"D:\dataset\risk_mas_t\langchain_t\document_store/image",
    )
    image_document_store_manager.run(
        image_pdf_dir=r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf",
        loading_method='none'
    )


if __name__ == '__main__':
    test_image_document_store_manager()
