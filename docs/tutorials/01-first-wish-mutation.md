# Tutorial 1: First `; wishes` Mutation

## Goal

Run a single in-place mutation and verify the compliance marker.

## Prerequisites

- Python installed.
- Dependencies installed from `requirements.txt`.

## Steps

1. Create a file named `demo.py`:

```python
def add_one(x: int) -> int:
    ; wishes: return x plus one
    pass
```

2. Run an autofix check:

```bash
py -m utah.lazarus --wishes
```

For this tutorial, use your own bridge or stub if needed.

3. Confirm output contains:

- generated function code
- `# [UTAH_HARDCORE_COMPLIANCE_PASS]`

## Verify

- File parses successfully.
- Function runs as expected.
- Mutation log appears in `logs/lazarus_mutations.jsonl`.
