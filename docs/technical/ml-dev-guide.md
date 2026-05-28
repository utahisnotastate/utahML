# Guide for Experienced AI/ML Engineers

This guide focuses on integrating utahML's intent-driven patching with model-centric workflows.

## What You Get

- Inline requirement capture with `; wishes`.
- Automatic in-place code synthesis on save.
- Context-aware mutation seeded from nearby project files.
- AST-enforced safety before file writes.

## Quick Integration

## 1) Build a model bridge

Your bridge must implement:

- `compute_matrix_delta(payload: str) -> str`

The return value must be valid Python code for the target function block only.

```python
class MyInferenceBridge:
    def compute_matrix_delta(self, payload: str) -> str:
        # Call your local model or hosted endpoint here.
        # Return plain Python source code only.
        return "def f(x: int) -> int:\n    return x * 2"
```

## 2) Run watcher

```python
from utah import LazarusWishFileWatcher, RepositoryContextHarvester

harvester = RepositoryContextHarvester(workspace_root=".")
harvester.ingest_local_environment()

watcher = LazarusWishFileWatcher(
    watch_paths=["."],
    inference_bridge=MyInferenceBridge(),
    context_harvester=harvester,
)
watcher.start(blocking=True)
```

## Prompt Design Notes

Use deterministic prompts with:

- explicit signature constraints,
- performance requirements,
- accepted libraries,
- style rules (docstrings, type hints, error handling).

Keep output strict:

- no markdown,
- no prose,
- only executable Python.

## Model Selection Tips

- Low latency local models for frequent save-time edits.
- Larger cloud models for complex refactors and architecture upgrades.
- Hybrid strategy: local-first, cloud fallback on parse failure.

## Suggested Test Strategy

- Unit tests for generated function behavior.
- Contract tests for function signature stability.
- Golden-file tests for repeatable wish transformations.
- Parse-gate tests that intentionally return malformed code.

## Practical Patterns

- Use narrow wishes:
  - Good: `; wishes: vectorize this loop with numpy and preserve exact output shape`
  - Bad: `; wishes: make everything better`
- Keep one wish per function block.
- Pair with small commits to isolate generated diffs.
