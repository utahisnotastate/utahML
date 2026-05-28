# Tutorial 3: Context-Grounded Mutation

## Goal

Use `RepositoryContextHarvester` to bias generation toward local project conventions.

## Example script

```python
from utah import (
    LazarusCodeSynthesizer,
    LocalInferenceStub,
    RepositoryContextHarvester,
)

harvester = RepositoryContextHarvester(workspace_root=".")
harvester.ingest_local_environment([".py"])

synth = LazarusCodeSynthesizer()
bridge = LocalInferenceStub()

context = harvester.search_contextual_signatures("tensor shape validation", depth_limit=3)
synth.process_source_file("target_module.py", bridge, context_blocks=context)
```

## Why this matters

- Promotes naming/style consistency.
- Reduces architectural drift.
- Improves generated patch relevance in larger repos.

## Verify

- Mutation still passes AST parse gate.
- Generated function matches nearby code style and patterns.
