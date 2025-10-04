from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math":
            {
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio",
            },
            "weather":
            {
                "url":"http://localhost:8000/mcp",
                "transport":"streamable_http",

            }
            
        }

    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what's weather in nyc"}]}
    )

    print("Math response:",math_response["messages"][-1].content)


asyncio.run(main())


