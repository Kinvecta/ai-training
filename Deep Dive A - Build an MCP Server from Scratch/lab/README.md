# Lab: ticket-desk, an MCP server from scratch

The code from [Deep Dive A](../README.md). **ticket-desk** is a minimal help-desk MCP server, written twice: in Python (`mcp` SDK 2.x) and in TypeScript (`@modelcontextprotocol/server` 2.x). Both versions expose the same four things:

| Primitive | Name | What it shows |
|---|---|---|
| Tool (read-only) | `get_ticket` | A tight input schema (`TCK-` plus four digits), structured output, and a tool error for bad input |
| Tool (action) | `close_ticket` | An action that asks a person to confirm before it runs, and does nothing if they decline |
| Resource | `tickets://{ticket_id}` | A ticket as JSON, attached as context by the app |
| Prompt | `triage_ticket` | A user-invoked template that reads a ticket but never closes it |

The tickets live in memory, standing in for a real ticketing API.

## Python

Requires Python 3.10+.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q          # 6 tests, in-memory client, no network
python server.py             # run over stdio (what desktop and coding apps use)
uvicorn app:app --host 127.0.0.1 --port 8000   # Streamable HTTP at http://127.0.0.1:8000/mcp
```

`app.py` only accepts `localhost` and `127.0.0.1` Host headers by default. Set `MCP_ALLOWED_HOSTS` (comma-separated) if you put it behind a proxy, and add authentication before it leaves your machine.

## TypeScript

Requires Node 20+.

```bash
cd ts
npm ci
npm test            # end-to-end test through an in-memory HTTP transport
npm run typecheck
npm run stdio       # run over stdio
npm run http        # Streamable HTTP at http://127.0.0.1:3000/mcp
```

## Connect it to an AI app

Most MCP hosts take a JSON entry like this (use absolute paths; the exact file and key names vary by app, so check its docs):

```json
{
  "mcpServers": {
    "ticket-desk": {
      "command": "/absolute/path/to/lab/.venv/bin/python",
      "args": ["/absolute/path/to/lab/server.py"]
    }
  }
}
```

To inspect it without an AI app, use the MCP Inspector: `npx @modelcontextprotocol/inspector` (Node 22.19+), then connect to the stdio command or the HTTP URL.

## Safety notes

- Logging goes to stderr. On stdio, anything printed to stdout corrupts the protocol.
- `close_ticket` gets the person's confirmation from the client (elicitation), not from a model-supplied argument, so the model can't confirm on the person's behalf.
- Keep the HTTP server on localhost. Never pass a client's token through to another API.
- Versions are pinned to what the video used (October 2026) and are not kept current. Update and scan them before you reuse this code.
