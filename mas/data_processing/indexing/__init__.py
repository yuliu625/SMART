"""
使用已有的文档存储，生成对应的embedding。

每个vector-store对应同一embedding-model。

文件树结构为:
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

metadata内容:
在原基础上添加'loading_method'和'embedding_method'。
text:
{
    'modality': 'text',
    'pdf_name': <Path.name>,
    'loading_method': <loading_method>,
    'embedding_method': <embedding_method>,
}
image:
{
    'modality': 'image',
    'pdf_name': <Path.parent.name>,
    'page_num': <Path.name>,
    'loading_method': <loading_method>,
    'embedding_method': <embedding_method>,
}

"""

