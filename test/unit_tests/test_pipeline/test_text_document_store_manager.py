
from mas.data_processing.loading.text.text_document_store_processor import TextDocumentStoreProcessor


def test_text_document_store_manager():
    text_document_store_manager = TextDocumentStoreProcessor(
        text_document_store_dir=r"D:\dataset\risk_mas_t\langchain_t/document_store/text"
    )
    text_document_store_manager.run(
        pdf_path=r"D:\dataset\risk_mas_t\original_pdf\1910.13461v1.pdf",
        loading_method='rule'
    )


if __name__ == '__main__':
    test_text_document_store_manager()
