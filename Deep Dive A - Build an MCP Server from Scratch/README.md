# Deep Dive A · Deep dive A: build an MCP server from scratch

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/UQZCd-izZZI) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch%20-%20transcript.txt) [![Lab](https://img.shields.io/badge/open-lab-orange)](lab/)

<a href="https://youtu.be/UQZCd-izZZI"><img src="thumbnail.png" width="560" alt="Watch Deep Dive A: Deep dive A: build an MCP server from scratch"></a>

**Length:** 20:30 · **For:** Builders · **Classroom version:** 120 minutes

The Model Context Protocol (MCP) changed in July 2026, and most tutorials are now out of date. In this deep dive from the Kinvecta AI training series, we build a small MCP server, ticket-desk, from scratch on the current spec and the version-two SDKs, and we build it the DevSecOps way: security at every step, not bolted on at the end.

## What you'll learn

- How MCP works: host, client and server, and the trust boundaries between them
- What a request looks like on the wire today (spec 2026-07-28: no handshake, no sessions, server/discover)
- Tools, resources and prompts, and who controls each one
- The anatomy of a tool definition, and why descriptions must be reviewed like code
- A read-only tool in Python, where type hints become the schema
- An action that asks a person first, and the decline-and-cancel bug to avoid (Python and TypeScript)
- stdio vs Streamable HTTP, and where a server should run: local, remote, or in a container behind a firewall
- Testing with the MCP Inspector, and snapshotting the tool list in CI
- Connecting to Claude Desktop, Claude Code and VS Code
- Remote sign-in with OAuth 2.1, and why token passthrough is forbidden
- Real threats (tool poisoning, rug pulls, injection in results, malicious packages, DNS rebinding) and the server-side control for each
- A DevSecOps loop for the whole life of a server

## Rule of thumb

> **Few tools, tight schemas. A person confirms every action. Validate your own token. Never pass it on.**

## Chapters

- 0:00 Welcome: build a server you can trust
- 0:37 What you'll be able to do
- 1:11 Why build it carefully
- 2:05 Host, client, server
- 2:59 The big picture: four layers, three trust boundaries
- 3:52 Tools, resources and prompts
- 4:34 Anatomy of a tool definition
- 5:12 One request on the wire today
- 6:03 Set up on the current SDKs
- 6:54 Python: a read-only tool in 16 lines
- 8:04 Python: an action that asks a person first
- 9:01 How the server asks: multi-round-trip requests
- 9:59 TypeScript: the decline fix
- 10:51 stdio vs Streamable HTTP
- 12:01 Where an MCP server runs
- 12:50 Build, inspect, break, fix
- 13:42 Connect it to a host
- 14:31 OAuth 2.1, and why no token passthrough
- 15:44 Threats and server-side controls
- 16:58 DevSecOps for an MCP server
- 17:54 The rule of thumb
- 18:10 Hands-on lab
- 19:23 Check your understanding
- 20:11 Next: containers, scanning and the CI/CD pipeline (Deep Dive B)

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Deep Dive A - Build an MCP Server from Scratch - transcript.txt`](transcript/Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch%20-%20transcript.txt) | The narration as text, with chapter times |
| [`lab/`](lab/) | The ticket-desk MCP server in Python and TypeScript, with tests |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Inmersi%C3%B3n%20t%C3%A9cnica%20A%20-%20Construye%20un%20servidor%20MCP%20desde%20cero/)
