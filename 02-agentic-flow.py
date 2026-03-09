"""
    System Flow Diagram (Textual)
    -----------------------------
    User Input
        │
        ▼
        ┌───────────────────────┐
        │ Input Prompt (query)  │
        └───────────────────────┘
                │
                ▼
        ┌─────────────────────────────┐
        │ Agent (initialize_agent)    │
        │                             │
        │ - Receives query            │
        │ - Determines which tool(s)  │
        │   to use                    │
        └─────────────────────────────┘
                │
                ▼
        ┌─────────────────────────────┐
        │ Tool: search_documents()    │
        │                             │
        │ - Executes the function     │
        │ - Returns result string     │
        │   (e.g., "search results…") │
        └─────────────────────────────┘
                │
                ▼
        ┌─────────────────────────────┐
        │ LLM (OpenAI API)            │
        │                             │
        │ - Receives prompt + tool    │
        │   output                    │
        │ - Generates AI response     │
        │ - Handles reasoning &       │
        │   language processing       │
        └─────────────────────────────┘
                │
                ▼
        ┌─────────────────────────────┐
        │ Agent collects AI response  │
        └─────────────────────────────┘
                │
                ▼
        ┌─────────────────────────────┐
        │ Output to User              │
        │ print(f"[AI RESPONSE]: …")  │
        └─────────────────────────────┘
"""

from dotenv import load_dotenv
load_dotenv()  # loads OPENAI_API_KEY from .env

# Import libraries
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool


# Define documents
def search_documents(query):
    return "search results for " + query

# Define tools => Agent
tools = [
    Tool(
        name="Search",
        func=search_documents,
        description="useful for when you need to answer questions about current events"
    )
]

# Define LLM
llm = OpenAI()

# Initialize agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

# user query
query = input("Write the query: ")

# run
result = agent.run(query)

print(f"[AI RESPONSE]: {result}")