## Copyright

Copyright © 2026 Mitali Choubisa.

All rights reserved. This repository is shared for portfolio and interview purposes only.

# FolderMind

> Turn any local folder into an AI-powered knowledge base.

FolderMind is an AI-powered knowledge platform that transforms a local folder of documents into an intelligent, searchable knowledge base. It indexes files, performs semantic search, and answers questions using Retrieval-Augmented Generation (RAG). The platform also exposes MCP tools, enabling AI agents to interact with the knowledge base.

## Features

* AI-powered search over local documents
* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG)
* FastAPI REST APIs
* MCP Server for AI Agent integration
* Dockerized deployment

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
FastAPI APIs / MCP Server
```

## Tech Stack

* **Backend:** Python, FastAPI
* **AI:** RAG, Embedding Models
* **Search:** ChromaDB (Vector Database)
* **Data:** PyArrow
* **Storage:** PostgreSQL
* **Agent Integration:** MCP
* **Infrastructure:** Docker

## Future Enhancements

* Apache Iceberg
* Apache Airflow
* Kafka / RabbitMQ
* OpenTelemetry
* Kubernetes


