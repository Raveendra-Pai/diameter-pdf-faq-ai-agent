import os
from fastmcp import FastMCP
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_chroma import Chroma

# Initialize FastMCP Server
mcp = FastMCP("Diameter-Specs-Server")

# --- CONFIGURATION  ---
PDF_PATH = "./data/pdfs/diameter.pdf"
DB_DIR = "./storage/chroma/doc_vector_db"

def get_db():
    embeddings = FastEmbedEmbeddings()
    # Build if not exists, otherwise load
    if not os.path.exists(DB_DIR):
        print("Initial build of Vector DB...")
        loader = PyPDFLoader(PDF_PATH)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=150)
        chunks = text_splitter.split_documents(documents)
        return Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_DIR)
    return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

# Shared DB instance
vector_store = get_db()
 
@mcp.tool()
def search_diameter_pdf(query: str) -> dict:
    """
    Search the Diameter.pdf technical documentation for specific measurements or standards.
    Returns relevant text chunks to help answer technical questions.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    docs = retriever.invoke(query)

    return {
        "query": query,
        "matches": [
            {
                "page": doc.metadata.get("page", 0) + 1,
                "text": doc.page_content
            }
            for doc in docs
        ]
    }


if __name__ == "__main__":
    mcp.run()