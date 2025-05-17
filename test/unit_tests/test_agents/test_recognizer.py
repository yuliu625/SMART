"""

"""

from mas.graph.states import MASState
from mas.graph.nodes import AgentFactory


def test_recognizer_1():
    agent_factory = AgentFactory()
    recognizer = agent_factory.get_recognizer()
    result = recognizer.run(MASState(original_pdf_text=""))
    print(result)


if __name__ == '__main__':
    test_recognizer_1()
