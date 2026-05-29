# Migration Guide: ESLint/Prettier/Lint-Only to Active Synthesis

Traditional lint stacks are excellent for detection. utahML adds correction and intent execution.

## Mental Model Shift

- Before: "Detect and block."
- After: "Detect, synthesize, validate, then write."

## Feature Comparison

- Operational stance
  - Lint-only: reactive validation
  - utahML: active in-place synthesis + validation
- Context scope
  - Lint-only: rule-bound token checks
  - utahML: nearby source context harvesting
- Resolution path
  - Lint-only: manual fix
  - utahML: auto-generated patch with AST gate

## Migration Steps

1. Keep your linter initially (do not remove on day one).
2. Add utahML watcher in a small pilot directory.
3. Enforce commit review on generated changes.
4. Expand scope by module once confidence is high.
5. Optionally reduce strict blocking hooks after proving stability.

## Recommended Hybrid Phase

- Keep formatting and import order tools.
- Let utahML handle intent-driven function rewrites.
- Keep CI tests as final source of truth.

## Common Pitfalls

- Turning watcher on for entire monorepo too early.
- Writing vague wishes.
- Skipping generated diff review.

## Safe Rollout Template

- Week 1: single module pilot.
- Week 2: two high-churn modules.
- Week 3: project-wide dev-only enablement.
- Week 4+: policy decision for staging/production usage.

## Broader AI/ML comparisons

For how utahML compares to conventional training, RAG, agents, and orchestration (not only linters), see `docs/technical/conventional-vs-utahml.md`.
