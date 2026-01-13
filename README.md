📌 Project: Diameter PDF FAQ AI Agent (Local RAG + MCP)
This repository contains a local-first AI agent that answers technical questions from the Diameter protocol PDF documentation.

✅ Key Features
- 📄 Load and process large Diameter PDF documents
- ✂️ Chunking with RecursiveCharacterTextSplitter
- 🧠 Embeddings using FastEmbedEmbeddings (CPU friendly)
- 🗂️ Vector search using ChromaDB
- 🤖 Answer generation using Mistral via Ollama
- 🔍 Accurate answers based only on retrieved PDF context
- 🧰 Optional MCP Server exposing retrieval as a reusable AI tool (search_diameter_pdf)
- 💻 Runs fully locally (no cloud dependency)

🏗️ Architecture
 1. PDF → chunks → embeddings → Chroma DB
 2. Query → retrieve top-k relevant chunks
 3. Inject context into LLM prompt
 4. Generate grounded answer + page references

🔌 MCP Mode (Tool-based Retrieval)
- The project also supports splitting responsibilities:
- MCP server handles document retrieval
- Agent client uses the tool output + LLM for grounded answering

🎯 Use Cases
- Technical FAQ bot for internal docs
- Local AI assistant for telecom engineers
- Building scalable “tool-based RAG” systems with MCP
