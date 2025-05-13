"""
封装通过文件加载prompt-template的过程。

仅暴露可直接使用format方法的prompt-template对象。
"""


from mas.utils import load_prompt_template
from pathlib import Path
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate

from langchain_core.messages import BaseMessage
from langchain_core.prompts import BasePromptTemplate
from typing import Literal


class PromptTemplateFactory:
    """
    prompt-template的生成工厂。

    封装了:
        - 路径管理。不同的prompt文件树管理，默认2级文件。
        - prompt加载。返回langchain可用的BaseMessage。
    """
    def __init__(
        self,
        mode: Literal['all', 'text_only', 'wo_query_engine'] = 'all',
        prompts_dir: str | Path = None,
    ):
        if prompts_dir is None:
            self.prompts_dir = Path(__file__).parent
        else:
            self.prompts_dir = Path(prompts_dir)
        self.prompts_dir = self.prompts_dir / mode

    def get_system_message(
        self,
        agent_name: str,
        **kwargs,
    ) -> SystemMessage:
        system_prompt_template = load_prompt_template(self.prompts_dir / f"{agent_name}_system_prompt_template.j2")
        system_prompt = system_prompt_template.format(**kwargs)
        return SystemMessage(system_prompt)




