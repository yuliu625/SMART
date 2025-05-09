"""

"""

from mas.data_processing.indexing import build_text_vector_store, build_image_vector_store


def test_build_text_vector_store():
    build_text_vector_store(
        base_dir=r"D:\dataset\risk_mas_t",
        text_embedding_methods=['model1'],
        text_loading_methods=['rule', 'ocr']
    )


def test_build_image_vector_store():
    build_image_vector_store(
        base_dir=r"D:\dataset\risk_mas_t",
        image_loading_methods=['none'],
        image_embedding_methods=['model2']
    )


if __name__ == '__main__':
    # test_build_text_vector_store()
    test_build_image_vector_store()
