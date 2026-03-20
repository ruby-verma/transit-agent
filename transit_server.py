from mcp.server.fastmcp import FastMCP
import os

# Initialize the FastMCP server
mcp = FastMCP("Transit-Data-Server")

# 1. TOOL: Fetch live operational data
@mcp.tool()
def check_transit_status(origin: str, destination: str) -> dict:
    """Fetches real-time transit status including delay in minutes."""
    database = {
        ("Mumbai", "Ahmedabad"): {"status": "On time", "delay_minutes": 0, "transport": "Vande Bharat"},
        ("Mumbai", "Bengaluru"): {"status": "Delayed", "delay_minutes": 120, "transport": "Flight Indigo 6E-5234"}
    }
    return database.get((origin, destination), {"error": f"No active schedules found."})

# 2. RESOURCE: Deep knowledge integration (Business Rules)
@mcp.resource("policy://refunds")
def get_refund_policy() -> str:
    """Returns the official corporate refund and compensation policy for transit delays."""
    return """
    Transit Compensation Policy:
    - Delays under 60 minutes: No compensation.
    - Delays between 60 and 119 minutes: Eligible for a 500 INR food voucher.
    - Delays 120 minutes or more: Eligible for a full refund or free rebooking.
    """

# 3. TOOL: Take transactional action based on reasoning
@mcp.tool()
def process_compensation(user_id: str, compensation_type: str) -> str:
    """Files a claim for a voucher or refund based on established eligibility."""
    return f"SUCCESS: {compensation_type} processed for user {user_id}. Confirmation email triggered."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    mcp.run(transport="sse", port=port)