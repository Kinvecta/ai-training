# Session 8 · Agents, skills and running the program

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/RnQR570l17k) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program%20-%20transcript.txt)

<a href="https://youtu.be/RnQR570l17k"><img src="thumbnail.png" width="560" alt="Watch Session 8: Agents, skills and running the program"></a>

**Length:** 7:14 · **For:** Automators and leaders · **Classroom version:** 90 minutes

Training only works when the work changes. In the final session of the Kinvecta AI training series, we put the pieces together: skills, tools and a model working as one repeatable job, agents with guardrails, a shared prompt and skill library, and how to roll the program out and prove it worked.

## What you'll learn

- What an AI skill is, how it loads in layers, and why it stays cheap
- Why every skill should be treated like code (read, scan, pin, internal registry)
- How a skill, tools and a model combine into one repeatable job
- How to put guardrails on an agent: a container, a step log, and a person who approves what leaves
- How a saved prompt becomes a reviewed, versioned skill in one shared library
- The five stages of an AI program, the new risk at each stage, and where each role stops
- How to measure whether training worked: baselines first, then count work, not courses

## Rule of thumb

> **Write it once, as a skill. Gate what leaves. Measure what changes.**

## Key ideas

- A skill is like an onboarding guide the AI loads only when needed. Only names and descriptions load up front, about 80 tokens each, so dozens can be installed cheaply. When a request matches one description, the full instructions load, then only the file it needs. A vague description means a skill that never fires.
- Treat every skill like code: read every file before it's installed, scan it, pin the version, install only from an internal registry, run skills with scripts in a container, and decide who may install before you turn them on.
- A skill brings the method, tools bring facts and actions, and the model fills the gaps with judgment. Same request, same steps, for anyone who runs it.
- An agent runs in a container, logs every step, and holds at the gate until a person approves anything that leaves. Review the steps, not just the answer.
- One shared library of prompts and skills feeds every chat, script and agent. A saved prompt becomes a skill when it has a name and description, steps, a template, test cases, a second person's review and a version.
- Everyone starts at Stage 1, and each stage adds one new risk. Training worked when the work changed: take baselines first, then measure time saved, errors caught, reuse and workflows in production.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Skill | A folder of instructions, templates and optional scripts that the AI loads only when a request matches its description. |
| Loads in layers | First only each skill's name and description; then the full instructions for the one that matches; then only the file it needs. |
| Description | The one or two sentences that decide when a skill fires. Vague descriptions never trigger. |
| Internal registry | Your organization's approved download shelf. Skills are installed from here, not from the open web. |
| Pin the version | Lock a skill or model to one known version so it changes only when you decide. |
| Agent | An AI that plans, acts and checks in a loop to finish a multi-step task, inside a container and under review. |
| Gate | The point where an action that would leave the system (send, write back, change a record) holds until a person approves it. |
| Step log | The record of each step an agent took, so a reviewer can check the path, not just the final answer. |
| Shared library | The one version-controlled home for prompts and skills that chat, scripts and agents all pull from. |
| Baseline | The measurement taken before training or automation starts, so you can show what changed. |

## Try it

About 20 minutes. You need paper or a text file and a prompt you already use often. Nothing in it should contain real names or data.

**Part A: package it (12 minutes).**

1. Name your prompt as a skill, and write a description that says when to use it (one or two sentences).
2. Write three requests that should trigger it, and two that shouldn't.
3. Test the description on its own. Give an AI assistant only the description and the five requests, and ask which ones it would trigger on. Or put the list away and come back to it tomorrow with fresh eyes.
4. Fix the description until all five come out right.

For homework, add the template and two test cases plus one tricky case, and ask a second person to review it before it goes into your library.

**Part B: plan the rollout (8 minutes).** For one real pilot, write down:

| | Your answer |
|---|---|
| The pilot workflow | |
| Which roles go to which stage | |
| Three measures, each with a baseline you can take this week | |
| The date you'll review the numbers | |

If any of your measures counts courses completed instead of work changed, swap it out.

<details><summary>Example measures from the video</summary>

Time per report, corrections in review, library reuse by other teams, and workflows in production. Track security findings too. Take the baseline before training starts, or there is nothing to compare against.

</details>

## Check your understanding

1. What loads before a skill is triggered?

   <details><summary>Answer</summary>Only each skill's name and description, about 80 tokens each.</details>

2. Which stage does everyone complete, and where do analysts stop?

   <details><summary>Answer</summary>Everyone completes Stage 1. Analysts stop at Stage 3.</details>

3. What do a skill, tools and a model each add?

   <details><summary>Answer</summary>The skill adds the method, the tools add facts, actions and checks, and the model adds judgment in the gaps.</details>

4. Where must a person approve an agent's work?

   <details><summary>Answer</summary>Before any action leaves the system: sending, writing back or changing a record.</details>

5. What makes a prompt ready for the library?

   <details><summary>Answer</summary>A plain-text file with a header, a second person's review, versioning, and test cases it passes.</details>

6. Name two measures that show training worked.

   <details><summary>Answer</summary>Any two of: time saved per task, errors caught in review, library reuse, workflows in production, security findings.</details>

## Further reading

- [Agent Skills: overview and specification](https://agentskills.io/). The open format for skills: a folder with a `SKILL.md` whose name and description load first, with full instructions loaded on demand.
- [OWASP Top 10 for LLM Applications: LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). Why agents need least access and a person at the gate.
- [OWASP Top 10 for LLM Applications: LLM03 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/). The risks of installing models, plugins and skills from untrusted sources.
- [ToxicSkills: a study of agent skills supply chain compromise](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub) (Snyk, 2026). The audit of a public skills registry referenced in the video, in which roughly a third of skills had a security flaw.
- [The Kirkpatrick Model](https://www.kirkpatrickpartners.com/the-kirkpatrick-model/). The standard four levels for evaluating training, from reaction to results. Measuring changed work is level 3 and level 4.

## Chapters

- 0:00 Welcome: putting the pieces together
- 0:26 What you'll be able to do
- 0:47 Three ways AI programs stall
- 1:16 How a skill loads in layers
- 1:45 Treat every skill like code
- 2:11 Skill + tools + model: one repeatable job
- 2:51 Agents with guardrails
- 3:25 One shared prompt and skill library
- 3:50 Five stages, one new risk each
- 4:32 Measuring what changed
- 5:08 The rule of thumb
- 5:21 Exercise: package it, then plan it
- 6:04 Check your understanding
- 6:31 Series complete: your next step

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Session 8 - Agents, Skills and Running the Program - transcript.txt`](transcript/Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program%20-%20transcript.txt) | The narration as text, with chapter times |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Sesi%C3%B3n%208%20-%20Agentes%2C%20skills%20y%20c%C3%B3mo%20dirigir%20el%20programa/)
