# cursor-sdk-modernizations

Legacy COBOL modules for the [cursor-sdk-migrations](https://github.com/dlamotta/cursor-sdk-migrations) field demo.

The SDK agent runs **in this repo** (`local.cwd`). Each Modernize job creates a `job/<uuid>` branch here; HITL merge lands on `main`.

## Fixtures

- `FEECALC.cbl` — maintenance fee on low-balance accounts
- `INTCALC.cbl` — interest calculation
- `MINBAL.cbl` — minimum balance rules

## Scratch

`jobs/<jobId>/` — per-run uploads from the demo UI (gitignored).

## Hooks

`.cursor/hooks.json` — fail-closed on git commands that touch `main`.

## Setup

Clone next to the demo repo (default path the demo expects):

```bash
cd ..
git clone git@github.com:dlamotta/cursor-sdk-modernizations.git
```

Or set `WORKSPACE_ROOT` in the demo's `.env` to this directory's absolute path.
