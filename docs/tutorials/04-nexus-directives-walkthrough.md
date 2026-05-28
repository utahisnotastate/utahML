# Tutorial 4: Directives + Nexus Walkthrough

## Goal

Run a full intent-resolution cycle with `UtahSingularityNexus`.

## Steps

1. Execute:

```bash
py -m utah.core
```

2. Observe output:

- Assigned engine target (for example `UtahSynthesisEngine`).
- Processed data hash.
- Child-friendly blueprint text from directives wrapper.

## Custom payload example

```python
import numpy as np
from utah import UtahSingularityNexus

nexus = UtahSingularityNexus(trace_log_path="logs/nexus_telemetry.jsonl")
result = nexus.execute_unified_multimodal_cycle(
    {"intent": "language memory module", "data": np.random.rand(2, 8)}
)
print(result)
```

## Verify

- JSONL telemetry is created.
- Returned manifest includes `status`, `assigned_engine`, and `processed_data_hash`.
