import os
from mcp.server.transport_security import TransportSecuritySettings
from server import mcp

hosts = os.environ.get("MCP_ALLOWED_HOSTS", "localhost:*,127.0.0.1:*").split(",")
app = mcp.streamable_http_app(
    transport_security=TransportSecuritySettings(allowed_hosts=hosts, allowed_origins=[]),
)
