# New to Machine Learning Guide

Use utahML to move from idea to runnable ML-oriented code faster.

## Core idea

You describe behavior in plain language next to function signatures. The framework generates implementation candidates you can test and improve.

## Starter Pattern

```python
def normalize_features(x):
    ; wishes: normalize each feature column to zero mean and unit variance, avoid division by zero
    pass
```

## Learning Loop

1. Generate code from wishes.
2. Inspect the math.
3. Validate with toy arrays.
4. Add assertions and tests.
5. Iterate with a tighter wish.

## Suggested Beginner Exercises

- Feature scaling.
- Train/validation split helper.
- Batch creation utility.
- Basic evaluation metrics (accuracy, MAE, F1).

## Important Reminder

Generated code is a starting point, not scientific truth. Keep checking assumptions, metrics, and data quality.
