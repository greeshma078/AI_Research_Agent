# 🤖 AI Research Agent

An **Agentic AI research assistant** built with **Python, LangChain, LangGraph, Ollama, Llama 3.2, and Streamlit**.

The agent can understand a user's question, decide whether a tool is required, select the appropriate tool, execute it, and generate a final response.

The project demonstrates the core workflow of an **AI Agent with tool calling and LangGraph-based orchestration**.

---

## 🚀 Features

* 🤖 **Llama 3.2** as the Large Language Model
* 🧠 **LangChain** for LLM and tool integration
* 🔄 **LangGraph** for agent workflow orchestration
* 🧮 **Calculator Tool** for mathematical calculations
* 📚 **Wikipedia Tool** for factual information
* 🛠️ **Tool Calling** — the LLM decides which tool to use
* 🔁 **Agent Loop** — tool results are returned to the LLM for final responses
* 🎨 **Streamlit UI** for an interactive web application
* 🏠 **Ollama** for running the LLM locally
* 🔐 No paid API key required

---

## 🧠 What is an AI Agent?

An AI Agent is a system that can:

1. Understand a user's request
2. Decide what action is required
3. Select an appropriate tool
4. Execute the tool
5. Receive the tool result
6. Use the result to generate a final answer

Unlike a simple chatbot, an agent can **take actions using external tools**.

### Example

User:

> What is 1250 multiplied by 24?

The agent identifies that a calculation is required.

```text
User Question
      ↓
Llama 3.2
      ↓
Decides Calculator Tool is required
      ↓
Calculator Tool
      ↓
30000
      ↓
Llama 3.2
      ↓
Final Answer
```

---

## 🔄 Agent Workflow

The complete workflow is:

```text
                 ┌──────────────────┐
                 │   User Question  │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │    Llama 3.2     │
                 │   AI Agent/LLM   │
                 └────────┬─────────┘
                          ↓
                Does the question
                 require a tool?
                    ↙          ↘
                  Yes           No
                   ↓             ↓
          ┌────────────────┐   Final Answer
          │ Select a Tool  │
          └───────┬────────┘
                  ↓
        ┌─────────────────────┐
        │                     │
        ↓                     ↓
┌───────────────┐     ┌─────────────────┐
│  Calculator   │     │    Wikipedia    │
│     Tool      │     │      Tool       │
└───────┬───────┘     └────────┬────────┘
        │                      │
        └──────────┬───────────┘
                   ↓
             Tool Result
                   ↓
             Llama 3.2
                   ↓
             Final Answer
```

---

## 🛠️ Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming language         |
| LangChain  | LLM and tool integration     |
| LangGraph  | Agent workflow orchestration |
| Ollama     | Local LLM runtime            |
| Llama 3.2  | Large Language Model         |
| Streamlit  | Web application interface    |
| Requests   | Wikipedia API requests       |
| Wikipedia  | Factual information source   |

---

## 📁 Project Structure

```text
AI_Research_Agent/
│
├── agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── prompts.py
│   └── state.py
│
├── tools/
│   ├── __init__.py
│   ├── calculator_tool.py
│   └── wikipedia_tool.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📂 Project Components

### `agent/`

Contains the main agent implementation.

#### `agent.py`

Creates and runs the LangGraph-based AI agent.

It contains:

* Llama 3.2 configuration
* Tool binding
* LLM node
* Tool node
* Conditional routing
* LangGraph workflow
* Agent execution

#### `state.py`

Defines the state used by the LangGraph workflow.

The state stores the conversation messages as the agent moves through the workflow.

#### `prompts.py`

Contains the system prompt that defines the behavior of the AI research assistant.

---

### `tools/`

Contains the tools available to the AI agent.

#### `calculator_tool.py`

Provides mathematical calculation functionality.

Example:

```text
Input:
250 * 18

Output:
4500
```

#### `wikipedia_tool.py`

Uses the Wikipedia REST API to retrieve factual information.

Example:

```text
Input:
Artificial Intelligence

