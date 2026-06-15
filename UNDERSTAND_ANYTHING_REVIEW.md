# Understand-Anything Review Note

Reviewed: 2026-06-15
Repo: https://github.com/Egonex-AI/Understand-Anything

Short conclusion: usable later, but not worth installing immediately in this Codex frontend setup.

Key points:

- The project provides skills such as `understand`, `understand-dashboard`, `understand-chat`, `understand-diff`, `understand-explain`, `understand-onboard`, `understand-domain`, and `understand-knowledge`.
- The default Windows Codex installer links skills into `$HOME\.agents\skills`, while this frontend currently exposes skills from `$HOME\.codex\skills`.
- A plain install may therefore succeed but not become visible here unless the frontend also reads `.agents\skills`, or we create adapted junctions into `.codex\skills`.
- It requires Node and pnpm. Node is available locally; pnpm would need to be enabled through Corepack.
- The skill instructions are mostly Bash-oriented, so Windows/PowerShell use may require Git Bash, WSL, or manual command adaptation.
- The dashboard appears reasonably safe for local use: it binds to `127.0.0.1`, uses a random tokenized URL, and restricts file previews to files in the generated graph.
- Do not enable `--auto-update` initially. Its hook behavior is Claude-oriented and may not fit this Codex frontend.

If revisited:

1. Clone/install in a controlled location instead of piping the remote install script directly into PowerShell.
2. Enable pnpm with Corepack.
3. Junction selected skills into `$HOME\.codex\skills` or configure the frontend to read `$HOME\.agents\skills`.
4. Restart the Codex/frontend session so skills are rediscovered.
5. Start with a scoped run, for example `tools/`, not the full vault.
6. Add `.understand-anything/` to `.gitignore` unless graph output is intentionally committed.
