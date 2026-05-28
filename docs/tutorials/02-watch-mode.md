# Tutorial 2: Continuous Watch Mode

## Goal

Enable save-triggered auto-mutation in a target folder.

## Steps

1. Start watcher:

```bash
py -m utah.lazarus --watch .
```

2. In another terminal or editor tab, create `watched_example.py`:

```python
def safe_divide(a: float, b: float) -> float:
    ; wishes: return a divided by b and raise ValueError for b equal to zero
    pass
```

3. Save file and return to watcher output.

## Expected behavior

- Watcher logs a detected mutation.
- File gets rewritten.
- Compliance marker appended:
  - `# [UTAH_HARDCORE_COMPLIANCE_PASS]`

## Troubleshooting

- No mutation:
  - Ensure file extension is `.py`.
  - Confirm watcher path includes your file.
- Repeated mutations:
  - Ensure save events are not duplicated by external tools.
