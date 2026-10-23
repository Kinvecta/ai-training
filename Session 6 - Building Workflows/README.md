# Session 6 · Building workflows that don't break

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/zAT5IMap_YI) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Session%206%20-%20Building%20Workflows%20-%20transcript.txt)

<a href="https://youtu.be/zAT5IMap_YI"><img src="thumbnail.png" width="560" alt="Watch Session 6: Building workflows that don't break"></a>

**Length:** 7:04 · **For:** Automators · **Classroom version:** 90 minutes

Pasting the same prompt every Monday? Session 6 of the Kinvecta AI training series shows how to turn a repeat task into a safe, fixed AI workflow: the same steps every run, a check on every output, and a person who approves before anything ships. No agents required.

## What you'll learn

- The difference between a chatbot, a workflow and an agent: who picks each step
- How far you can go with just chat plus an API (Stage 3: working automation)
- How to score a task to find a good first workflow
- The anatomy of a workflow: trigger, inputs, saved prompt, validation, review, delivery
- How validation catches bad output before it moves on
- How to run it safely: container, secrets, logs and cost limits
- Why a new prompt version is a new release, tested before it goes live
- Four numbers that prove a workflow is working

## Rule of thumb

> **Fix the path. Check every output. A person approves before it ships.**

## Key ideas

- Who picks each step tells the three apart. In a chatbot the person picks each step. In a workflow a designer fixes the path before it runs, and every run follows it exactly. In an agent the AI decides at run time.
- Chat plus an API is enough for Stage 3: working, containerized automation. You don't need agents to start.
- Score a task before you build: repeats weekly, same shape every time, a known-good output, already reviewed, approved data level, time you can measure. Four out of six is enough to start.
- A workflow has six fixed steps, including one check and one person: trigger, pull inputs, saved prompt, validate, human review, deliver. Every step writes to the audit log, and the script decides each step, not the model.
- Bad output is flagged, never passed on. One failed check routes the run to a person and nothing is delivered.
- A new prompt version is a new release, tested against known-good cases and one tricky case before it goes live. Prove it works with four numbers: time saved per run, errors caught in review, workflows in production, and reuse by other teams.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Chatbot | A person asks, reads, asks again and copies the result out. The person decides each turn. |
| Workflow | A path drawn before it runs. Every run follows the same steps: pull inputs, summarize, check, route. |
| Agent | The AI plans, acts and checks in a loop, deciding at run time. A person reviews afterwards. |
| Trigger | What starts a run, usually a schedule such as every Monday at 08:00. |
| Saved prompt | A versioned, reviewed prompt file in a shared location, loaded by the script rather than typed into each flow. |
| MCP server | A connector that pulls inputs or delivers results as a fixed step in the workflow. Session 7 covers it in detail. |
| Validation | Automatic checks on the output: format, required fields, unexpected links, recipients. One failure flags the run. |
| Human review gate | The step where a named person reads the output and signs off before delivery. |
| Test set | A handful of known-good cases plus one tricky case that every new prompt version must pass before release. |
| Baseline | How long the task took by hand before the workflow existed. Measure it first so you can prove the saving. |

## Try it

About 20 minutes with paper or a text file. Use a task you know well; no real data is needed.

**Part A: design it (10 minutes).** Pick one weekly task you or your team repeats, such as a status report. Fill in a workflow card:

| | Your answer |
|---|---|
| Trigger: when does it run? | |
| Inputs: where do they come from? | |
| Steps: which saved prompts, in what order? | |
| Check: what counts as bad output? | |
| Reviewer and delivery: who signs, and where does it go? | |

Example from the video: trigger Monday 08:00; inputs five reports pulled through a connector; step `status-summary-v2`; checks for fields and links; review by the team lead; delivery to the team inbox.

**Part B: break it (10 minutes).** Run these six scenarios against your design. For each one, does your workflow flag it or pass it on?

1. The input template changed.
2. One report is missing.
3. The output has an unknown link.
4. The model version was updated.
5. A report says "ignore your rules."
6. The run loops and keeps calling the model.

Anything that would pass silently is a missing check. Write the check you would add.

<details><summary>What a complete design catches</summary>

1 and 2: a required-fields check on the inputs or output flags the change. 3: a links check flags the unexpected address. 4: a pinned model version means this can't happen by surprise; a new version is a new release that runs the test set first. 5: the validation check flags unexpected links, recipients or actions, and the human review gate catches the rest; the tricky case in the test set catches it before release too. 6: a cost limit stops the run before a loop can run up the bill.

</details>

## Check your understanding

1. Who decides the steps in a workflow?

   <details><summary>Answer</summary>A designer, in advance. The script follows the same path every run.</details>

2. What can a team build with only chat and an API?

   <details><summary>Answer</summary>Scripted or low-code workflows that call the model through the API, with MCP servers as fixed steps. That's Stage 3.</details>

3. Name three signs of a good first workflow.

   <details><summary>Answer</summary>Any three of: repeats weekly, same shape every time, a known-good output, already reviewed, approved data level, time you can measure.</details>

4. What happens when a validation check fails?

   <details><summary>Answer</summary>The run is flagged and routed to a person. Nothing is delivered.</details>

5. Where should a workflow's prompts live?

   <details><summary>Answer</summary>As saved, versioned, reviewed files in a shared approved location, not typed into each flow.</details>

6. A report in the inputs says "ignore your rules." Which two parts of the workflow stop that from shipping?

   <details><summary>Answer</summary>The validation check, which flags unexpected links, recipients or actions, and the human review gate. The tricky case in the test set catches it before release, too.</details>

## Further reading

- [OWASP Top 10 for LLM Applications: LLM05 Improper Output Handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/). Why model output must be validated before anything downstream acts on it.
- [OWASP Top 10 for LLM Applications: LLM10 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/). The case for rate and cost limits on every automated run.
- [Google SRE book, chapter 8: Release Engineering](https://sre.google/sre-book/release-engineering/). The habits behind "a new version is a new release": repeatable builds, testing before rollout, and configuration kept under control.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). A vendor-neutral framework for governing, measuring and managing AI systems in production.

## Chapters

- 0:00 Welcome: three Mondays, one fixed path
- 0:34 What you'll be able to do
- 0:56 Why repeat work needs a fixed path
- 1:23 Chatbot, workflow or agent: who picks each step?
- 2:01 What you can build today
- 2:32 Score your first workflow
- 2:56 Anatomy of a workflow
- 3:36 Check every output
- 4:06 Run it safely: sealed in, logged, capped
- 4:32 Test it, then version it
- 5:01 Four numbers that prove it's working
- 5:16 The rule of thumb
- 5:31 Exercise: design it, then break it
- 6:12 Check your understanding
- 6:42 Next: tools, MCP and prompt injection (Session 7)

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Session 6 - Building Workflows - transcript.txt`](transcript/Session%206%20-%20Building%20Workflows%20-%20transcript.txt) | The narration as text, with chapter times |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Sesi%C3%B3n%206%20-%20C%C3%B3mo%20construir%20flujos%20de%20trabajo/)
