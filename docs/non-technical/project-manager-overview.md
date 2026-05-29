# Project Manager and Non-Technical Overview

This document explains the `; wishes` workflow in plain language.

## What Problem It Solves

Software teams spend time translating requirements into implementation. utahML shortens that gap by allowing intent to be written directly near code.

## How It Works

1. A developer writes a function and a line like:
   - `; wishes: add retry logic with exponential backoff`
2. On save, utahML detects the wish and generates code.
3. The generated patch is checked for Python syntax safety.
4. If valid, it is written to disk and tagged with:
   - `# [UTAH_HARDCORE_COMPLIANCE_PASS]`

## What This Means for Delivery

- Less manual boilerplate.
- Faster turnaround on routine enhancements.
- Better consistency when teams standardize wish phrasing.

## What It Does Not Replace

- Product requirements.
- Technical review.
- Testing and release approval.

## Recommended Team Policy

- Require pull requests for all generated changes.
- Track mutation logs in sprint retrospectives.
- Start with low-risk modules first.

## Further reading

- Documentation hub: `docs/README.md`
- How utahML compares to conventional AI/ML tooling (non-code summary in section 13): `docs/technical/conventional-vs-utahml.md`
