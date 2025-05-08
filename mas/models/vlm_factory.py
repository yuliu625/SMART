"""
生成VLM的工厂。
"""

from typing import Annotated
import os


class VLMFactory:
    def __init__(self):
        ...

    def get_qwen_vlm(
        self,
        model: Annotated[str, "qwen系列模型的名字"] = 'qwen-vl-max-latest'
    ):
        """
        获得qwen的VLM。
        由于现有的各种agent-framework对于VLM不完全支持，这里专门去使用。

        Returns:
            llama-index中的MultiModalLLM。这里是qwen-vl-max，我默认使用这个。
        """
        dashscope_multi_modal_llm = DashScopeMultiModal(
            model_name=model,
            api_key=os.environ['DASHSCOPE_API_KEY'],
            vl_high_resolution_images=True,  # 因为文档的缺失，不是很确定这个参数是否有效。为了冗余，会在每次请求时额外再指定。
        )
        return dashscope_multi_modal_llm


if __name__ == '__main__':
    pass
