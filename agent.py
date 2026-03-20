import asyncio
import os
import logging
from adk.agent import LLMAgent
from adk.mcp import McpToolset

# Expose the ReAct (Reason + Act) internal monologue
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger("adk")
logger.setLevel(logging.DEBUG)

async def main():
    print("\n[SYSTEM] Initializing ADK Enterprise Agent...\n")

    # Connect to the MCP server
    mcp_host = os.environ.get("MCP_HOST", "http://localhost:8080")
    mcp_toolset = McpToolset(
        server_name="transit-server",
        server_url=f"{mcp_host}/sse"
    )
    
    # Initialize the Agent
    agent = LLMAgent(
        model="gemini-2.5-pro",
        tools=[mcp_toolset],
        system_prompt="You are an autonomous transit agent. Always use tools to check live status and policies before taking action."
    )
    
    prompt = """
    I am travelling from Mumbai to Bengaluru today (User ID: 90210). 
    Please check my flight status. If it is delayed, check the refund policy to see what I am eligible for, 
    and if I am eligible for anything, go ahead and process that compensation for me.
    """
    
    print(f"[USER PROMPT]: {prompt.strip()}\n")
    print("--- 🧠 AGENT REASONING TRACE STARTED ---\n")
    
    # Execute the loop
    response = await agent.run(prompt)
    
    print("\n--- ✅ FINAL OUTPUT ---\n")
    print(f"Agent: {response.content}\n")

if __name__ == "__main__":
    asyncio.run(main())