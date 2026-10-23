# Deep Dive B · DevSecOps: containers, scanning and CI/CD

[![Watch on YouTube](https://img.shields.io/badge/watch-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/zGLWpj00n3U) [![Slides](https://img.shields.io/badge/view-slides%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcript](https://img.shields.io/badge/read-transcript-lightgrey)](transcript/Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD%20-%20transcript.txt) [![Research brief](https://img.shields.io/badge/read-brief-blue)](research-brief.md) [![Lab](https://img.shields.io/badge/open-lab-orange)](lab/)

<a href="https://youtu.be/zGLWpj00n3U"><img src="thumbnail.png" width="560" alt="Watch Deep Dive B: DevSecOps: containers, scanning and CI/CD"></a>

**Length:** 19:41 · **For:** Builders and reviewers · **Classroom version:** 120 minutes

How do you ship software you can actually trust, and keep trusting it? This deep dive from the Kinvecta AI training series walks through DevSecOps for AI workloads end to end: what a container really is, where containers run, how to harden an image, where secrets belong, how scanning and triage work, how signing proves you shipped the same box you scanned, how the CI/CD pipeline enforces it all, and how firewalls fence it in, in both directions.

## What you'll learn

- DevSecOps: security in every stage, not one gate at the end (shift left, keep watching right)
- Images, containers, registries, and why the digest, not the tag, is the true identity
- Where containers run: laptop, single server, serverless containers, Kubernetes, edge and air-gapped, and who patches what
- How to harden a Dockerfile: minimal pinned base, multi-stage build, no secrets, non-root user
- Where secrets live: never in the image or repo; secrets managers, OIDC workload identity and runtime injection
- The kinds of scanning (secrets, SAST, SCA, IaC, image, SBOM, DAST) and the open-source and commercial tools for each
- Triage that works: KEV first, then EPSS, then fixable criticals, with VEX for what doesn't apply
- Signing, attestations and admission control (Cosign, SBOM, provenance, Kyverno)
- A real GitHub Actions pipeline, annotated, and why you pin actions by full commit SHA
- Firewalls and network controls: WAF, cloud firewalls, host firewalls, the Docker/ufw gotcha, NetworkPolicy and egress allow-lists
- AI-specific gates: pinned models and prompts, evals, MCP/skill scanning and egress control

## Rule of thumb

> **Pin everything. Scan before it ships. Sign it, and ship the same digest.**

## Chapters

- 0:00 Welcome: one box, trusted everywhere
- 0:33 What you'll be able to do
- 0:56 Three problems a good pipeline solves
- 1:33 DevSecOps: security in every stage
- 2:19 Image, container, registry and digest
- 3:06 Where containers run
- 4:05 Hardening the image
- 4:52 Reading a hardened Dockerfile
- 6:00 Where secrets live
- 6:58 A scanner at every station
- 7:47 Scanning tools by category
- 8:57 Triage: fix what's exploited first
- 10:01 Sign, attest, verify
- 10:52 Signing, registry, admission and runtime tools
- 11:51 The CI/CD line and its gates
- 12:41 A GitHub Actions pipeline, annotated
- 13:44 When the scanner is the attack
- 14:31 Firewalls: default deny, both directions
- 15:27 Network layers and the tools for each
- 16:42 AI-specific gates
- 17:23 The rule of thumb
- 17:38 Exercise: find the problems, then triage
- 18:27 Check your understanding
- 19:22 Wrap-up: build it, box it, ship it

## Key ideas

- DevSecOps means security in every stage, not one gate at the end: shift left, and keep watching right.
- An image is a sealed box; its digest is its true identity, while a tag can move. The same image runs on a laptop, a server, serverless containers, Kubernetes or the edge; who patches what changes, but your image, code, keys and network rules stay yours.
- Harden the image (minimal base pinned by digest, multi-stage build, non-root) and keep secrets out of images and repos: inject them at run time from a secrets manager.
- Use several scanners, then triage by real risk: actively exploited (KEV) first, then likely to be exploited (EPSS), then fixable critical and high.
- Sign and attest the digest, verify it at admission, and promote the same digest from staging to production. Pin CI actions to full commit SHAs, because your scanner is a dependency too.
- Firewalls: default deny in both directions, layer by layer. A Docker-published port bypasses ufw, and AI workloads should reach only the LLM API and approved backends through an egress allow-list.

## Key terms

| Term | Meaning |
|---|---|
| Image | A sealed, immutable bundle of your code, runtime and libraries, built once. |
| Container | An image running as an isolated process on a shared kernel. |
| Registry | Where images are stored and pulled from. |
| Tag | A movable label such as `:latest` or `:1.4`. It can point at different bytes tomorrow. |
| Digest | The `sha256:` hash of the exact image bytes. The true identity; sign it and deploy it. |
| Layer | The result of one Dockerfile step. Layers are permanent, so a secret deleted in a later step is still in an earlier one. |
| Multi-stage build | Build tools stay in a builder stage; only the result is copied into a minimal runtime stage. |
| Distroless, hardened base | A base image with no shell or package manager, so there is less to scan and less for an attacker to use. |
| SBOM | Software bill of materials: the inventory of every component in the image (SPDX or CycloneDX). |
| CVE | The public ID of a known vulnerability. |
| CVSS | A 0 to 10 score of how bad a vulnerability could be. |
| EPSS | The probability that a vulnerability will be exploited in the next 30 days (FIRST, updated daily). |
| KEV | CISA's catalog of vulnerabilities known to be exploited right now. Fix these first. |
| VEX | A machine-readable statement that a vulnerability does not affect your product, and why. |
| SAST, SCA, DAST | Scanning your own code, your dependencies, and the running application. |
| Signing (Cosign, Notation) | A tamper-evident seal on the digest proving who produced it. |
| Attestation, provenance | Signed statements attached to the digest: the SBOM, who built it from which commit, the scan result. |
| SLSA | Supply-chain Levels for Software Artifacts: graded requirements for build provenance (v1.2 adds a Source track). |
| Admission control | The gate at deploy time that refuses unsigned or unverified images (Kyverno, Gatekeeper, policy-controller). |
| Pin by SHA | Referencing a CI action by its full 40-character commit SHA instead of a movable tag. |
| OIDC workload identity | Short-lived credentials issued to a CI job or workload, instead of long-lived keys stored in CI. |
| Egress allow-list | Default-deny outbound traffic, then allow only the LLM API and approved backends by hostname. |
| `DOCKER-USER` chain | The iptables chain where host firewall rules must go to apply to Docker-published ports. |

## Check your understanding

Pause and answer in your own words, then open the answer.

<details>
<summary>1. Why sign and deploy by digest instead of tag?</summary>

A tag is a movable label; a digest is a hash of the exact bytes. It guarantees that what was scanned and approved is what runs.
</details>

<details>
<summary>2. A key was added in one step and deleted in the next. Is the image safe to publish?</summary>

No. Each step is a permanent layer, so the key is still there. Rotate it now, rebuild with run-time injection or build-secret mounts, and add secret scanning.
</details>

<details>
<summary>3. A scan shows 40 HIGH findings. What do you fix first?</summary>

KEV first, then high EPSS, then fixable critical and high, focusing on what actually runs. Document the rest with VEX. Often a newer minimal base image is the fastest fix.
</details>

<details>
<summary>4. Scanning versus signing: why do you need both?</summary>

Scanning checks the contents for known problems; signing proves identity and origin and that nothing was altered. Without signing someone can swap the box; without scanning you faithfully ship something vulnerable.
</details>

<details>
<summary>5. ufw denies incoming traffic, but a port published with <code>docker run -p</code> is still reachable. Why, and what are two fixes?</summary>

Docker publishes ports through its own NAT rules, which bypass ufw. Bind the port to localhost behind a reverse proxy, or put rules in the `DOCKER-USER` chain. Treat the cloud security group as the real perimeter and test from outside with nmap.
</details>

<details>
<summary>6. A scanner's GitHub Action was hijacked. Which two controls limit the damage?</summary>

Pin actions to full commit SHAs (and scanner images by digest), and keep CI least-privilege with short-lived OIDC credentials, minimal permissions and fast secret rotation.
</details>

## Further reading

- [NIST SP 800-190, Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final): the reference for image, registry, orchestrator, container and host risks and countermeasures
- [NIST SP 800-218, Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) and [SP 800-204D, supply chain security in DevSecOps pipelines](https://csrc.nist.gov/pubs/sp/800/204/d/final)
- [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [Sigstore documentation](https://docs.sigstore.dev/): provenance levels, keyless signing with Cosign, and verification
- [FIRST EPSS](https://www.first.org/epss/) and [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): the two inputs to risk-based triage
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) and [CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
- [Docker: packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/) (the ufw gotcha and the `DOCKER-USER` chain) and [GitHub: security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## In this folder

| File | What it is |
|---|---|
| [`slides.pdf`](slides.pdf) | The slides from the video, one page per slide |
| [`transcript/Deep Dive B - DevSecOps Containers, Scanning and CI-CD - transcript.txt`](transcript/Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD%20-%20transcript.txt) | The narration as text, with chapter times |
| [`research-brief.md`](research-brief.md) | The research brief behind the session, with sources |
| [`lab/`](lab/) | Hands-on: a hardened Dockerfile and `.dockerignore` for the Deep Dive A server, a scan-and-triage walkthrough with Trivy, Syft and Grype, the find-the-problems exercise with answers, and an annotated pipeline example |

Watch the whole series in order in the [YouTube playlist](https://www.youtube.com/playlist?list=PLQqgikRVyDAM). [Back to the course](../README.md#course) · [Versión en español](../es/Inmersi%C3%B3n%20t%C3%A9cnica%20B%20-%20DevSecOps%2C%20contenedores%2C%20escaneo%20y%20el%20pipeline%20de%20CI-CD/)
