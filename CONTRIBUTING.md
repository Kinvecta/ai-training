# Contributing

Thanks for your interest. A few things to know before you open anything.

## This repository is not actively maintained

It is a snapshot of course material that accompanies a recorded video series. There is no roadmap, no release schedule and no support. Issues and pull requests are read on a best-effort basis and may not get a response. The videos cannot change, so the slides and transcripts stay as recorded.

## Reporting an error in the content

If a slide, transcript, README or the master guide says something wrong or out of date, open a [content error report](https://github.com/Kinvecta/ai-training/issues/new/choose). Say which file and where, what it says, what it should say, and a source if you have one. Keep reports factual and short.

Small fixes to the Markdown files (typos, broken links, outdated URLs) are welcome as pull requests. Keep them minimal and one topic per PR.

## Reporting a security problem

Do not open a public issue. Follow [SECURITY.md](SECURITY.md) and use GitHub's private vulnerability reporting.

## Changing or extending the material

Fork the repository. The licenses allow it:

- Course content (slides, transcripts, master guides, research brief): [CC BY 4.0](LICENSE-CONTENT.md). Adapt and share with attribution to Mark D. Espinoza / Kinvecta, and note what you changed.
- Code (the Deep Dive A lab): [MIT](LICENSE).

New sessions, translations into other languages, or a rewrite for your own organization belong in your fork, not here.

## What not to commit

- No secrets, API keys, tokens or credentials, including in examples or test fixtures.
- No personal data: names, email addresses, screenshots of real conversations or records.
- No internal documents from your organization.
- No audio or video files; the repository links to the videos instead.

CI runs a secret scan of the full history on every push and pull request, and a leaked secret in git history is permanent until the history is rewritten. If you commit one by mistake, rotate it first, then open an issue.

## Running the checks locally

The only code is the MCP lab. Before a pull request that touches it:

```bash
cd "Deep Dive A - Build an MCP Server from Scratch/lab"
python -m pytest -q
cd ts && npm ci && npm run typecheck && npm test
```

Workflows pin third-party actions to full commit SHAs. If you update one, update the version comment next to it.
