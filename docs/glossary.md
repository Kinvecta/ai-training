# Glossary

Plain-language definitions of the terms the course uses, in the sense the course uses them. Each entry links to the session that teaches it; the [master guide](../master-guide.pdf) has the key points and check questions for every session.

Sessions: [1](../Session%201%20-%20What%20an%20LLM%20Is/) · [2](../Session%202%20-%20AI%20Resilience/) · [3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) · [4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) · [5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) · [6](../Session%206%20-%20Building%20Workflows/) · [7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) · [8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) · [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) · [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/)

## Models and harnesses

| Term | Meaning | Taught in |
|---|---|---|
| **LLM (large language model)** | A trained engine that predicts and writes text one token at a time. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/) |
| **Memory (in an AI app)** | Notes the app saves and feeds back into the model later; the model itself remembers nothing between calls. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/) |
| **Harness** | The software around the model. It decides what the model can see and do, so the same model can be safe in one app and risky in another. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/) |
| **Six types of harness** | Chat assistants, AI built into tools, organization platforms or gateways, coding and agent tools, open-source agents, and your own software via the API. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/) |
| **Chatbot** | An AI system where the person picks each step. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/) |
| **Workflow** | An AI system where a designer fixes the steps in advance; the same path runs every time. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/), [Session 6](../Session%206%20-%20Building%20Workflows/) |
| **Agent** | An AI system where the model picks the steps at run time, within the limits the harness sets. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/), [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **Five stages of AI use** | 1 safe everyday use, 2 the API in a container, 3 fixed workflows, 4 tool calling, 5 agents and skills. Everyone starts at Stage 1; each stage adds one new risk. | [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |

## Staying able to switch

| Term | Meaning | Taught in |
|---|---|---|
| **Agnostic** | Able to swap the model, or the whole vendor, without rebuilding your work. | [Session 2](../Session%202%20-%20AI%20Resilience/) |
| **Seven foundations** | What makes a switch easy: approved MCP tools, containers, scanning, skills, code packages, a multi-vendor API layer and stored evals. | [Session 2](../Session%202%20-%20AI%20Resilience/) |
| **Eval (stored evaluation)** | A saved set of test inputs with known-good outputs. Your proof that a new model, or a changed prompt, still works. | [Session 2](../Session%202%20-%20AI%20Resilience/) |
| **Model drift** | A new model version answers differently to the same prompt. | [Session 2](../Session%202%20-%20AI%20Resilience/) |
| **Use-case drift** | The business, data or users change while the prompt stays the same. | [Session 2](../Session%202%20-%20AI%20Resilience/) |
| **Pinned version** | Naming an exact version (of a model, package, image or action) so nothing changes under you without a deliberate update. | [Session 2](../Session%202%20-%20AI%20Resilience/), [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |

## Safe everyday use

| Term | Meaning | Taught in |
|---|---|---|
| **The one rule** | Data only goes into a tool approved for that data's sensitivity level. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |
| **Data sensitivity level** | Your organization's classification of how private a piece of data is, which decides which tools may receive it. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |
| **Briefing prompt** | A prompt written like a briefing to a teammate: role, task, audience and format, plus the source material. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |
| **Verification checklist** | What to check before using a draft: sources, numbers, names and dates, quotes, what is missing, and tone and bias. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |
| **"AI drafts, a person signs"** | A named person is accountable for AI-assisted work, and reviews it before it is used. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |
| **Prompt library** | A shared, approved place for saved prompts: each a plain-text file with a header (name, purpose, owner, inputs, data level), a second person's review and test cases. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/), [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **Hallucination** | Fluent output that is wrong. Fluent is not correct, so check every claim. | [Session 3](../Session%203%20-%20Safe%20Prompting%20and%20Verification/) |

## Tokens, context and finding data

| Term | Meaning | Taught in |
|---|---|---|
| **Token** | The unit a model reads and writes: roughly four characters, about three quarters of an English word. Codes and numbers use more, and every vendor counts differently. | [Session 4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) |
| **Context window** | One fixed budget shared by everything the model sees: instructions, tools, history, documents, the question and the answer. | [Session 4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) |
| **Prompt caching** | Making a stable, repeated prefix (instructions, tool definitions, reference documents) cheap to re-send. | [Session 4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) |
| **Finder** | Any method that fetches data into the context: everything in context, semantic search, keyword search, agentic search, structured queries or multimodal retrieval. The model only sees what finders return. | [Session 4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) |
| **Search index** | A copy of your data arranged for fast lookup. It needs the same access rules and approvals as the source. | [Session 4](../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/) |

## Calling the model from code

| Term | Meaning | Taught in |
|---|---|---|
| **API** | The interface your own software uses to call a model directly, with no chat app in between. Your code becomes the harness. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) |
| **Endpoint** | The address your code sends requests to. Keep it in configuration, not hard-coded. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) |
| **Three front doors** | The three kinds of endpoint for the same model: the vendor's own API, a cloud provider's hosted version, and your organization's approved platform or gateway. Choose the door by its terms and approvals first. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) |
| **Six jobs your code owns** | What the chat app used to do: instructions, data handling, logging, keys and network, human review, and cost limits. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) |
| **Container** | A sealed box that runs your software with only what it needs, and can reach only approved addresses: "one way out". | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/), [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Egress allow-list** | A network rule that lets a container reach only named destinations, such as the approved model endpoint and tool servers. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/), [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Four run controls** | Secrets injected at run time from a secrets store, a pinned model version, an audit log of every run, and rate and cost limits. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/) |
| **Audit log** | A record of every run: what went in, what came out, who approved it. | [Session 5](../Session%205%20-%20APIs%2C%20Endpoints%20and%20Containers/), [Session 6](../Session%206%20-%20Building%20Workflows/) |

