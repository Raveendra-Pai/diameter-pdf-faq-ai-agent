📌 **Project: Diameter PDF FAQ AI Agent (Local RAG + MCP)**

This repository contains a local-first AI agent that answers technical questions from the Diameter protocol PDF documentation.

**✅ Key Features**
- 📄 Load and process large Diameter PDF documents
- ✂️ Chunking with RecursiveCharacterTextSplitter
- 🧠 Embeddings using FastEmbedEmbeddings (CPU friendly)
- 🗂️ Vector search using ChromaDB
- 🤖 Answer generation using Mistral via Ollama
- 🔍 Accurate answers based only on retrieved PDF context
- 🧰 Optional MCP Server exposing retrieval as a reusable AI tool (search_diameter_pdf)
- 💻 Runs fully locally (no cloud dependency)

**🏗️ Architecture**

   <img width="672" height="452" alt="FAQ_Agent" src="https://github.com/user-attachments/assets/fcfd9c9d-925f-4748-96ae-7e3fd232c08b" />
 
 1. PDF → chunks → embeddings → Chroma DB
 2. Query → retrieve top-k relevant chunks
 3. Inject context into LLM prompt
 4. Generate grounded answer + page references

**🔌 MCP Mode (Tool-based Retrieval)**
- The project also supports splitting responsibilities:
- MCP server handles document retrieval
- Agent client uses the tool output + LLM for grounded answering

**🎯 Use Cases**
- Technical FAQ bot for internal docs
- Local AI assistant for telecom engineers
- Building scalable “tool-based RAG” systems with MCP


**⚙️ Setup & Run (Local RAG + MCP)**

✅ Prerequisites
Make sure you have these installed:
- Python 3.11 (Dont use latest python version)
- Ollama (for running Mistral locally)
- Git (optional, for cloning)

1️⃣ Clone the repo
 ```bash
 git clone https://github.com/Raveendra-Pai/diameter-pdf-faq-ai-agent
 cd diameter_pdf_faq_ai_agent
 ```

2️⃣ Create & activate virtual environment (Recommended)
For Windows (PowerShell) :
  ```bash
 python -m venv .venv
 .\.venv\Scripts\Activate.ps1
 ```

3️⃣ Install dependencies
 ```bash
 pip install -r requirements.txt
 ```

4️⃣ Install and run Ollama (Mistral)
 - Download and Install from the official Ollama website [https://ollama.com/download]
 - Start Ollama server by running this command 'ollama serve'
 - Keep this terminal running.
 - Pull Mistral model by running the command 'ollama pull mistral'
 - Test it by running the command 'ollama run mistral'

5️⃣ Run the project
 - Start the MCP-RAG Client (Main App)
   ```bash
      python main.py
   ```   
- You should see:
```bash  
--- Diameter MCP-RAG Agent Online (type 'exit' to quit) ---
Then ask questions like:
What is CCR stands for ?
what is the command code of CCA ?
```



