from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from agent.state import AgentState
from agent.prompts import SYSTEM_PROMPT

from tools.calculator_tool import calculator
from tools.wikipedia_tool import wikipedia_search


# --------------------------------------------------
# 1. Create the Llama 3.2 model
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 2. Create the available tools
# --------------------------------------------------

tools = [
    calculator,
    wikipedia_search
]


# --------------------------------------------------
# 3. Connect tools to Llama
# --------------------------------------------------

llm_with_tools = llm.bind_tools(
    tools
)


# --------------------------------------------------
# 4. Create the LLM node
# --------------------------------------------------

def call_llm(state: AgentState):

    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT
        )
    ] + state["messages"]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [response]
    }


# --------------------------------------------------
# 5. Create the Tool Node
# --------------------------------------------------

tool_node = ToolNode(
    tools
)


# --------------------------------------------------
# 6. Decide whether to use a tool or finish
# --------------------------------------------------

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:

        return "tools"

    return END


# --------------------------------------------------
# 7. Create the LangGraph
# --------------------------------------------------

graph = StateGraph(
    AgentState
)


# --------------------------------------------------
# 8. Add nodes
# --------------------------------------------------

graph.add_node(
    "llm",
    call_llm
)

graph.add_node(
    "tools",
    tool_node
)


# --------------------------------------------------
# 9. Set the starting point
# --------------------------------------------------

graph.set_entry_point(
    "llm"
)


# --------------------------------------------------
# 10. Connect LLM to Tool or END
# --------------------------------------------------

graph.add_conditional_edges(
    "llm",
    should_continue
)


# --------------------------------------------------
# 11. Connect Tool back to LLM
# --------------------------------------------------

graph.add_edge(
    "tools",
    "llm"
)


# --------------------------------------------------
# 12. Compile the graph
# --------------------------------------------------

app = graph.compile()


# --------------------------------------------------
# 13. Test the Agent
# --------------------------------------------------

if __name__ == "__main__":

    question = "What is Artificial Intelligence?"

    result = app.invoke(
        {
            "messages": [
                (
                    "user",
                    question
                )
            ]
        }
    )

    print("\n" + "=" * 60)

    print("\nUser Question:")
    print(question)

    print("\n" + "=" * 60)

    print("\nFinal Answer:")

    print(
        result["messages"][-1].content
    )