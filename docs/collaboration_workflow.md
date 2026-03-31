# Collaboration Workflow: Getting Sandbox Work onto Your GitHub

This explains common ways users move agent-produced work from a sandbox into their GitHub repo.

## Short answer

Yes — if your environment is configured with GitHub credentials that can push to your repo, the agent can push to a feature branch and you can review via PR.

## Typical workflows

### Workflow A (best UX): Direct feature-branch push from agent environment

1. Configure the environment with GitHub auth (PAT/GitHub App/OAuth) with least privilege.
2. Agent pushes to `feature/...` branch (not `main/master`).
3. You review on GitHub and merge via PR.

**Pros:** Fast, normal GitHub review flow.
**Cons:** Requires credential setup in the agent runtime.

### Workflow B: Patch-based handoff (no push permissions needed)

1. Agent generates patch/diff.
2. You apply locally with `git apply` or `git am`.
3. You commit and push from your machine.

**Pros:** No remote credential sharing.
**Cons:** Extra manual step.

### Workflow C: Bundle/tar handoff (path-preserving file transfer)

1. Agent exports selected files as tarball.
2. You unpack in repo root.
3. You review/commit/push.

**Pros:** Preserves relative paths; simple to import.
**Cons:** Not commit-history preserving unless paired with patches.

## Recommended permission model

- Grant push only to feature branches.
- Keep branch protection on `main/master`.
- Require PR review before merge.
- Use short-lived or revocable credentials where possible.

## What most users do in practice

- If their tool supports GitHub integration: **Workflow A**.
- If not: **Workflow B** first, or **Workflow C** for quick file transfer.

## For your current case

Given you currently cannot see sandbox commits on GitHub, your practical choices are:

1. Enable GitHub push credentials in this environment so pushes can go to a feature branch, or
2. Use patch/tar transfer and push from desktop.

Both are standard and safe when done via feature branches + PR.