Output:
Wikipedia summary about Artificial Intelligence
```

---

### `app.py`

Provides the Streamlit user interface.

Users can enter a question and receive the agent's final response through the web application.

---

## 🔧 How Tool Calling Works

The agent uses Llama 3.2 with tool calling.

The model receives a question and decides whether one of the available tools should be used.

For example:

```text
Question:
What is 1250 multiplied by 24?
```

The model selects:

```text
calculator
```

The tool receives:

```text
1250 * 24
```

The tool returns:

```text
30000
```

The result is then passed back to Llama 3.2.

The model generates:

```text
The result of 1250 multiplied by 24 is 30000.
```

---

## 🔄 LangGraph Workflow

The agent workflow is implemented using LangGraph.

The graph contains two main nodes:

### LLM Node

Responsible for:

* Receiving the conversation
* Understanding the question
* Deciding whether a tool is required
* Calling the LLM

### Tool Node

Responsible for:

* Executing the selected tool
* Returning the tool result

The workflow follows:

```text
START
  ↓
LLM
  ↓
Tool Required?
  ├── No → END
  │
  └── Yes
       ↓
     TOOLS
       ↓
      LLM
       ↓
     END
```

This creates an agent loop where the LLM can use a tool and then continue reasoning from the tool result.

---

## 📚 Available Tools

### 1. Calculator

Used for mathematical operations.

Example questions:

```text
What is 250 multiplied by 18?

Calculate 1250 * 24

What is 4500 divided by 15?
```

---

### 2. Wikipedia Search

Used for general factual questions.

Example questions:

```text
What is Artificial Intelligence?

Who is Alan Turing?

What is Machine Learning?

What is Natural Language Processing?
```

---

## 💻 Installation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/greeshma078/AI_Research_Agent.git
```

Move into the project directory:

```bash
cd AI_Research_Agent
```

---

### Step 2 — Install Python Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama Setup

This project uses **Ollama** to run Llama 3.2 locally.

Install Ollama on your system and make sure it is running.

Then check the installed models:

```bash
ollama list
```

Make sure the following model is available:

```text
llama3.2
```

If the model is not available, run:

```bash
ollama pull llama3.2
```

---

## ▶️ Run the Agent

You can test the agent directly from the terminal.

From the project root:

```bash
python -m agent.agent
```

Example:

```text
============================================================

User Question:
What is Artificial Intelligence?

============================================================

Final Answer:
The term "Artificial Intelligence" was first coined in 1956 by John McCarthy...
```

---

## 🌐 Run the Streamlit Application

Start the web application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 🧪 Example Queries

### Calculator Example

```text
What is 1250 multiplied by 24?
```

Expected result:

```text
The result of 1250 multiplied by 24 is 30000.
```

### Wikipedia Example

```text
What is Artificial Intelligence?
```

The agent uses the Wikipedia tool and generates a response based on the retrieved information.

---

## 🎯 Project Objectives

This project was built to understand and demonstrate:

* Large Language Models
* Agentic AI
* Tool Calling
* LangChain
* LangGraph
* State-based workflows
* Local LLM deployment
* Function/tool execution
* Agent loops
* Streamlit application development

---

## 📈 Future Improvements

The project can be extended with additional tools and capabilities.

Possible improvements include:

* 🌐 Web Search Tool
* 📄 PDF Document Research
* 📊 Data Analysis Tool
* 🗄️ Database Query Tool
* 🧠 Conversation Memory
* 🔎 Multi-source Research
* 📝 Research Report Generation
* 📑 Citation Support
* 💬 Chat History
* ⚡ Streaming Responses
* 🧩 Additional specialized agents

---

## 🔐 Privacy

The LLM runs locally through Ollama.

No OpenAI API key or paid LLM API is required for the current implementation.

---

## ⚠️ Limitations

* Wikipedia search depends on the availability of the Wikipedia API.
* The current agent has only two tools.
* The application is designed as a local educational and portfolio project.
* Responses generated by the LLM may require verification for important factual information.

---

## 👩‍💻 Author

**Greeshma Reddy**

B.Tech — Artificial Intelligence & Data Science

GitHub:

https://github.com/greeshma078

---

## ⭐ Project Highlights

This project demonstrates a complete **Agentic AI workflow**:

```text
User
 ↓
Streamlit
 ↓
LangGraph
 ↓
Llama 3.2
 ↓
Tool Selection
 ↓
Calculator / Wikipedia
 ↓
Tool Result
 ↓
Llama 3.2
 ↓
Final Answer
```

Built using **Python + LangChain + LangGraph + Ollama + Llama 3.2 + Streamlit**.
