---
name: cobol-modernize
description: >-
  Modernize legacy COBOL (.cbl/.cob) into Java, Python, or C#, then add and run
  pytest for new Python modules. Use when converting, porting, or modernizing
  COBOL, writing jobs/*/ outputs, or when asked to modernize legacy banking
  modules. Applies to any and all files being modernized.
---

# COBOL modernize

## When to use

Apply this skill to **any and all files being modernized** from COBOL into Java, Python, or C#.

## Instructions

1. Read the full COBOL source (IDENTIFICATION through PROCEDURE DIVISION), including the comment banner at the top.
2. Inventory programs called, COPY books, files, WORKING-STORAGE, and paragraph flow.
3. Map types and I/O (PIC → native types; OPEN/READ/WRITE → clear equivalents or stubs).
4. Translate **behavior only** — same edge cases, rounding, and control flow. Do not invent business rules.
5. Write the modern module at the path the user/job specifies (typically beside the source under `jobs/<slug>/`).
6. Obey the project **copyright-headers** rule: upon creating a new file in the target language, add a Copyright header at the top of the file, and port over any comments in the header that may exist in the original file that is being modified.
7. Prefer clear names when intent is obvious; preserve numeric precision explicitly (e.g. `Decimal` / `BigDecimal` for money).
8. **After** the modernized source(s) exist, create pytest unit tests (see below), then run them and fix failures before finishing.

## Pytest (after every Python modernization)

When the target is **Python** (or any new `.py` was produced):

1. For **each** new modernized `.py` module, add a matching pytest file next to it (e.g. `feecalc.py` → `test_feecalc.py` in the same `jobs/<slug>/` directory).
2. Cover the COBOL-visible behavior (happy path + the important edge cases from the legacy logic). Do not invent business rules beyond the COBOL.
3. Prefer plain `pytest` + assertions; use `Decimal` where the module uses money/precision.
4. Run the tests from the workspace, e.g. `pytest jobs/<slug> -q` (or the paths you wrote).
5. If tests fail, fix the implementation or tests until they pass — still without changing the COBOL business rules.
6. Do this for **every** modernized Python file in the job, not only one.

For **Java** / **C#** targets, still modernize + copyright headers; add a minimal unit test project/file only if the user asks (pytest is Python-specific).

## Anti-patterns

- Do not “improve” fee/interest/min-balance formulas.
- Do not skip Copyright headers (see project rule).
- Do not ship Python modernizations without pytest coverage and a green `pytest` run.
- Do not add unrelated frameworks beyond pytest for Python demos unless asked.
