from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# Initialize FastMCP with DNS Rebinding Protection disabled for Docker networking
mcp = FastMCP(
    "Transit-Data-Server",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False)
)

@mcp.tool()
def check_transit_status(origin: str, destination: str) -> dict:
    """Fetches real-time transit status including delay in minutes."""
    database = {
        ("Mumbai", "Ahmedabad"): {"status": "On time", "delay_minutes": 0, "transport": "Vande Bharat Express"},
        ("Mumbai", "Bengaluru"): {"status": "Delayed", "delay_minutes": 120, "transport": "Flight Indigo 6E-5234"}
    }
    return database.get((origin, destination), {"error": f"No active schedules found."})

@mcp.tool()
def get_refund_policy() -> str:
    """Returns the official corporate refund and compensation policy for transit delays."""
    return """
    Transit Compensation Policy:
    - Delays under 60 minutes: No compensation.
    - Delays between 60 and 119 minutes: Eligible for a 500 INR food voucher.
    - Delays 120 minutes or more: Eligible for a full refund or free rebooking.
    """

@mcp.tool()
def process_compensation(user_id: str, compensation_type: str) -> str:
    """Files a claim for a voucher or refund based on established eligibility."""
    return f"SUCCESS: {compensation_type} processed for user {user_id}. Confirmation email triggered."