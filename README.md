## RAG (Retrieval Augmented Generation)

| Term | Description | Example |
| ----- | ----- | ----- |
| **LLM (Large Language Model)** | <ul><li>It uses layered neural networks (Transformers) to process data, while brains use complex biological neurons and circuits.</li><li>It is not a brain but acting more like a complex pattern-matching system trained on vast data.</li><li>The trained on massive text data</li><li>The understanding of natural language</li><li>It does not have memory</li></ul> | <p>**ChatGPT**</p><p>answering questions purely from its training data. E.g., “Explain quantum computing.”</p> |
| **RAG (Retrieval-Augmented Generation)** | <ul><li>AI framework that enhances Large Language Models (LLMs) by allowing them to retrieve real-time, specific information from external knowledge bases (like documents or databases) _before_ generating a response.</li><li>generating a response, making answers more accurate, up-to-date, and contextually relevant, without needing costly retraining of the core LLM.</li><li>Accesses current data not in the LLM's static training set.</li><li>Full model retraining for new knowledge base.</li></ul> | <ul><li>Using **LLM + Pinecone/FAISS **to answer company-specific policy questions. E.g., “What is our HR leave policy?” where the answer is retrieved from internal docs.</li><li>Accessing company policies and product info.</li><li>Retrieving relevant medical literature or patient history.</li></ul> |
| **Agent** | An LLM-based system that can perform multi-step actions, access tools, APIs, or databases, and decide what steps to take to complete a task. | <p>**AutoGPT or LangChain Agent**</p><p>booking flights: it searches websites, checks prices, and updates a calendar automatically.</p> |
**Summary:**

- LLM = language understanding/generation only.
- RAG = LLM + external knowledge retrieval.
- Agent = LLM + reasoning + actions/tools.

---

## Architecture
```python
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
```

---
