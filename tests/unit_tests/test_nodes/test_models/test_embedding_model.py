"""

"""

from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.nodes.models import EmbeddingModelFactory


def test_embedding_model_factory_1():
    embedding_model_factory = EmbeddingModelFactory()
    embedding_model = embedding_model_factory.get_model1()
    print(embedding_model.embed_query("喂喂喂"))
    print(embedding_model.embed_text("喂喂喂"))


def test_embedding_model_factory_2():
    embedding_model_factory = EmbeddingModelFactory()
    embedding_model = embedding_model_factory.get_model2()
    print(embedding_model.embed_query("喂喂喂"))
    print(embedding_model.embed_documents("喂喂喂"))


def test_embedding_model_factory_5():
    embedding_model_factory = EmbeddingModelFactory()
    embedding_model = embedding_model_factory.get_embedding_model_by_key('model5')
    print(embedding_model.embed_text(["喂喂喂"]))
    print(embedding_model.embed_image([r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png"]))


def test_embedding_model_factory_6():
    embedding_model_factory = EmbeddingModelFactory()
    embedding_model = embedding_model_factory.get_embedding_model_by_key('model6')
    print(embedding_model.embed_text(["喂喂喂"]))
    print(embedding_model.embed_image([r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png"]))
    print(len(embedding_model.embed_text(["喂喂喂"])[0]))
    print(len(embedding_model.embed_image([r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png"])[0]))


if __name__ == '__main__':
    # test_embedding_model_factory_1()
    # test_embedding_model_factory_2()
    # test_embedding_model_factory_5()
    test_embedding_model_factory_6()
