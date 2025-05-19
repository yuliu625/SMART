"""

"""

from mas.data_processing import (
    build_document_store,
    build_text_vector_store,
    build_image_vector_store,
)


def main(
    base_dir: str,
    text_embedding_methods: list[str],
    text_loading_methods: list[str],
    image_embedding_methods: list[str],
    image_loading_methods: list[str],
):
    build_document_store(
        base_dir=base_dir, text_loading_methods=text_loading_methods, image_loading_methods=image_loading_methods
    )
    build_text_vector_store(
        base_dir=base_dir, text_embedding_methods=text_embedding_methods, text_loading_methods=text_loading_methods
    )
    build_image_vector_store(
        base_dir=base_dir, image_embedding_methods=image_embedding_methods, image_loading_methods=image_loading_methods
    )


if __name__ == '__main__':
    base_dir = r""

    text_loading_methods = ['rule', 'ocr', 'vlm']
    text_embedding_methods = ['model1', 'model2', 'model3']
    image_loading_methods = ['none']
    image_embedding_methods = ['model4', 'model5', 'model6', 'model7', 'model8']
    main(
        base_dir=base_dir,
        text_embedding_methods=text_embedding_methods,
        text_loading_methods=text_loading_methods,
        image_embedding_methods=image_embedding_methods,
        image_loading_methods=image_loading_methods,
    )
