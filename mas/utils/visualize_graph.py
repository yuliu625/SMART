"""

"""

from IPython.display import Image, display


def get_graph_png(graph):
    """
    只能在ipynb中进行可视化的方法。

    Args:
        graph:

    Returns:

    """
    display(Image(graph.get_graph().draw_mermaid_png()))


def save_graph_png(graph, output_path=None):
    """
    脚本中也可以可视化的方法，但是默认分辨率低。

    Args:
        graph:
        output_path:

    Returns:

    """
    Image(
        graph.get_graph().draw_mermaid_png(
            output_file_path=output_path,
        ),
    )

