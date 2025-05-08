
# path
BASE_PATH = rf""
ORIGINAL_PDF_DIR = rf"{BASE_PATH}/original_pdf"
BASE_IMAGE_PDF_DIR = rf"{BASE_PATH}/image_pdf"
DOCUMENT_STORE_DIR = rf"{BASE_PATH}/document_store"
PIPELINE_CACHE_DIR = rf"{BASE_PATH}/pipeline_cache"
VECTOR_STORE_DIR = rf"{BASE_PATH}/vector_store"
INDEX_STORE_DIR = rf"{BASE_PATH}/index_store"


# pdf
TEXT_LOADING_MODE = ['rule', 'ocr', 'vlm', ]
TEXT_PARSING_MODE = ['markdown', ]
IMAGE_PARSING_MODE = ['none', ]


# milvus
URI = "http://localhost:19530"


# IngestionPipeline cache
# PIPELINE_CACHE=dict(
#     text=dict(
#         parsing=['markdown'],
#         embedding=['', ],
#     ),
#     image=dict(
#         parsing=['none'],
#         embedding=['', ],
#     )
# )

PIPELINE_CACHE_CONTENT = dict(
    parsing=['markdown', ],
    embedding=['model_1', 'model_2', 'model_3', 'model_4', ]
)


# vector store pipeline
VECTOR_STORE_PIPELINE = [
    ['text', 'rule', 'model_1'],
    ['text', 'ocr', 'model_1'],
    ['text', 'vlm', 'model_1'],
    ['image', 'none', 'model_2'],
    ['image', 'none', 'model_3'],
    ['image', 'none', 'model_4'],
]


# pipeline or name required fields
REQUIRED_CONFIG = dict(
    modality_type="模态。也有document_store_type，具体为['text', 'image']",
    loading_method="文件加载方法。text有['rule', 'ocr', 'vlm']， image有['none']",
    # parsing_method="这个字段没有，因为text一定是['markdown']， image不进行。"
    embedding_method="使用的embedding-model。以键值映射管理。",
    pdf_name="pdf的名字。最重要。",
)

