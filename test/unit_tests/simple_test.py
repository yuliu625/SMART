from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from typing import TypedDict, Annotated
from operator import add
from langgraph.graph.message import add_messages
from langgraph.graph import MessagesState
#%%
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    extra_field: int
#%%
class State(MessagesState):
    extra_field: int
#%%
def node(state: State):
    messages = state["messages"]
    new_message = AIMessage("Hello!")

    return {"messages": [new_message], "extra_field": 10}
#%%
from langgraph.graph import StateGraph

graph_builder = StateGraph(State)
graph_builder.add_node(node)
graph_builder.set_entry_point("node")
graph = graph_builder.compile()
#%%
from IPython.display import Image, display

Image(
    graph.get_graph().draw_mermaid_png(
        output_file_path='./t.png',
    ),
)