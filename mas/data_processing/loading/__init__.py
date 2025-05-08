"""
文档加载，冷启动。

先将document使用假embedding-model编码，存入vector-store中，后续更新真正embedding-model的编码。

文件树结构为:
    - document_store
        - text
            - ${loading_method}
        - image
            - ${loading_method}

collection-name使用默认命名，所有文档均存储在同一collection中，以metadata进行区分。

metadata内容:
text:
{
    'modality': 'text',
    'loading_method': <rule, ocr, vlm>,
    'pdf_name': <Path.name>,
}
image:
{
    'modality': 'image',
    'loading_method': 'none',
    'pdf_name': <Path.parent.name>,
    'page_num': <Path.name>,
}

"""



