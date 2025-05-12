"""

"""

from mas.graph.prompts import PromptTemplateFactory


def test_prompt_template_factory_1():
    prompt_template_factory = PromptTemplateFactory('all')
    print(prompt_template_factory.get_system_prompt_template('document_reader'))


def test_prompt_template_factory_2():
    prompt_template_factory = PromptTemplateFactory('all')
    print(prompt_template_factory.get_system_prompt_template('recognizer'))


if __name__ == '__main__':
    test_prompt_template_factory_1()
