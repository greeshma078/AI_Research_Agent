from typing import Annotated

from langgraph.graph.message import add_messages


class AgentState:

    messages: Annotated[
        list,
        add_messages
    ]