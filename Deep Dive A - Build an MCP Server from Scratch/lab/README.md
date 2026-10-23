# Lab: ticket-desk, an MCP server from scratch

The code from [Deep Dive A](../README.md). **ticket-desk** is a minimal help-desk MCP server, written twice: in Python (`mcp` SDK 2.x) and in TypeScript (`@modelcontextprotocol/server` 2.x). Both versions expose the same four things:

| Primitive | Name | What it shows |
|---|---|---|
| Tool (read-only) | `get_ticket` | A tight input schema (`TCK-` plus four digits), structured output, and a tool error for bad input |
| Tool (action) | `close_ticket` | An action that asks a person to confirm before it runs, and does nothing if they decline |
| Resource | `tickets://{ticket_id}` | A ticket as JSON, attached as context by the app |
| Prompt | `triage_ticket` | A user-invoked template that reads a ticket but never closes it |

The tickets live in memory, standing in for a real ticketing API. They are made up.

| File | What it is |
|---|---|
| `server.py` | The finished Python server (stdio by default) |
| `app.py` | The same server as a Streamable HTTP app for `uvicorn`, with Host-header checks |
| `test_server.py` | Six tests through an in-memory client, including the decline path in both protocol eras |
| `starter.py` | An empty server to start Part A of the video's lab from, if you want to type the tools yourself |
| `ts/` | The TypeScript version: `server.ts`, `stdio.ts`, `http.ts`, `test.ts` |
| [`exercises.md`](exercises.md) | Guided exercises that extend the server without touching the shipped code |

## Python

Requires Python 3.10+ (tested on 3.13).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q          # 6 tests, in-memory client, no network
python server.py             # run over stdio (what desktop and coding apps use); it waits silently
uvicorn app:app --host 127.0.0.1 --port 8000   # Streamable HTTP at http://127.0.0.1:8000/mcp
```

`app.py` only accepts `localhost` and `127.0.0.1` Host headers by default and answers anything else with `421 Misdirected Request` (the DNS-rebinding guard from the video). Set `MCP_ALLOWED_HOSTS` (comma-separated, for example `tickets.internal.example:*`) if you put it behind a proxy, and add authentication before it leaves your machine.

A plain `curl` to `/mcp` is rejected because every request must carry the protocol metadata; use the Inspector or the SDK client below instead.

## TypeScript

Requires Node 20+ (the Inspector needs 22.19 or newer, so 22 LTS is the simplest choice).

```bash
cd ts
npm ci
npm test            # end-to-end test through an in-memory HTTP transport
npm run typecheck
npm run stdio       # run over stdio
npm run http        # Streamable HTTP at http://127.0.0.1:3000/mcp
```

`http.ts` uses the SDK's Express helper, which also rejects unknown Host and Origin headers on localhost.

## Inspect it without an AI app

The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) needs Node 22.19 or newer. From this folder, with the virtual environment active:

```bash
# Web UI: opens a browser, connect to the stdio command or to an HTTP URL
npx @modelcontextprotocol/inspector python server.py

# CLI mode: list the tools (two), then call one, then call it with a bad ID
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
npx @modelcontextprotocol/inspector --cli python server.py --method tools/call --tool-name get_ticket --tool-arg ticket_id=TCK-1001
npx @modelcontextprotocol/inspector --cli python server.py --method tools/call --tool-name get_ticket --tool-arg ticket_id=TCK-9999
```

The bad-ID call prints a readable `isError` result and exits with code 5, which is what you want in a script. For the TypeScript server, run the same commands from `ts/` (after `npm ci`) with `npx tsx stdio.ts` in place of `python server.py`, or start `npm run http` and pass `http://127.0.0.1:3000/mcp --transport http` as the target. Add `--format json` when you want to pipe the result into `jq`.

`close_ticket` asks the person a question (elicitation). The CLI mode cannot answer questions, so it refuses that call; use the web UI, where a form appears, or the tests.

Without an operating-system keychain the Inspector stores secrets in an unencrypted file under `~/.mcp-inspector/`, so be careful on shared machines.

## Connect it to an AI app

Most MCP hosts take a JSON entry like this. Use absolute paths, because the host does not share your shell's `PATH` or working directory, and restart the app after editing. The exact file and key names vary by app, so check its docs.

Claude Desktop (`claude_desktop_config.json`, found under Settings, Developer, Edit Config):

```json
{
  "mcpServers": {
    "ticket-desk": {
      "command": "/absolute/path/to/lab/.venv/bin/python",
      "args": ["/absolute/path/to/lab/server.py"],
      "env": { "TICKET_API_TOKEN": "<from your secrets manager>" }
    }
  }
}
```

The `env` block is where a real server would get its credentials; ticket-desk does not read any, so you can leave it out.

Claude Code (local scope by default; `--` separates Claude's options from the server command):

```bash
claude mcp add --transport stdio ticket-desk -- /absolute/path/to/lab/.venv/bin/python /absolute/path/to/lab/server.py
claude mcp add --transport http ticket-desk-remote http://127.0.0.1:8000/mcp   # after starting uvicorn
```

VS Code (`.vscode/mcp.json` in the workspace; the top-level key is `servers`, and sandboxing is available on macOS and Linux):

```json
{
  "servers": {
    "ticket-desk": {
      "type": "stdio",
      "command": "/absolute/path/to/lab/.venv/bin/python",
      "args": ["/absolute/path/to/lab/server.py"],
      "sandboxEnabled": true
    }
  }
}
```

If the host says the server failed but it runs by hand, look at the host's log for the server's stderr: the usual causes are a relative path, a missing environment variable, or something printing to stdout.

## Safety notes

- Logging goes to stderr. On stdio, anything printed to stdout corrupts the protocol.
- `close_ticket` gets the person's confirmation from the client (elicitation), not from a model-supplied argument, so the model can't confirm on the person's behalf. Both versions end the call on a decline or cancel instead of asking again.
- Keep the HTTP server on localhost. Never pass a client's token through to another API.
- Versions are pinned to what the video used (October 2026) and are not kept current. Update and scan them before you reuse this code.

Next: [exercises.md](exercises.md) extends the server step by step, and [Deep Dive B](../../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) puts it in a container, scans it and ships it.
