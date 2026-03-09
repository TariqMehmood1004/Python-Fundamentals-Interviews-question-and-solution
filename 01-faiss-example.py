"""
    System Flow (End-to-End)
-----------------------------------------
    User Query
        ↓
    Embedding Layer (query → vector)
        ↓
    Vector Store (FAISS similarity search)
        ↓
    Top-k Relevant Documents
        ↓
    LLM (OpenAI) → Prompt Construction
        ↓
    Generated Response
        ↓
    Output to User
"""

from dotenv import load_dotenv
load_dotenv()  # loads OPENAI_API_KEY from .env

# Import libraries
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS

# Define documents
documents = [
    "AI is transforming industries",
    "Python is widely used in AI"
]

# 1. Create embeddings
embeddings = OpenAIEmbeddings()

# 2. Create vector store
vector_stores = FAISS.from_texts(documents, embeddings)

# 3. Query
query = input("Enter your query: ")

# 4. Similarity search
docs = vector_stores.similarity_search(query, k=2)

# 5. Initialize the LLM
llm = OpenAI()

# 6. Generate response
context = docs[0].page_content
prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"


response = llm.invoke(prompt)
print(response)

