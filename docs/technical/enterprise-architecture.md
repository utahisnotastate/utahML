# Enterprise Architecture Guide

This guide explains how to adopt utahML's self-healing and intent-driven mutation substrate in production engineering environments.

## System Model

The platform has three core operational loops:

1. Intent extraction
   - Parse function signatures followed by `; wishes: <intent>`.
   - Convert intent into a structured synthesis prompt.
2. Context grounding
   - Harvest adjacent source artifacts using `RepositoryContextHarvester`.
   - Inject local architectural context into the synthesis request.
3. Safe in-place mutation
   - Generate updated function implementation through a model bridge.
   - Validate full-file Python syntax via `ast.parse`.
   - Persist mutated content only after AST verification.

## Runtime Topology

- `LazarusWishFileWatcher`
  - Trigger source-file processing on save events.
  - Use watchdog observer where available.
  - Fallback to polling when watchdog is unavailable.
- `LazarusCodeSynthesizer`
  - Process each wish marker and patch in place.
  - Log mutation telemetry to JSONL.
- `HighDensityTelemetryLogger`
  - Persist operational metrics for review and alerting.

## Recommended Deployment Pattern

### Development tier

- Enable watcher on feature branches.
- Use a local inference bridge or deterministic stub.
- Keep strict code review for all auto-generated edits.

### Staging tier

- Run in non-blocking watch mode for selected directories only.
- Capture JSONL telemetry and aggregate into your observability stack.
- Add nightly replay tests over representative files with `; wishes`.

### Production tier

- Use controlled mutation windows and scoped paths.
- Require signed model bridge configuration.
- Enforce PR gates on all generated modifications.

## Governance and Controls

- Scope controls
  - Restrict watch roots to approved repositories.
  - Restrict extensions to `.py` unless explicitly approved.
- Change controls
  - Require branch-level review.
  - Snapshot files before mutation in high-risk projects.
- Security controls
  - Keep inference bridge credentials out of source control.
  - Log every mutation event (file, wish text, success/failure).

## Failure Modes and Mitigations

- Invalid generated code
  - Mitigation: AST parse gate aborts write.
- Recursive save loops
  - Mitigation: write-suppression markers in synthesizer.
- Context drift
  - Mitigation: refresh repository context before processing.
- Over-broad mutation scope
  - Mitigation: run watcher with explicit directory boundaries.

## KPI Suggestions

- Mutation success rate.
- Mean time from save to valid patch.
- Percentage of patches accepted without manual edits.
- Rollback frequency per module.
- Hotspot files with repeated `; wishes` churn.
