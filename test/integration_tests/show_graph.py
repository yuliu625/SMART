"""

"""

from mas.utils import save_graph_png
from mas.graph import MASGraphBuilder


def show_graph():
    mas_graph = MASGraphBuilder()
    graph = mas_graph.build_graph()
    save_graph_png(graph, output_path='./t.png')


if __name__ == '__main__':
    show_graph()
