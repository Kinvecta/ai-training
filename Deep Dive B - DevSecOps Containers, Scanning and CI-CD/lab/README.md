# Lab: box it, scan it, triage it, ship it

Hands-on material for [Deep Dive B](../README.md). It takes the ticket-desk server from [Deep Dive A](../../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/) through the pipeline the video describes: a hardened image, several scanners, risk-based triage, and a signed digest. About 60 to 90 minutes with the tools installed.

Everything here is an example to learn from and adapt, not a drop-in product. Versions and majors were checked in October 2026 and will move.

| File | What it is |
|---|---|
| [`Dockerfile`](Dockerfile) | A hardened, annotated two-stage build of the Python ticket-desk server (Streamable HTTP) |
| [`.dockerignore`](.dockerignore) | Keeps secrets, caches, tests and git history out of the build context |
| [`Dockerfile.naive`](Dockerfile.naive) | The "find the problems" exercise from the video, as a file you can scan |
| [`ci-pipeline.yml.example`](ci-pipeline.yml.example) | An annotated GitHub Actions workflow: test, build, scan before push, sign the digest, attest, verify. Renamed so it does not run here |

## What you need

- Docker (or Podman with the `docker` alias) and the Deep Dive A lab folder.
- [Trivy](https://trivy.dev/latest/docs/), [Syft and Grype](https://oss.anchore.com/docs/) on your PATH. Each is a single binary, and each is also available as a container image; the commands below assume the binaries.
- Optional: [Cosign](https://docs.sigstore.dev/) for part 5, and `jq`.

Pin the scanners too. Install a specific version from the project's release page rather than "latest", and record it. In March 2026, a hijacked scanner action was the attack.

## Part 1: build the hardened image (15 min)

1. Copy `Dockerfile` and `.dockerignore` from this folder into the Deep Dive A `lab/` folder, next to `server.py`, `app.py` and `requirements.txt`.
2. Read the Dockerfile top to bottom. Every block has a comment saying what it prevents.
3. Pin the base by digest. Resolve the digest for the tag, then replace the `ARG BASE_IMAGE=` line with the pinned form:

   ```bash
   docker buildx imagetools inspect python:3.13-slim --format '{{json .Manifest.Digest}}'
   # ARG BASE_IMAGE=python:3.13-slim@sha256:<the digest you just printed>
   ```

   A digest pin means the build fails loudly if the base changes, instead of silently picking up different bytes. Tools such as Renovate or Dependabot can keep the pin current through pull requests.

4. Build, then run it published to localhost only and with a read-only root filesystem:

   ```bash
   docker build -t ticket-desk:dev --build-arg GIT_SHA=$(git rev-parse --short HEAD 2>/dev/null || echo local) .
   docker run --rm --read-only -p 127.0.0.1:8000:8000 ticket-desk:dev
   ```

5. In a second terminal, prove three things:

   ```bash
   # The server answers (Inspector CLI needs Node 22.19+)
   npx @modelcontextprotocol/inspector --cli http://127.0.0.1:8000/mcp --transport http --method tools/list
   # It runs as a non-root UID
   docker exec $(docker ps -q --filter ancestor=ticket-desk:dev) id
   # A forged Host header is refused (421), the DNS-rebinding guard from Deep Dive A
   curl -s -o /dev/null -w "%{http_code}\n" -X POST http://127.0.0.1:8000/mcp -H "Host: evil.example" \
     -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
     -d '{"jsonrpc":"2.0","id":1,"method":"server/discover","params":{}}'
   ```

6. Look at what is and is not in the image:

   ```bash
   docker history ticket-desk:dev            # one line per layer; no secrets, no "rm" of secrets
   docker inspect ticket-desk:dev --format '{{json .Config.Env}}'   # ENV is visible to anyone who can pull
   docker inspect ticket-desk:dev --format '{{.Config.User}}'       # 65532:65532
   ```

What this example does not do, on purpose, and what to do next in a real system: `python:3.13-slim` still contains a shell and a package manager. The next step up is a distroless or hardened base with no shell at all (the research brief compares the options), which cuts the CVE count further but makes debugging harder. Also add `pip-compile --generate-hashes` and `--require-hashes` so a substituted dependency cannot install.

## Part 2: scan it, three ways (15 min)

Different scanners look for different things. Run all three and compare.

```bash
# 1) Vulnerabilities in OS packages and Python libraries, failing on fixable HIGH/CRITICAL
trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 ticket-desk:dev

# 2) Secrets and misconfiguration inside the image (not just the code)
trivy image --scanners secret,misconfig ticket-desk:dev

# 3) The Dockerfile itself, before building
trivy config .

# 4) The inventory: an SBOM in CycloneDX, then Grype matching it against vulnerability data
syft ticket-desk:dev -o cyclonedx-json=sbom.cdx.json
grype sbom:./sbom.cdx.json
```

Things to notice:

- The SBOM is the inventory, not a verdict. Open `sbom.cdx.json` and count the components. Everything a scanner says is a match against this list, which is why an SBOM you can hand to a customer or an assessor is worth generating on every build.
- Grype's table sorts by a risk score and includes EPSS and, in the annotations column, `(kev)` for anything in CISA's Known Exploited Vulnerabilities catalog. That is the triage order from the video, built into the output. Try `grype sbom:./sbom.cdx.json --sort-by kev` and `--only-fixed`.
- Run the same scan a week later. New CVEs appear after you ship, which is why registries rescan stored images.

Now scan the naive Dockerfile and see how much a configuration scanner catches before an image is even built:

```bash
trivy config "<path to this folder>"
# If Trivy does not pick the file up by name, tell it the type explicitly:
trivy config --file-patterns "dockerfile:Dockerfile.naive" "<path to this folder>"
```

## Part 3: find the problems (12 min)

Open [`Dockerfile.naive`](Dockerfile.naive). Find at least eight problems and name a fix for each. Check the base tag, what is copied in, where the key lives, who the app runs as, the action pin, the order of push and scan, and what happens when the scan fails. Hint from the video: look hard at `|| true`.

<details>
<summary>Answers (at least ten)</summary>

| # | Problem | Fix |
|---|---|---|
| 1 | `FROM python:latest`: a moving tag, and a full image with compilers and tools | A minimal base pinned by digest |
| 2 | `COPY . /app` with no `.dockerignore`: `.env`, `.git`, keys and tests all land in a layer | Copy only what the runtime needs; add `.dockerignore` |
| 3 | Single stage: pip caches and build tools ship in the final image | Multi-stage build; copy only the virtual environment and code |
| 4 | Dependencies installed without pins or hashes | Pin exact versions and use `--require-hashes` |
| 5 | `ENV OPENAI_API_KEY=...`: a secret in the image config, visible with `docker inspect` to anyone who can pull | Inject at run time from a secrets manager; rotate this key now |
| 6 | `RUN rm /app/.env`: the file is still in the earlier `COPY` layer | Never copy it in; `.dockerignore` |
| 7 | No `USER`: the server runs as root | `USER 65532:65532`; in Kubernetes also `runAsNonRoot` |
| 8 | `trivy-action@master`: a moving branch, the exact pattern the March 2026 hijack exploited | Pin to a full commit SHA of a post-incident release |
| 9 | `docker push` runs before the scan | Build and load locally, scan, then push |
| 10 | `trivy ... \|\| true`: the scanner can never fail the build | Remove it; set `--exit-code 1` and let the gate work |
| 11 | Pushing and deploying `:latest`, nothing signed | Tag by commit, sign and deploy by digest |

</details>

## Part 4: triage by real risk (8 min)

A scan of a different image produced six findings. The policy is the one from the video: block anything on KEV, anything with EPSS of 0.1 or higher, and any fixable CRITICAL (CVSS 9.0 or higher). No fix available: a time-boxed exception with an owner. Not reachable: a VEX statement. These are illustrative numbers, not real CVEs.

| ID | CVSS | EPSS | KEV | Fix available | Note |
|---|---|---|---|---|---|
| A | 9.8 | 0.92 | yes | yes | |
| B | 9.1 | 0.01 | no | yes | |
| C | 7.8 | 0.03 | no | no | |
| D | 8.1 | 0.02 | no | yes | code never called |
| E | 5.3 | 0.01 | no | yes | |
| F | 7.5 | 0.61 | no | yes | |

Decide for each: block, exception, VEX, or backlog, and say why. Three should block.

<details>
<summary>Answer key</summary>

| ID | Decision | Why |
|---|---|---|
| A | Block | On KEV: being exploited now. Fix before anything ships. |
| B | Block | Fixable CRITICAL (9.1). Low EPSS does not override a fix you can apply today. |
| C | Exception | HIGH with no fix available. Write a time-boxed risk acceptance with an owner and an expiry, and watch for the patch. |
| D | VEX | The vulnerable code is never called. Record a `not_affected` statement with the justification, so the finding stops reappearing. A fix is still cheap here, so schedule it. |
| E | Backlog | MEDIUM, low EPSS, fixable. Fix in the normal cadence, usually by moving to a newer base. |
| F | Block | EPSS 0.61: very likely to be exploited soon, and a fix exists. Score is "only" 7.5, which is the point: exploitability beats severity. |

Blocked: A, B, F. Often the fastest way to clear B, E and F at once is a newer minimal base image.

To make D stick in the tools, write an OpenVEX document and pass it to the scanner: `grype --vex vex.openvex.json ...` or `trivy image --vex vex.openvex.json ...`. The statement names the product by digest, the vulnerability, the status `not_affected`, and a justification such as `vulnerable_code_not_in_execute_path`.
</details>

## Part 5: sign the digest and read the pipeline (15 min)

1. Get the digest. Tags move; this is the identity you sign and deploy:

   ```bash
   docker inspect ticket-desk:dev --format '{{index .RepoDigests 0}}'   # empty until pushed to a registry
   ```

   A digest exists once the image is in a registry. If you have one you can push to (a local registry is fine: `docker run -d -p 127.0.0.1:5000:5000 registry:2`), tag, push and read the digest from the push output.

2. Sign it with Cosign. Keyless signing uses your OIDC identity and records the signature in a transparency log; for a quick local test, a key pair also works:

   ```bash
   cosign generate-key-pair                      # local test only; CI uses keyless or a KMS-backed key
   cosign sign --key cosign.key 127.0.0.1:5000/ticket-desk@sha256:<digest>
   cosign verify --key cosign.pub 127.0.0.1:5000/ticket-desk@sha256:<digest>
   cosign attest --key cosign.key --type cyclonedx --predicate sbom.cdx.json 127.0.0.1:5000/ticket-desk@sha256:<digest>
   ```

   Change one byte in the image, rebuild, push: the new digest has no signature and verification fails. That is the whole idea.

3. Read [`ci-pipeline.yml.example`](ci-pipeline.yml.example) with the video's checklist: least privilege by default, every action pinned by full SHA, scan before push, sign the digest, attest the SBOM and provenance, verify. Note what is deliberately absent (listed at the bottom of the file), and that the tool-list snapshot gate from Deep Dive A sits in the `tests` job.

Questions to answer in your own words:

- Why does the workflow build the image twice (once with `load: true`, once with `push: true`) and why is that safe?
- Where would an attacker who controlled a tag of `trivy-action` get stopped in this workflow, and where would they succeed in `Dockerfile.naive`'s pipeline?
- Staging passed. What exactly gets promoted to production, and what must not happen on the way?

<details>
<summary>Suggested answers</summary>

- The first build stays on the runner so it can be scanned before anything reaches the registry; the second reuses the same cache, so the layers are identical, and only runs on a push to `main` after the gate passed. The signature is then attached to the digest that was actually pushed.
- Nowhere in this workflow: the action is pinned to a commit SHA, so a moved tag changes nothing. In the naive pipeline the moved `@master` tag runs the attacker's code with the job's token on the next run, and `|| true` would hide any error it caused.
- The same digest, by reference, with its signature and attestations verified at admission. It must not be rebuilt, retagged from a different build, or pulled by tag.
</details>

## Where this leaves you

You have built the same box once, scanned it with three tools, made risk-based decisions you can defend, and signed the exact bytes you scanned. The rule of thumb from the video covers all of it: pin everything, scan before it ships, sign it, and ship the same digest.

Back to [Deep Dive B](../README.md) · [Research brief](../research-brief.md) with the tool tables and sources · [Deep Dive A lab](../../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/)
