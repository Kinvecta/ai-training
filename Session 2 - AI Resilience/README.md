# Session 2 · AI resilience: switch models and vendors without rebuilding

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/BnhkCMgtz7A) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Session%202%20-%20AI%20Resilience%20-%20transcript.txt)

<a href="https://youtu.be/BnhkCMgtz7A"><img src="thumbnail.png" width="560" alt="Watch Session 2: AI resilience: switch models and vendors without rebuilding"></a>

**Length:** 8:41 · **For:** Everyone · **Classroom version:** 90 minutes

Models retire, vendors change their terms, and approvals shift. Session 2 of the Kinvecta AI training series shows how an organization stays "agnostic": able to swap the model, or the whole vendor, without rebuilding its work.

## What you'll learn

- What you rent (models, apps, harnesses) vs. what you own
- The four kinds of switch: model version, vendor, endpoint, harness
- The seven foundations an organization owns: approved MCP tools, containers, scanning, skills, code packages, a multi-vendor API layer, and stored evals
- How a model switch becomes a one-line configuration change
- How evals catch model drift and use-case drift
- The switching playbook: no evals, no switch

## Rule of thumb

> **Rent the model. Own the connections. Own the know-how. Own the proof.**

## Key ideas

- The model you use today will not be the model you use next year. Models retire, terms change and approvals change, on the vendor's schedule, not yours.
- Being agnostic means you can swap the model, or the whole vendor, without rebuilding your work. It does not mean using every vendor, and a gateway alone does not get you there.
- A switch can happen at four levels: model version, vendor, endpoint and harness. Each is cheap only if prompts and evals are stored, the workflow layer is vendor-neutral, the endpoint lives in configuration, and tools and skills are portable.
- Seven foundations make a switch easy: approved MCP tools, containers, scanning, skills, code packages, a multi-vendor API layer and stored evals. Wherever you don't own one, that's where lock-in hides.
- Keep the model name and endpoint in configuration, with the version pinned (never "latest"), so a switch is a one-line change.
- Stored evals are your proof. They catch model drift (a new version answers differently) and use-case drift (the business, data or users change under an unchanged prompt). No evals, no switch.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Agnostic | Able to swap the model, or the whole vendor, without rebuilding the work. |
| Lock-in | Being unable to switch because prompts, tools, skills or tests are tied to one vendor. |
| Model version | A specific, named release of a model. Pin it so the model can't change under you. |
| Endpoint | The address your software calls to reach a model: the vendor's own API, a cloud provider, or an approved platform. Keep it in configuration. |
| Configuration | Settings kept outside the code, such as the endpoint, model version and prompt, so a change does not mean a rewrite. |
| MCP tools | Connections to your data built on the Model Context Protocol, usable by any harness that speaks MCP. |
| Skill | Know-how captured once as a folder of instructions, in an open format that most major harnesses read. Write once, test in each harness. |
| Eval | A stored test set for a prompt, skill or workflow, run on a schedule and on every change. How you know a switch worked. |
| Model drift | A new model version answers differently, and the eval score drops. Fix: pin the version and fix it in configuration. |
| Use-case drift | The business, data or users change while the prompt stays the same, and the score slides slowly. Fix: update the skill or prompt. |

## Try it

About 15 minutes. You need one workflow you know well and a notepad. No sensitive data is needed; you are scoring how the work is built, not sharing its contents.

**Part A: score one real workflow (7 minutes)**

Pick one AI-assisted task you or your team runs every week. For each of the seven foundations, mark whether your organization owns it, a vendor owns it, or it is missing.

| Foundation | Owned | Vendor | Missing |
|---|---|---|---|
| 1. MCP tools (connections to your data) | | | |
| 2. Containers | | | |
| 3. Scanning | | | |
| 4. Skills | | | |
| 5. Code packages | | | |
| 6. API layer and configuration | | | |
| 7. Stored evals | | | |

**Part B: the 30-day scenario (8 minutes)**

Imagine the model behind that workflow is retired in thirty days. Write a one-line answer to each:

1. Where is the model named: in configuration, or in code?
2. Which evals would prove the new model works?
3. Which prompts or skills might need changes?
4. Who approves the switch?
5. What would make the next switch easier?

When you are done, name your single biggest gap. For most teams, it's evals.

## Check your understanding

1. In one sentence, what makes an organization agnostic?
   <details><summary>Answer</summary>It can swap the model, or the whole vendor, without rebuilding its work.</details>

2. Name four of the seven foundations.
   <details><summary>Answer</summary>Any four of: approved MCP tools, containers, scanning, skills, code packages, a multi-vendor API layer, stored evals.</details>

3. Why do stored evals matter most when you switch?
   <details><summary>Answer</summary>They're the only evidence the new model works as well as the old one. Without them, a switch is a guess.</details>

4. What is the difference between model drift and use-case drift?
   <details><summary>Answer</summary>Model drift: a new model version answers differently. Use-case drift: the business, data or users change while the prompt stays the same.</details>

5. Where should the model name and endpoint live?
   <details><summary>Answer</summary>In configuration, with the version pinned, not hard-coded.</details>

6. Why test a skill in each harness if the format is shared?
   <details><summary>Answer</summary>Scripts, file paths and tool names can differ between harnesses, so a skill can fail even though the format is shared.</details>

## Further reading

- [Model Context Protocol](https://modelcontextprotocol.io/): the open standard behind portable tool connections.
- [Agent Skills](https://agentskills.io/): the open format for skills as folders of instructions that many harnesses can read.
- [OWASP Top 10 for LLM Applications: LLM03 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/): why scanning and pinned packages belong in the foundations.
- Model deprecation schedules from two vendors, as examples of why versions must be pinned and switches planned: [Claude Platform model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [OpenAI API deprecations](https://developers.openai.com/api/docs/deprecations).

## Chapters

- 0:00 Welcome
- 0:27 What you'll be able to do
- 0:48 Why resilience matters
- 1:15 What "agnostic" means
- 1:51 Four kinds of switch
- 2:24 Four beliefs to correct
- 3:00 Seven foundations, one loop
- 3:50 Seven things you own
- 4:29 The one-line model switch
- 5:06 One skill, many harnesses
- 5:40 Evals catch drift
- 6:17 The rule of thumb
- 6:33 The switching playbook
- 7:05 Exercise: lock-in audit
- 7:43 Check your understanding
- 8:11 Next: safe prompting and verification (Session 3)

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Session 2 - AI Resilience - transcript.txt`](transcript/Session%202%20-%20AI%20Resilience%20-%20transcript.txt) | The narration as text, with chapter times |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Sesi%C3%B3n%202%20-%20Resiliencia%20en%20IA/)
