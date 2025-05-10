"""

"""

from mas.graph.prompts import PromptTemplateFactory


def test_prompt_template_factory():
    prompt_template_factory = PromptTemplateFactory()
    print(prompt_template_factory.get_system_prompt_template('recognizer'))


if __name__ == '__main__':
    test_prompt_template_factory()
