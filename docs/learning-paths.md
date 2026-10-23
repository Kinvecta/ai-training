# Learning paths

Ten videos, about 1 hour 42 minutes in total. You do not have to watch all of them. Pick the path that matches your role, watch in the order given, and close each session with its rule of thumb. Times are video length only; add reading the slides and transcript, and the master guide's check questions, if you want to retain it.

| Path | Who | Watch | Video time |
|---|---|---|---|
| [Everyone](#everyone) | Anyone who uses AI at work | Sessions 1–4 | about 34 min |
| [Automators](#automators) | People who automate work with AI, with or without code | Sessions 1–8 | about 1 h 2 min |
| [Builders](#builders) | Developers and platform engineers | Sessions 1, 5, 7, then Deep Dives A and B | about 1 h 5 min, plus the lab |
| [Leaders running a program](#leaders-running-a-program) | Managers, program leads, security and compliance | Sessions 1, 2, 3, 8, optionally 6 | about 34–41 min |
| [Trainers](#trainers) | People delivering the course in classroom slots | All ten, as 90- and 120-minute modules | about 16 h of classroom time |

The series follows five stages of AI use (1 safe everyday use, 2 the API in a container, 3 fixed workflows, 4 tool calling, 5 agents and skills). Everyone starts at Stage 1, and each path above stops at the stage its audience needs.

## Everyone

Stage 1: use AI safely for everyday work. No technical background needed.

| Order | Session | Length | You leave with |
|:--:|---|:--:|---|
| 1 | [What an LLM is, and the types of harnesses](../Session%201%20-%20What%20an%20LLM%20Is/) | 11:12 | The vocabulary: model, harness, chatbot, workflow, agent |
| 2 | [AI resilience](../Session%202%20-%20AI%20Resilience/) | 8:41 | Why to stay able to switch models and vendors, and what you own |
| 3 | [Safe prompting and verification](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) | 6:41 | The one rule, the briefing prompt, the verification checklist |
| 4 | [Tokens, context and how AI finds your data](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) | 6:59 | Why cost and "forgetting" happen, and how tools fetch your data |

Total: 33:33. If you only have ten minutes, watch Session 3.

## Automators

Stages 1 to 5 for people who will turn repeat tasks into workflows, connect tools, and use agents with guardrails. No coding required; Session 5 explains APIs and containers without code.

| Order | Session | Length |
|:--:|---|:--:|
| 1–4 | The [Everyone](#everyone) path | 33:33 |
| 5 | [APIs, endpoints and containers](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) | 6:07 |
| 6 | [Building workflows that don't break](../Session%206%20-%20Building%20Workflows/) | 7:04 |
| 7 | [Tools, MCP and prompt injection](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) | 7:35 |
| 8 | [Agents, skills and running the program](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) | 7:14 |

Total: 1:01:33. Suggested first project after Session 6: one weekly task that repeats, has the same shape every time, and already gets reviewed.

## Builders

For developers and platform engineers who will build MCP servers and ship AI workloads. If you already know the basics, start at Session 5; Session 1 is still worth it for the shared vocabulary the deep dives assume.

| Order | Session | Length |
|:--:|---|:--:|
| 1 | [What an LLM is, and the types of harnesses](../Session%201%20-%20What%20an%20LLM%20Is/) | 11:12 |
| 2 | [APIs, endpoints and containers](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) | 6:07 |
| 3 | [Tools, MCP and prompt injection](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) | 7:35 |
| 4 | [Deep Dive A: build an MCP server from scratch](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) | 20:30 |
| 5 | [Run the lab](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/): the ticket-desk server and its tests, in Python or TypeScript | about 15 min |
| 6 | [Deep Dive B: DevSecOps, containers, scanning and CI/CD](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) | 19:41 |

Total: 1:05:05 of video, plus the lab. The deep dives pair with each other: A builds the server, B boxes, scans, signs and ships it. Deep Dive B's [research brief](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/research-brief.md) lists the sources. Then go back for Sessions 2, 3, 4, 6 and 8 (about 37 min) to see what the people who use what you build are taught.

## Leaders running a program

For managers, program leads, and security or compliance reviewers who decide what the organization may do with AI and need to show that training worked.

| Order | Session | Length | Why |
|:--:|---|:--:|---|
| 1 | [What an LLM is, and the types of harnesses](../Session%201%20-%20What%20an%20LLM%20Is/) | 11:12 | Approve the harness, not just the model |
| 2 | [AI resilience](../Session%202%20-%20AI%20Resilience/) | 8:41 | What to own so a vendor change is not a rebuild |
| 3 | [Safe prompting and verification](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) | 6:41 | The one rule, the incident response when it is broken, who signs |
| 4 | [Agents, skills and running the program](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) | 7:14 | The five stages, the shared library, baselines and measures |
| (5) | [Building workflows that don't break](../Session%206%20-%20Building%20Workflows/) | 7:04 | Optional: what a safe first automation looks like, and the four numbers that prove it works |

Total: 33:48, or 40:52 with Session 6. Reviewers who sign off on infrastructure should add [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) (19:41).

## Trainers

Each video is written to expand into a classroom module: 90 minutes for Sessions 1–8, 120 minutes for the deep dives, which include hands-on work. Run the sessions in order; the stages build on each other.

| Module | Classroom slot | Audience |
|---|:--:|---|
| Sessions 1–4 | 4 × 90 min | Everyone |
| Sessions 5–8 | 4 × 90 min | People who automate work with AI |
| Deep Dive A (with the lab) | 120 min | Builders |
| Deep Dive B | 120 min | Builders and reviewers |

That is 16 hours in all: 6 hours for the everyone track, 12 hours through Session 8, and 4 more for the deep dives.

A 90-minute slot that works with the materials in this repository:

1. **Open** with the previous session's rule of thumb and one question from its check questions (5 min).
2. **Watch** the video together, or present from `slides.pdf` using the transcript as speaker notes (15–25 min).
3. **Discuss** the session's key points and where they show up in your organization (15 min).
4. **Exercise**: every session has one, named in its chapter list in the [master guide](../master-guide.pdf). Run it in pairs, on real but non-sensitive work (25–30 min).
5. **Check understanding** with the six check questions and model answers from the master guide (10 min).
6. **Close** with the rule of thumb and the bridge to the next session (5 min).

For the deep dives, replace the exercise with the hands-on part: the [MCP lab](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/) for A, and the find-the-problems-then-triage exercise plus the [research brief](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/research-brief.md) for B.

Before you teach:

- Watch the video and read the transcript yourself first.
- Check which AI tools your organization has approved for which data, so Session 3's one rule has concrete answers in your room.
- Ask people to bring one real, repeat task. It becomes the example in Sessions 3, 6 and 8.
- The whole series exists in Spanish in [`es/`](../es/), with its own slides, transcripts and master guide, for bilingual or Spanish-speaking groups.

The content is [CC BY 4.0](../LICENSE-CONTENT.md): you can present, adapt and share it with attribution.
