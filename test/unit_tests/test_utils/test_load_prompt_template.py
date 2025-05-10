"""

"""

from mas.utils import load_prompt_template


def test_load_prompt_template():
    prompt_template = load_prompt_template(
        '../../../mas/graph/prompts/recognizer_system_prompt_template.j2'
    )
    print(prompt_template)
    print(prompt_template.format())


if __name__ == '__main__':
    test_load_prompt_template()
