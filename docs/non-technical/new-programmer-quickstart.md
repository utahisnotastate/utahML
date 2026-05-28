# New Programmer Quickstart

If you are new to coding, this guide helps you use utahML safely.

## Step 1: Write a clear function signature

```python
def square_numbers(values: list[int]) -> list[int]:
    ; wishes: return a list where each number is squared
    pass
```

## Step 2: Save with watcher active

Run:

```bash
py -m utah.lazarus --watch .
```

Then save your file. utahML attempts to generate the function body.

## Step 3: Verify before trusting

- Read the generated code.
- Run your script.
- Add a tiny test input and check output.

## Good Wish Writing

- Be specific about input and output.
- Mention edge cases.

Good:
- `; wishes: return 0 when input list is empty`

Too vague:
- `; wishes: make this better`

## Common Beginner Mistakes

- Forgetting type hints.
- Asking for too many things in one wish.
- Skipping tests after generation.
