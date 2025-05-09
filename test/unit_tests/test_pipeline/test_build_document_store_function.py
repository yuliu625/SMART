"""

"""

from mas.data_processing.loading import build_document_store


def test_build_document_store_function():
    build_document_store(
        base_dir=r"D:\dataset\risk_mas_t",
        text_loading_methods=['rule', 'ocr'],
        image_loading_methods=['none'],
        convert_image_method='incremental',
    )


if __name__ == '__main__':
    test_build_document_store_function()
