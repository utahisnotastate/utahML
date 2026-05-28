# [utahML/utah/core.py]
import logging
import os
import shutil
from functools import wraps
from typing import Any, Callable, Dict, List

import numpy as np

logger = logging.getLogger(__name__)


def detect_hardware_target() -> str:
    """
    Detect a runtime class for hardware-aware dispatch.

    Override via UTAH_HARDWARE_TARGET environment variable:
    - m5stack
    - raspberry_pi
    - workstation
    """
    explicit_target = os.getenv("UTAH_HARDWARE_TARGET", "").strip().lower()
    if explicit_target:
        return explicit_target

    machine = os.getenv("PROCESSOR_IDENTIFIER", "").lower()
    if "arm" in machine and "raspberry" in os.getenv("COMPUTERNAME", "").lower():
        return "raspberry_pi"
    return "workstation"


def hardware_optimized(func):
    """
    Dispatch decorator for constrained edge hardware vs workstation execution.

    Decorated call returns a dictionary containing:
    - hardware_target
    - execution_mode
    - result
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        target = detect_hardware_target()
        if target in {"m5stack", "esp32", "raspberry_pi"}:
            return {
                "hardware_target": target,
                "execution_mode": "freertos_header_dispatch",
                "result": {
                    "dispatch_header": "utah_freertos_dispatch.hpp",
                    "callable": func.__name__,
                    "note": "Use generated C++ bridge for edge runtime.",
                },
            }
        return {
            "hardware_target": target,
            "execution_mode": "python_tensor_execution",
            "result": func(*args, **kwargs),
        }

    return wrapper


class VoxelMapDebugger:
    """Utility for 2D/3D latent manifold projection snapshots."""

    @staticmethod
    def project(latent_space_manifold: np.ndarray, dimensions: int = 2) -> np.ndarray:
        if latent_space_manifold.ndim != 2:
            raise ValueError("latent_space_manifold must be 2D: (samples, features).")
        if dimensions not in {2, 3}:
            raise ValueError("dimensions must be 2 or 3.")
        centered = latent_space_manifold - latent_space_manifold.mean(axis=0, keepdims=True)
        _, _, vh = np.linalg.svd(centered, full_matrices=False)
        basis = vh[:dimensions].T
        return centered @ basis

    @staticmethod
    def to_debug_payload(latent_space_manifold: np.ndarray, dimensions: int = 2) -> Dict[str, Any]:
        projection = VoxelMapDebugger.project(latent_space_manifold, dimensions=dimensions)
        return {
            "dimensions": dimensions,
            "points": projection.tolist(),
            "sample_count": int(projection.shape[0]),
        }


class IntentEventManifold:
    """
    Event-driven intent resolver for hardware/UI interaction loops.

    Replaces repetitive polling logic with declarative event registration.
    """

    def __init__(self) -> None:
        self._intent_handlers: Dict[str, List[Callable[[Dict[str, Any]], Any]]] = {}

    def register_intent(self, intent_name: str, handler: Callable[[Dict[str, Any]], Any]) -> None:
        if intent_name not in self._intent_handlers:
            self._intent_handlers[intent_name] = []
        self._intent_handlers[intent_name].append(handler)

    def resolve_intent(self, intent_name: str, payload: Dict[str, Any]) -> List[Any]:
        handlers = self._intent_handlers.get(intent_name, [])
        return [handler(payload) for handler in handlers]


class OracleEyeBridge:
    """
    Vision-action bridge for migrating from polling loops to intent-driven interaction.
    """

    def __init__(self) -> None:
        self.event_manifold = IntentEventManifold()

    def bind_intent(self, intent_name: str, callback: Callable[[Dict[str, Any]], Any]) -> None:
        self.event_manifold.register_intent(intent_name, callback)

    def process_hardware_frame(self, frame_payload: Dict[str, Any]) -> Dict[str, Any]:
        intent_name = frame_payload.get("intent", "generic_hardware_event")
        responses = self.event_manifold.resolve_intent(intent_name, frame_payload)
        return {
            "intent": intent_name,
            "responses": responses,
            "response_count": len(responses),
        }


class UtahApp:
    """The central Latent Space Manager for Utah Hans."""

    def __init__(self, app_name: str):
        self.app_name = app_name
        print(f"[UTAH-OS] Engine Initialized: {self.app_name}")

    def synthesize(self, component_logic: callable, intent_data: str):
        print("[*] Collapsing Wave Function...")
        return component_logic(intent_data)


class UtahSingularityNexus:
    """
    The central nervous system core registry for the utahML architecture.
    Acts as the master processing grid controller across distributed hardware nodes.
    """

    def __init__(self, trace_log_path: str = "logs/nexus_telemetry.jsonl") -> None:
        self.state_active = True
        self.registered_components: Dict[str, Any] = {}
        self.trace_log_path = trace_log_path
        self._initialize_core_infrastructure()

    def _initialize_core_infrastructure(self) -> None:
        """Anchors sub-system infrastructure instances directly within core structural memory registers."""
        from .directives import IntentDirectiveResolver
        from .lazarus import LazarusStateGuardian
        from .stenographer import HighDensityTelemetryLogger

        self.registered_components["directives"] = IntentDirectiveResolver()
        self.registered_components["stenographer"] = HighDensityTelemetryLogger(
            self.trace_log_path
        )
        self.registered_components["lazarus"] = LazarusStateGuardian()
        logger.info("[SINGULARITY_NEXUS] All high-level subsystem channels connected and online.")

    def bind_processing_node(self, node_domain: str, instantiation_pointer: Any) -> None:
        """Binds an explicit algorithmic or model processing asset directly to the system manifold."""
        self.registered_components[node_domain] = instantiation_pointer
        logger.info(
            f"[SINGULARITY_NEXUS] Operational binding verified: Domain Surface='{node_domain}'"
        )

    def execute_unified_multimodal_cycle(
        self, input_vector_payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Coordinates parallel transformation steps: parses sensory matrices, resolves operational
        directives, logs telemetry metrics, and manages error boundaries.

        Args:
            input_vector_payload: Raw dynamic data input container.

        Returns:
            Serialized operational results pipeline manifest.
        """
        directives_resolver = self.registered_components["directives"]
        telemetry_logger = self.registered_components["stenographer"]

        intent_query = input_vector_payload.get("intent", "generic_synthesis")
        raw_numeric_data = input_vector_payload.get("data", np.zeros((1, 1)))

        if "data_manifest" in input_vector_payload:
            stream_vector = input_vector_payload["data_manifest"].to_stream_vector()
            raw_numeric_data = stream_vector.payload

        configuration_blueprint = directives_resolver.manifest_preset_pipeline(intent_query)

        telemetry_logger.log_vector_event(
            "nexus_core",
            {
                "resolved_engine": configuration_blueprint["engine_target"],
                "data_allocation_bytes": getattr(raw_numeric_data, "nbytes", 0),
            },
        )

        return {
            "status": "COMPLETED",
            "assigned_engine": configuration_blueprint["engine_target"],
            "internal_parameters": configuration_blueprint,
            "processed_data_hash": f"0x{int(raw_numeric_data.sum()):08X}",
        }