## Workflows

| Term | Meaning | Taught in |
|---|---|---|
| **Six fixed steps** | The anatomy of a workflow: trigger, pull inputs, saved prompt, validate, human review, deliver. Every step writes to the audit log. | [Session 6](../Session%206%20-%20Building%20Workflows/) |
| **Validation check** | An automatic test on every output that flags unexpected links, recipients, actions or formats. Bad output is flagged, never passed on. | [Session 6](../Session%206%20-%20Building%20Workflows/) |
| **Human review gate** | The step where a person approves before anything ships. | [Session 6](../Session%206%20-%20Building%20Workflows/), [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |

## Tools, MCP and prompt injection

| Term | Meaning | Taught in |
|---|---|---|
| **Tool calling** | The model asks for a tool; the harness decides whether to run it and returns the result as data. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **Read tool / action tool** | A read tool looks something up and can run freely from approved sources. An action tool sends, changes or deletes something and waits for a person. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **MCP (Model Context Protocol)** | The open standard for plugging tools into any harness. Build one server and a chat app, a workflow and an agent can all use it. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/), [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Host, client, server** | The three MCP roles: the AI app (host) holds a client that talks to a tool server. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Tools, resources, prompts** | The three things an MCP server offers: actions the model can call, data the app can read, and templates the user can pick. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/), [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Tool definition** | A tool's name, description, input schema and annotations. The model reads the name and description, the SDK enforces the schema, and annotations are only hints. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Prompt injection** | Instructions hidden in content the AI reads, aimed at making it do something its user did not ask for. Ranked the number-one risk for AI applications. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **Indirect prompt injection** | Instructions planted in content the AI reads later, such as a document, web page, email or record. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **Three ingredients of an attack** | Private data, untrusted content and a way out. Remove any one and the attack fails. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **Layered defenses** | No single control stops injection; together they do: treat content as data, least access, approval for actions, output validation, a container limited to approved endpoints, and line-by-line review of outside skills. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/) |
| **Least access (least privilege)** | Giving a tool, token or agent only the permissions its job needs. | [Session 7](../Session%207%20-%20Tools%2C%20MCP%20and%20Prompt%20Injection/), [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **stdio / Streamable HTTP** | The two MCP transports: stdio for one person on one machine, Streamable HTTP behind a gateway for teams. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Multi-round-trip request** | How a server asks a person something mid-call: it returns an input-required result, the client asks, and retries with the answer. Always handle no and cancel. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **Token passthrough** | Forwarding the token a client sent you to another API. Forbidden by the MCP spec: validate your own token and use your own credential downstream. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |
| **OAuth 2.1** | The sign-in standard remote MCP servers use to identify users and issue tokens meant for that server. | [Deep Dive A](../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/) |

## Agents, skills and the program

| Term | Meaning | Taught in |
|---|---|---|
| **Skill** | Packaged know-how the AI loads only when needed, like an onboarding guide. Only names and descriptions load up front. | [Session 1](../Session%201%20-%20What%20an%20LLM%20Is/), [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **"Treat every skill like code"** | Read it, scan it, pin the version, install from an internal registry, and decide who may install. | [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **Skill + tools + model** | One repeatable job: the skill brings the method, tools bring facts and actions, and the model fills the gaps with judgment. | [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **Guardrails** | The limits around an agent: it runs in a container, logs every step, and holds at the gate until a person approves anything that leaves. | [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |
| **Measures that training worked** | Time saved per task, errors caught in review, library reuse, workflows in production, security findings. | [Session 8](../Session%208%20-%20Agents%2C%20Skills%20and%20Running%20the%20Program/) |

## Shipping it: DevSecOps

| Term | Meaning | Taught in |
|---|---|---|
| **DevSecOps** | Security in every stage of building and running software, not one gate at the end: shift left, and keep watching right. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Image** | The sealed, read-only package a container is started from. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Digest** | The hash of an image's exact bytes: its true identity. A tag is a movable label; a digest is not. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Hardened image** | A minimal base pinned by digest, a multi-stage build, a non-root user, and no secrets baked in. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Secrets manager** | A service that holds keys and passwords and injects them at run time, so they never sit in images or repositories. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Scanning** | Checking code, dependencies, images and configuration for known problems, at every station of the pipeline. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Triage (KEV, EPSS, VEX)** | Ordering findings by real risk: actively exploited (KEV) first, then likely to be exploited (EPSS), then fixable critical and high; document the rest (VEX). | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Signing and attestation** | Proving who built an image and that nothing changed since: sign the digest, attach what you know about it, verify at admission. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **CI/CD pipeline** | The automated line that builds, tests, scans, signs and ships code, with gates that stop a bad change. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Pin actions to SHAs** | Referencing CI actions by full commit hash, because your scanner is a dependency too and a tag can be moved. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |
| **Default deny** | A firewall stance that blocks all traffic, in both directions, except what is explicitly allowed. | [Deep Dive B](../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/) |

Content: [CC BY 4.0](../LICENSE-CONTENT.md). © 2026 Mark D. Espinoza / Kinvecta.
