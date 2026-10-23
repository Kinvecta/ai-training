"""ticket-desk starter: an empty MCP server for Part A of the lab (Python SDK 2.x).

The finished version is server.py. Use this file if you want to type the two tools
yourself while following the video, then compare with server.py.

Run it:            python starter.py              (stdio; it waits silently, which is correct)
List its tools:    npx @modelcontextprotocol/inspector --cli python starter.py --method tools/list
"""
import logging
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from mcp.server import MCPServer
from mcp.server.mcpserver import AcceptedElicitation, Elicit, ElicitationResult, Resolve  # noqa: F401 (used in step 2)
from mcp.server.mcpserver.exceptions import ToolError  # noqa: F401 (used in step 1)
from mcp.types import ToolAnnotations  # noqa: F401 (used in steps 1 and 2)

log = logging.getLogger("ticket-desk")  # logging writes to stderr, never stdout

mcp = MCPServer(
    "ticket-desk",
    version="0.1.0",
    instructions="Help-desk tickets. Look tickets up before acting on them.",
)

# Stand-in for a real ticketing API. Made-up tickets only.
TICKETS: dict[str, dict] = {
    "TCK-1001": {"id": "TCK-1001", "title": "VPN drops every 30 min", "status": "open", "priority": "high"},
    "TCK-1002": {"id": "TCK-1002", "title": "Printer on 3rd floor offline", "status": "open", "priority": "low"},
}

# The ID pattern is the schema: TCK, a hyphen, exactly four digits.
TicketId = Annotated[str, Field(pattern=r"^TCK-\d{4}$", description="Ticket ID, e.g. TCK-1001")]


class Ticket(BaseModel):
    id: str
    title: str
    status: Literal["open", "closed"]
    priority: Literal["low", "medium", "high"]


# Step 1: add get_ticket here.
#   - decorate with @mcp.tool(title=..., annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False))
#   - take ticket_id: TicketId and return a Ticket (the return type becomes the output schema)
#   - raise ToolError("No ticket ...") for an unknown ID, so the model gets a readable error, not a crash
#   - log with log.info(...), never print()


# Step 2: add close_ticket here.
#   - a Confirm model with one bool field, and a resolver that returns Elicit("Close ticket ...?", Confirm)
#   - parameters: ticket_id: TicketId, resolution (5 to 500 characters),
#     and confirm: Annotated[ElicitationResult[Confirm], Resolve(your_resolver)]
#   - only AcceptedElicitation(data=Confirm(confirm=True)) closes the ticket; anything else returns "NOT closed"


if __name__ == "__main__":
    mcp.run()  # stdio by default
