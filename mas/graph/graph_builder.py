"""

"""

from langgraph.graph import StateGraph
# from langgraph.graph.graph import (
#     END,
#     START,
#     CompiledGraph,
#     Graph,
#     Send,
# )


class MASGraph:
    def __init__(
        self,
    ):
        ...

    def build_graph(
        self,
        State,
    ):
        graph_builder = StateGraph(State)

        graph = graph_builder.compile()
        return graph

    def _init_nodes(self):
        self.nodes = []

    def _init_edges(self):
        ...

