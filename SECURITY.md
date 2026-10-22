# Security policy

## Status

This repository is course material for the **Kinvecta AI Training** series. It is **not actively maintained**, has no supported versions and makes no security guarantees. Content and dependencies may be outdated, and dependencies may come to include known vulnerabilities. Review and scan anything you reuse.

## Reporting a vulnerability

Please do not open a public issue. Use GitHub's private reporting instead: go to the **Security** tab and choose **Report a vulnerability**. Reports are read on a best-effort basis, with no response or fix timeline.

## What the repository does to lower risk

- No secrets, credentials, personal data, audio or video are committed. Every push and pull request is checked with a Gitleaks scan of the full history.
- The lab's Python and npm dependencies are pinned and audited (`pip-audit`, `npm audit`) on every push and weekly. Dependabot raises alerts and update PRs for pip, npm and GitHub Actions.
- CodeQL scans the Python and TypeScript on every push and weekly.
- Third-party GitHub Actions are pinned to full commit SHAs, and workflows run with read-only tokens by default.

## Safe use of the lab

- ticket-desk is a teaching example with in-memory data. Run it over `stdio` for one user, or over HTTP on localhost only.
- Add authentication before any MCP server leaves your machine, validate tokens issued for your server, and never pass a client's token through to another API.
- Treat everything a tool returns as data, not instructions.