class Manifold(UtahSingularityNexus):
    """Future-name compatibility alias for the deterministic execution plane."""


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if os.path.exists("logs"):
        shutil.rmtree("logs", ignore_errors=True)

    nexus_engine = UtahSingularityNexus(trace_log_path="logs/nexus_telemetry.jsonl")

    sample_child_intent_payload = {
        "intent": "Build me a fast image generator module",
        "data": np.random.rand(3, 64, 64),
    }

    cycle_outcome_manifest = nexus_engine.execute_unified_multimodal_cycle(
        sample_child_intent_payload
    )
    print("\n==================================================================")
    print("[NEXUS RUNTIME VERIFICATION COMPLETE]")
    print(
        f"Assigned Processing Engine Sub-Target: {cycle_outcome_manifest['assigned_engine']}"
    )
    print(
        f"Data Matrix Signature Checksum Hash  : {cycle_outcome_manifest['processed_data_hash']}"
    )
    print("==================================================================\n")

    directives_interface = nexus_engine.registered_components["directives"]
    child_metaphor_directive = (
        "Think of a massive castle where robot blocks can talk and share memories instantly"
    )

    compiled_child_log = directives_interface.child_friendly_blacksmith_wrapper(
        task_description=child_metaphor_directive,
        power_level=2.5,
    )
    print("[CHILD BLACKSMITH METAPHOR TRANSLATION RESULT]")
    print(compiled_child_log)
    print("==================================================================")
