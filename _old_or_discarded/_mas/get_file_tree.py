"""
文件树管理工具。

为简化文件树的管理，我遵循: 约定大于配置。

操作方法:
    - 全局配置。在项目根定义这个文件，所有路径相关均统一使用这个文件方法。
    - 指定_BASE_DIR。
    - 定义需要字段。使用pydantic定义所有的路径，类型全部是Path。
    - 定义文件树。在get_file_tree中写入所有的路径计算方法，基于pathlib实现。

使用:
    - 约定。所有文件都默认使用get_file_tree方法获取路径。
    - 项目迁移。仅修改_BASE_DIR。


该项目文件树结构为:
- base_dir
    - original_pdf
    - image_pdf
    - document_store
        - text
            - ${loading_method}
        - image
            - ${loading_method}
    - vector_store
        - text
            - ${embedding_method--loading_method}
        - image
            - ${embedding_method--loading_method}
"""

from pathlib import Path
from pydantic import BaseModel, Field


__BASE_DIR = r""


class FileTree(BaseModel):
    """声明所有需要的路径。"""
    base_dir: Path = Field(description="最基础的路径，其他路径都由这个路径生成。")
    original_pdf_dir: Path
    txt_pdf_dir: Path
    base_image_pdf_dir: Path
    document_store_dir: Path
    text_document_store_dir: Path
    image_document_store_dir: Path
    vector_store_dir: Path
    text_vector_store_dir: Path
    image_vector_store_dir: Path


def get_file_tree(
    base_dir: str = __BASE_DIR,
) -> FileTree:
    """
    全局的获取文件树的方法。

    Args:
        base_dir: 最根本的路径，其他路径都为其子路径。

    Returns:
        具体的所有子路径，都是Path对象。
    """
    base_dir = Path(base_dir)
    # 这里写生成FileTree的方法
    file_tree = FileTree(
        base_dir=base_dir,
        original_pdf_dir=base_dir / 'original_pdf',
        txt_pdf_dir=base_dir / 'txt_pdf',
        base_image_pdf_dir=base_dir / 'image_pdf',
        document_store_dir=base_dir / 'document_store',
        text_document_store_dir=base_dir / 'document_store' / 'text',
        image_document_store_dir=base_dir / 'document_store' / 'image',
        vector_store_dir=base_dir / 'vector_store',
        text_vector_store_dir=base_dir / 'vector_store' / 'text',
        image_vector_store_dir=base_dir / 'vector_store' / 'image',
    )
    return file_tree

