"""ticket-desk: a minimal MCP server (Python SDK 2.x)."""
import json
import logging
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from mcp.server import MCPServer
from mcp.server.mcpserver import AcceptedElicitation, Elicit, ElicitationResult, Resolve
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

log = logging.getLogger("ticket-desk")  # logging writes to stderr, never stdout

mcp = MCPServer(
    "ticket-desk",
    version="1.0.0",
    instructions="Help-desk tickets. Look tickets up before acting on them.",
)

# Stand-in for a real ticketing API
TICKETS: dict[str, dict] = {
    "TCK-1001": {"id": "TCK-1001", "title": "VPN drops every 30 min", "status": "open", "priority": "high"},
    "TCK-1002": {"id": "TCK-1002", "title": "Printer on 3rd floor offline", "status": "open", "priority": "low"},
}

TicketId = Annotated[str, Field(pattern=r"^TCK-\d{4}$", description="Ticket ID, e.g. TCK-1001")]


class Ticket(BaseModel):
    id: str
    title: str
    status: Literal["open", "closed"]
    priority: Literal["low", "medium", "high"]


# 1) Read-only tool -> structured output (outputSchema is generated from the return type)
@mcp.tool(
    title="Look up a ticket",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_ticket(ticket_id: TicketId) -> Ticket:
    """Return one help-desk ticket by ID. Read-only."""
    log.info("get_ticket %s", ticket_id)
    if ticket_id not in TICKETS:
        raise ToolError(f"No ticket {ticket_id}. Check the ID and try again.")
    return Ticket(**TICKETS[ticket_id])


# 2) Action tool that requires human confirmation (elicitation via a resolver)
class Confirm(BaseModel):
    confirm: bool = Field(description="Yes, close this ticket")


async def confirm_close(ticket_id: str) -> Elicit[Confirm]:
    """Resolver: always ask the human before closing."""
    return Elicit(f"Close ticket {ticket_id}? This notifies the requester.", Confirm)


@mcp.tool(
    title="Close a ticket",
    annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False
    ),
)
async def close_ticket(
    ticket_id: TicketId,
    resolution: Annotated[str, Field(min_length=5, max_length=500)],
    confirm: Annotated[ElicitationResult[Confirm], Resolve(confirm_close)],
) -> str:
    """Close a ticket with a resolution note. Asks the user to confirm first."""
    if ticket_id not in TICKETS:
        raise ToolError(f"No ticket {ticket_id}.")
    match confirm:
        case AcceptedElicitation(data=Confirm(confirm=True)):
            TICKETS[ticket_id]["status"] = "closed"
            log.info("AUDIT close_ticket %s resolution=%r", ticket_id, resolution)
            return f"{ticket_id} closed."
        case _:
            return f"{ticket_id} NOT closed: the user did not confirm."


# 3) Resource template: application-controlled context
@mcp.resource("tickets://{ticket_id}", mime_type="application/json")
def ticket_resource(ticket_id: str) -> str:
    """A ticket as JSON, for attaching as context."""
    return json.dumps(TICKETS.get(ticket_id, {}))


# 4) Prompt: user-invoked template (slash command in most hosts)
@mcp.prompt(title="Triage a ticket")
def triage_ticket(ticket_id: str) -> str:
    """Draft a triage plan for one ticket."""
    return (
        f"Use get_ticket to read {ticket_id}. Propose priority, owner team and next step. "
        "Do not close the ticket."
    )


if __name__ == "__main__":
    mcp.run()  # stdio by default
    # Remote: mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)  -> http://127.0.0.1:8000/mcp
