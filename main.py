import asyncio
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.prompts import ChatPromptTemplate

async def main():
    llm = ChatOllama(model="mistral", temperature=0, num_ctx=4096)
    
    client = MultiServerMCPClient({
        "diameter_server": {
            "command": "python",
            "args": ["./doc_mcp_server.py"],
            "transport": "stdio"
        }
    })

    tools = await client.get_tools()

    # pick tool by name
    search_tool = [t for t in tools if t.name == "search_diameter_pdf"][0]

    template = """<s>[INST] You are a strict technical documentation assistant.
Use ONLY the given context to answer.
If the answer is not present in the context, say: "I cannot find this in the PDF."

CONTEXT:
{context}

QUESTION:
{question} [/INST]</s>"""

    prompt = ChatPromptTemplate.from_template(template)

    print("\n--- Diameter MCP-RAG Agent Online (type 'exit' to quit) ---")

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() == "exit":
            break

        # ALWAYS fetch context from MCP tool
        context = await search_tool.ainvoke({"query": user_input})

        chain = prompt | llm
        response = chain.invoke({"context": context, "question": user_input})

        print("\nFAQ-Agent:", response.content)

if __name__ == "__main__":
    asyncio.run(main())
