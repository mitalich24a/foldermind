## Copyright

Copyright © 2026 Mitali Choubisa.

All rights reserved. This repository is shared for portfolio purposes only.

# FolderMind

> Turn any local folder into an AI-powered knowledge base.

FolderMind is an AI-powered knowledge platform that transforms a local folder of documents into an intelligent, searchable knowledge base. It indexes files, performs semantic search, and answers questions using Retrieval-Augmented Generation (RAG).
## Features

* AI-powered search over local documents
* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG)
* FastAPI REST APIs
  
## Architecture

```text
Ingestion
    ↓
Embedding
    ↓
Vector Store

User Query
    ↓
QueryEmbeddingService
    ↓
Retriever
    ↓
SearchResults
    ↓
PromptBuilder
    ↓
Prompt
    ↓
LLM
    ↓
Answer
      ▼
FastAPI APIs
```

## Tech Stack

* **Backend:** Python, FastAPI
* **AI:** RAG, Embedding Models
* **Search:** ChromaDB (Vector Database)
* **Storage:** ChromaDB




