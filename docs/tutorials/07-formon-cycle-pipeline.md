# Tutorial 7: Unified Formon Cycle Pipeline

This tutorial runs the **single-call SOTA pipeline** that chains:

`ChronoBuffer` → `OntologicalManifold` → `HiveMind` → `AkashicResonanceMatrix`

## Prerequisites

- Python 3.9+
- `pip install -e .` from the repository root (or `pip install utahml`)

## Step 1 — Minimal cycle

```python
import numpy as np
from utah import UtahSingularityNexus

nexus = UtahSingularityNexus()
result = nexus.execute_formon_cycle(
    {
        "intent": "stabilize edge inference under latency budget",
        "data": np.random.rand(4, 32),
    },
    manifold_dimension=128,
    swarm_nodes=3,
)

print(result["status"])
print(result["geometry_energy"])
print(result["knowledge_manifest"])
```

## Step 2 — Inspect stage artifacts

The returned manifest includes keys such as:

| Key | Stage |
|-----|--------|
| `chrono_acausal` | ChronoBuffer akashic snapshot |
| `precipitated_signature` | Ontological collapse checksum |
| `geometry_energy` | Scalar energy from precipitation |
| `swarm_actions` | HiveMind synchronization output |
| `entangled_state_size` | Shared `EntanglementTensor` readout length |
| `knowledge_manifest` | AkashicResonanceMatrix text |
| `assigned_engine` | Directive resolver blueprint |

## Step 3 — CLI smoke test

From the repo root:

```bash
python -m utah.core
```

Look for `[FORMON CYCLE VERIFICATION COMPLETE]` in the output.

## Conventional equivalent

In a typical stack you would separately configure:

- a vector DB for retrieval,
- an agent framework for multi-step reasoning,
- a training or inference service,
- and observability exporters.

utahML collapses a **demonstration path** into `execute_formon_cycle`. For production accuracy, still validate on your data; see `docs/technical/conventional-vs-utahml.md`.

## Next steps

- Tutorial 6 (ZEO building blocks): `docs/tutorials/06-zeo-architect-patterns.md`
- Full comparison guide: `docs/technical/conventional-vs-utahml.md`
- Architecture map: `docs/ARCHITECTURE.md`
