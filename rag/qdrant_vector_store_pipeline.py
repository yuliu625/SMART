"""
以下方法几乎是 one time script 。

针对性设计:
    - FlagEmbedding: 为了使用 bge-m3 的全部功能，只能直接使用原生 transformers 。
    - qdrant: pipeline 中，先计算 embedding 后构建 client。完全为了避免 显存溢出导致创建 vector store 但内容为空的意外。
    - 避免重复加载: 因为推理未服务化，FP 中是能持续持有 embedding model 。
"""

from __future__ import annotations
from loguru import logger

from rag.loading.load_text import TextLoadingMethods
from rag.splitting.split_markdown import MarkdownSplittingMethods
from rag.splitting.split_text import TextSplittingMethods
from rag.embedding.flag_embedding.bge_m3_embedding_model import BGEM3EmbeddingModel
from rag.storing.qdrant_client_builder import QdrantClientBuilder
from rag.storing.qdrant_point_builder import QdrantPointBuilder
from rag.storing.qdrant_vector_store_writer import QdrantVectorStoreWriter

from qdrant_client.models import (
    PointStruct,
    SparseVector,
    Distance,
    VectorParams,
    SparseVectorParams,
    SparseIndexParams,
    MultiVectorConfig,
    MultiVectorComparator,
)
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class QdrantVectorStorePipeline:
    # ==== 专用方法。 ====
    @staticmethod
    def make_vector_store_via_native_bge_m3(
        # loading
        markdown_file_path: str | Path,
        # splitting
        headers_to_split_on: list[tuple[str, str]],
        # embedding
        embedding_model_name_or_path: str,
        embedding_model_configs: dict,
        # storing
        vector_store_path: str | Path,
    ):
        # loading
        document = TextLoadingMethods.load_text(
            text_path=markdown_file_path,
            # HARDCODED
            encoding='utf-8',
            is_autodetect_encoding=False,
        )
        # chunks
        documents = MarkdownSplittingMethods.split_markdown_by_header(
            document=document,
            headers_to_split_on=headers_to_split_on,
            # HARDCODED
            is_strip_headers=False,
        )
        documents = TextSplittingMethods.split_documents_recursively(
            documents=documents,
            # HARDCODED
            chunk_size=4096,
            chunk_overlap=50,
        )
        ## for quick test
        # documents = documents[:2]
        # HACK: for native bge-m3 embedding model
        bge_m3_embedding_model = BGEM3EmbeddingModel(
            model_name_or_path=embedding_model_name_or_path,
            batch_size=embedding_model_configs['batch_size'],
        )
        encoded_results = bge_m3_embedding_model.encode_texts(
            texts=[
                document.page_content
                for document in documents
            ],
        )
        # build points for qdrant
        ## Specific: process sparse vector
        _sparse_vectors = [
            SparseVector(
                indices=[int(k) for k in bge_output.keys()],
                values=[float(v) for v in bge_output.values()],
            )
            for bge_output in encoded_results['sparse']
        ]
        points = QdrantPointBuilder.build_points(
            documents=documents,
            dense_vectors=encoded_results['dense'],
            sparse_vectors=_sparse_vectors,
            multi_vectors=encoded_results['multi_vector'],
        )
        logger.trace(f"Point: \n{points}")
        # HACK: for bge-m3 qdrant client
        client = QdrantClientBuilder.create_empty_client_from_disk(
            path=vector_store_path,
            # HARDCODED: all for bge-m3
            collection_name='default',
            vectors_config=dict(
                dense=VectorParams(
                    size=1024,
                    distance=Distance.COSINE,
                ),
                multi_vector=VectorParams(
                    size=1024,
                    distance=Distance.COSINE,
                    multivector_config=MultiVectorConfig(
                        comparator=MultiVectorComparator.MAX_SIM,
                    )
                )
            ),
            sparse_vectors_config=dict(
                sparse=SparseVectorParams(
                    index=SparseIndexParams(
                        on_disk=False,
                    )
                )
            )
        )
        # upload points to qdrant
        client = QdrantVectorStoreWriter.add_points(
            client=client,
            collection_name='default',  # HARDCODED
            points=points,
        )
        return client

    @staticmethod
    def batch_make_vector_store_via_native_bge_m3(
        # loading
        markdown_file_path: str | Path,
        # splitting
        headers_to_split_on: list[tuple[str, str]],
        # embedding
        bge_m3_embedding_model,
        # storing
        vector_store_path: str | Path,
    ):
        # loading
        document = TextLoadingMethods.load_text(
            text_path=markdown_file_path,
            # HARDCODED
            encoding='utf-8',
            is_autodetect_encoding=False,
        )
        # chunks
        documents = MarkdownSplittingMethods.split_markdown_by_header(
            document=document,
            headers_to_split_on=headers_to_split_on,
            # HARDCODED
            is_strip_headers=False,
        )
        documents = TextSplittingMethods.split_documents_recursively(
            documents=documents,
            # HARDCODED
            chunk_size=4096,
            chunk_overlap=50,
        )
        ## for quick test
        # documents = documents[:2]
        # HACK: for native bge-m3 embedding model
        # bge_m3_embedding_model = BGEM3EmbeddingModel(
        #     model_name_or_path=embedding_model_name_or_path,
        #     batch_size=embedding_model_configs['batch_size'],
        # )
        encoded_results = bge_m3_embedding_model.encode_texts(
            texts=[
                document.page_content
                for document in documents
            ],
        )
        # build points for qdrant
        ## Specific: process sparse vector
        _sparse_vectors = [
            SparseVector(
                indices=[int(k) for k in bge_output.keys()],
                values=[float(v) for v in bge_output.values()],
            )
            for bge_output in encoded_results['sparse']
        ]
        points = QdrantPointBuilder.build_points(
            documents=documents,
            dense_vectors=encoded_results['dense'],
            sparse_vectors=_sparse_vectors,
            multi_vectors=encoded_results['multi_vector'],
        )
        logger.trace(f"Point: \n{points}")
        # HACK: for bge-m3 qdrant client
        client = QdrantClientBuilder.create_empty_client_from_disk(
            path=vector_store_path,
            # HARDCODED: all for bge-m3
            collection_name='default',
            vectors_config=dict(
                dense=VectorParams(
                    size=1024,
                    distance=Distance.COSINE,
                ),
                multi_vector=VectorParams(
                    size=1024,
                    distance=Distance.COSINE,
                    multivector_config=MultiVectorConfig(
                        comparator=MultiVectorComparator.MAX_SIM,
                    )
                )
            ),
            sparse_vectors_config=dict(
                sparse=SparseVectorParams(
                    index=SparseIndexParams(
                        on_disk=False,
                    )
                )
            )
        )
        # upload points to qdrant
        client = QdrantVectorStoreWriter.add_points(
            client=client,
            collection_name='default',  # HARDCODED
            points=points,
        )
        return client

    @staticmethod
    def build_bge_m3_embedding_model(
        embedding_model_name_or_path: str,
        embedding_model_configs: dict,
    ):
        # HACK: for native bge-m3 embedding model
        bge_m3_embedding_model = BGEM3EmbeddingModel(
            model_name_or_path=embedding_model_name_or_path,
            batch_size=embedding_model_configs['batch_size'],
        )
        return bge_m3_embedding_model

