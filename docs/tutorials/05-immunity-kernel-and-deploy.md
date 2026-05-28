# Tutorial 5: Immunity Kernel + Deploy Bundle

## Goal

Use explicit self-healing routing and generate a hardware deployment bundle.

## 1) Explicit immunity kernel

```python
import utah

kernel = utah.ImmunityKernel(target_module="runtime_target.py")
```

This is optional (importing `utah` already enables daemon behavior), but explicit mode is useful when you want patch writes routed to a known file.

## 2) Start watcher for wish-driven mutation

```bash
py -m utah.lazarus --watch .
```

## 3) Build a deployment bundle

```bash
py -m utah.forge --deploy . --target m5stack --output-dir ../utah_deploy_out
```

Expected output includes:

- `status: DEPLOYED`
- `bundle_path`
- `launch_manifest` (`utah_hardware_launch.txt`)

## 4) Optional reactive hardware bridge

```python
from utah import OracleEyeBridge

bridge = OracleEyeBridge()
bridge.bind_intent("button_press", lambda payload: {"pressed": payload.get("value", 0) > 0})
print(bridge.process_hardware_frame({"intent": "button_press", "value": 1}))
```
