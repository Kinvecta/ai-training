# Session 4 · Tokens, context and how AI finds your data

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/YGxlkAdf1RQ) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data%20-%20transcript.txt)

<a href="https://youtu.be/YGxlkAdf1RQ"><img src="thumbnail.png" width="560" alt="Watch Session 4: Tokens, context and how AI finds your data"></a>

**Length:** 6:59 · **For:** Everyone · **Classroom version:** 90 minutes

Why did the AI bill surprise you? Why did it forget what you said? Why couldn't it find the table? All three come down to what the model can see. Session 4 of the Kinvecta AI training series explains tokens, the context window, and the different ways AI tools fetch your data.

## What you'll learn

- What a token is, and why codes and numbers cost more
- The types of tokens (input, output, thinking, cached, image, tool, embedding) and what each costs
- What fills the context window, and why caching makes stable instructions cheap
- Why long chats get more expensive every turn
- The six ways AI finds your data: everything in context, semantic search, keyword search, agentic search, structured queries and multimodal retrieval
- How to match the right finder to your data, and why a search index is a security question

## Rule of thumb

> **Send less. Cache what's stable. Fetch with the finder that fits.**

## Key ideas

- A token is roughly four characters, about three quarters of an English word. Codes and numbers use more, and every vendor counts differently, so treat any count as an estimate.
- The context window is one fixed budget shared by everything: instructions, tools, history, documents, the question and the answer. What you send costs more than what you get back.
- Long chats get more expensive every turn because the whole conversation is re-sent. Caching makes the stable prefix cheap; when the topic changes, start a new chat.
- Tokens show up in your work six ways: cost, capacity, speed, rate limits, quality (a lean context beats a stuffed one) and swapping models.
- The model never searches on its own. It only sees what the finders return, so match the finder to the data: semantic and keyword search for prose, structured queries for tables and live records, multimodal retrieval for scans, agentic search for code.
- A search index is a copy of your data. It needs the same access rules and approvals as the source.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Token | The piece of text the model reads, writes and bills. About four characters, or three quarters of an English word. |
| Tokenizer | The vendor's rules for splitting text into tokens. Each vendor's is different, so counts are estimates. |
| Input and output tokens | Input is everything you send: instructions, tools, documents, history and the question. Output is the answer, priced higher and the main driver of wait time. |
| Context window | The one fixed budget per request that input and output share. When it fills, early turns get dropped. |
| Caching | Storing a stable prefix (system prompt, tool definitions, reference documents) so repeated reads are cheap. |
| Finder | Any method the harness uses to fetch your data and hand it to the model. The model reads what the finders return. |
| Semantic search | Finding passages by meaning across large amounts of prose. Weak on exact IDs and tables. |
| Keyword search | Finding exact names, IDs and codes. Weak on synonyms. |
| Structured query | Pulling exact records from tables and databases, so totals come from a query, not from the model reading rows. |
| Search index | A copy of your data prepared for fast searching, often stored elsewhere. It needs the same access rules as the source. |

## Try it

About 15 minutes. Use a prompt of your own that contains no sensitive data, and a token counter from an approved tool.

**Part A: count it (7 minutes)**

1. Paste one of your own non-sensitive prompts into an approved token counter (many AI tools and APIs offer one).
2. Note the input tokens and the expected output tokens.
3. Multiply tokens per run by how many times a month that prompt runs.
4. Ask: what would a shorter prompt, or caching the stable part, save?

If you have no counter to hand, estimate: divide the character count by four.

**Part B: find it (8 minutes)**

For each of these six questions, pick the finder that fits: everything in context, semantic search, keyword search, agentic search, structured queries or multimodal retrieval.

1. What's our policy on remote work?
2. Find ticket INC-20418
3. Total spend by vendor this year
4. What does the org chart slide show?
5. Where is the retry logic in our code?
6. Summarize this three-page brief

<details><summary>Suggested answers</summary>

1. Semantic search, often with keyword search alongside it, across the policy documents.
2. Keyword search: an exact ID.
3. Structured query: a total should come from a query, not from the model reading rows. If you picked semantic search, think again.
4. Multimodal retrieval, or a vision model reading the slide.
5. Agentic search over the live code files.
6. Everything in context: a three-page brief fits in the window, so paste it.

</details>

## Check your understanding

1. Roughly how much text is one token?
   <details><summary>Answer</summary>About four characters, or three quarters of an English word. Codes and numbers use more.</details>

2. Why do long chats cost more each turn?
   <details><summary>Answer</summary>Every turn re-sends the system prompt and the whole history.</details>

3. What shares the context window?
   <details><summary>Answer</summary>Everything sent, plus the answer: instructions, tools, history, documents, the question and the output.</details>

4. What does caching make cheaper?
   <details><summary>Answer</summary>A stable prefix that repeats, such as instructions, tool definitions and reference documents.</details>

5. Name three ways AI fetches data.
   <details><summary>Answer</summary>Any three of: everything in context, semantic search, keyword search, agentic search, structured queries, multimodal retrieval.</details>

6. Why is a search index a security question?
   <details><summary>Answer</summary>An index is a copy of the data, often stored elsewhere, so it needs the same access rules and approvals as the source.</details>

## Further reading

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020): the paper that introduced retrieval-augmented generation, the pattern behind most finders.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) (Liu et al., 2023): evidence that a lean context beats a stuffed one.
- [Hybrid search using vectors and full-text search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) (Microsoft Learn): one vendor's explanation of why semantic and keyword search work best together.
- [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) and [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (Claude Platform docs): one vendor's primary documentation of counting tokens and caching a stable prefix.
- [OWASP Top 10 for LLM Applications: LLM08 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/): why a search index needs the same access controls as the source.

## Chapters

- 0:00 Welcome: what can the model see?
- 0:30 What you'll be able to do
- 0:49 Three complaints, one root cause
- 1:16 What a token is
- 1:48 Types of tokens
- 2:19 The context window budget
- 2:52 Why long chats cost more
- 3:19 Six reasons tokens matter
- 3:46 How AI finds your data
- 4:23 Six ways AI fetches data
- 4:58 Match the finder to the data
- 5:25 The rule of thumb
- 5:37 Exercise: count it, then find it
- 6:14 Check your understanding
- 6:37 Next: APIs, endpoints and containers (Session 5)

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Session 4 - Tokens, Context and How AI Finds Your Data - transcript.txt`](transcript/Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data%20-%20transcript.txt) | The narration as text, with chapter times |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Sesi%C3%B3n%204%20-%20Tokens%2C%20contexto%20y%20c%C3%B3mo%20encuentra%20la%20IA%20tus%20datos/)
