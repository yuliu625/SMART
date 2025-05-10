"""
测试LLM和embedding_model是否可以正常请求。
"""

from mas.models import LLMFactory, VLMFactory
from mas.utils.base64_to_pil import uri_to_base64


def test_llm_1():
    llm_factory = LLMFactory()
    llm = llm_factory.get_qwen_llm()
    print(llm.invoke('你能说话不？'))


def test_vlm_1():
    vlm_factory = LLMFactory()
    vlm = vlm_factory.get_qwen_llm(model='qwen-vl-max')
    response = vlm.invoke(
        input=[
            {"role": "user",
             "content": [
                 {"type": "text", "text": "这是什么"},
                 {"type": 'image', "source_type": "base64",
                  "data": uri_to_base64(r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png"),
                  "mime_type": "image/png", }
             ]
             }
        ]
    )
    print(response)


if __name__ == '__main__':
    # test_llm_1()
    test_vlm_1()
