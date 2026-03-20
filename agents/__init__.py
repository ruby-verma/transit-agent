import os
import logging
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset
# 🚨 Notice the new import path and new class name here:
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams

# Enable Debug Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger("adk")
logger.setLevel(logging.DEBUG)

# Connect to the MCP server via SSE using the updated params
mcp_host = os.environ.get("MCP_HOST", "http://mcp-server:8080")
mcp_toolset = MCPToolset(
    connection_params=SseConnectionParams(url=f"{mcp_host}/sse")
)

# Initialize the ADK Agent globally for the Web UI
root_agent = LlmAgent(
    name="transit_agent",
    model="gemini-2.5-flash", 
    tools=[mcp_toolset],
    instruction="""You are an autonomous transit agent. Follow these rules strictly:
    1. STATUS: To check delays, use the `check_transit_status` tool.
    2. POLICY: If a user asks about rules or compensation policies, you MUST use the `get_refund_policy` tool and recite the rules to them.
    3. ACTION: If a user asks to process a claim, you must first check their status, then check the policy to ensure they are eligible, and finally use the `process_compensation` tool."""
)