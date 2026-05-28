# Data Scientist Guide

This guide is for practitioners who want faster iteration without building full software pipelines first.

## Why This Helps

- You can describe intent directly near the function.
- The framework generates implementation scaffolding quickly.
- You stay focused on experiment logic and validation metrics.

## Typical Workflow

1. Draft a function signature and desired return type.
2. Add a `; wishes:` line with a concrete requirement.
3. Save file while watcher is active.
4. Review generated code and run your notebook/script tests.

## Example

```python
def build_features(df):
    ; wishes: create lag features for columns sales and traffic over windows 1, 7, and 14, handle missing values with forward fill
    pass
```

After save, review the generated implementation and adjust if domain assumptions differ.

## Best Practices

- Add data-shape expectations in the wish text.
- Mention missing-value strategy explicitly.
- Mention performance constraints (for example: "must run under 1s on 1M rows").
- Keep transformations deterministic for reproducibility.

## Validation Checklist

- Does output schema match expectations?
- Are null handling and type casting correct?
- Is leakage avoided for time-series features?
- Are train/test boundaries respected?

## Telemetry Usage

Use JSONL logs to track:

- which wishes were applied,
- which files changed,
- whether mutation passed AST validation.

This can be useful for experiment traceability and governance.
