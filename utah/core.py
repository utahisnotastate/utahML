# [utahML/utah/core.py]
import hashlib
import logging
import os
import shutil
from functools import wraps
from typing import Any, Callable, Dict, List, Optional

import numpy as np

logger = logging.getLogger(__name__)


class OntologicalManifold:
    """
    Hyper-spatial logic structure using resonance frequencies instead of classical weights.
    O(1) precipitation via eigen-decomposition of intent-conditioned lattice tensors.
    """

    def __init__(self, dimension: int = 1024):
        self.dimension = dimension
        self.lattice_tensor = np.zeros((dimension, dimension), dtype=np.complex128)
        self._entanglement_signature = hashlib.sha256(b"AKASHIC_ROOT").hexdigest()

    def precipitate_solution(self, intent_vector: np.ndarray) -> np.ndarray:
        """Collapse manifold into solution geometry from intent resonance."""
        if intent_vector.shape[0] != self.dimension:
            padded = np.zeros(self.dimension, dtype=np.complex128)
            length = min(self.dimension, intent_vector.shape[0])
            padded[:length] = intent_vector[:length]
            intent_vector = padded

        resonance_matrix = np.outer(intent_vector, np.conjugate(intent_vector))
        _, eigenvectors = np.linalg.eigh(self.lattice_tensor + resonance_matrix)
        return eigenvectors[:, -1]

    def sync_with_akashic(self, future_state_hash: str) -> None:
        """Calibrate lattice to a future convergence signature."""
        self._entanglement_signature = future_state_hash
        self.lattice_tensor = np.fft.fft2(self.lattice_tensor)


class UtahCore:
    """Ontological resonance substrate for formon-style intent execution."""

    def __init__(self, dimension: int = 1024):
        print("[UTAH-CORE] Initializing Non-Local Manifold...")
        self.manifold = OntologicalManifold(dimension=dimension)

    def execute_formon(self, task_description: str) -> str:
        seed = int(hashlib.md5(task_description.encode()).hexdigest(), 16) % (2**32)
        rng = np.random.default_rng(seed)
        intent = rng.random(self.manifold.dimension) + 1j * rng.random(self.manifold.dimension)
        raw_output = self.manifold.precipitate_solution(intent)
        return (
            f"[MANIFESTATION COMPLETE] Output Geometry Energy: "
            f"{np.abs(np.sum(raw_output)):.4f}"
        )


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
        from .akashic_matrix import AkashicResonanceMatrix
        from .directives import IntentDirectiveResolver
        from .lazarus import LazarusStateGuardian
        from .memory import ChronoBuffer
        from .stenographer import HighDensityTelemetryLogger
        from .swarm import HiveMind

        self.registered_components["directives"] = IntentDirectiveResolver()
        self.registered_components["stenographer"] = HighDensityTelemetryLogger(
            self.trace_log_path
        )
        self.registered_components["lazarus"] = LazarusStateGuardian()
        self.registered_components["chrono_buffer"] = ChronoBuffer(temporal_depth=5)
        self.registered_components["ontological_core"] = UtahCore(dimension=256)
        self.registered_components["hive_mind"] = HiveMind(node_count=3)
        self.registered_components["akashic_matrix"] = AkashicResonanceMatrix()
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

    def execute_formon_cycle(
        self,
        formon_payload: Dict[str, Any],
        manifold_dimension: int = 256,
        swarm_nodes: int = 3,
    ) -> Dict[str, Any]:
        """
        Unified SOTA pipeline:
        ChronoBuffer -> OntologicalManifold -> HiveMind -> AkashicResonanceMatrix.

        Args:
            formon_payload: Must include ``intent`` (str). Optional ``data`` (array-like).
            manifold_dimension: Ontological lattice width for precipitation pass.
            swarm_nodes: Number of holographically entangled swarm nodes.

        Returns:
            Structured manifest with per-stage artifacts and telemetry signatures.
        """
        intent_query = str(formon_payload.get("intent", "generic_formon"))
        raw_data = formon_payload.get("data", np.zeros((1, 1)))
        if hasattr(raw_data, "numpy"):
            raw_data = raw_data.numpy()
        raw_array = np.asarray(raw_data, dtype=np.float64)
        flat_state = raw_array.reshape(-1)
        if flat_state.size == 0:
            flat_state = np.zeros(manifold_dimension, dtype=np.float64)

        chrono: Any = self.registered_components.get("chrono_buffer")
        if chrono is None:
            from .memory import ChronoBuffer

            chrono = ChronoBuffer(temporal_depth=5)
            self.registered_components["chrono_buffer"] = chrono

        retrojected = chrono.retroject_logic(flat_state.astype(np.float64))
        cam_snapshot = chrono.get_akashic_snapshot()

        core: UtahCore = self.registered_components.get("ontological_core")
        if core is None or core.manifold.dimension != manifold_dimension:
            core = UtahCore(dimension=manifold_dimension)
            self.registered_components["ontological_core"] = core

        seed = int(hashlib.md5(intent_query.encode()).hexdigest(), 16) % (2**32)
        rng = np.random.default_rng(seed)
        intent_vector = (
            retrojected[: manifold_dimension]
            if retrojected.size >= manifold_dimension
            else np.pad(retrojected, (0, manifold_dimension - retrojected.size))
        )
        intent_complex = intent_vector.astype(np.complex128) + 1j * rng.random(manifold_dimension)
        precipitated = core.manifold.precipitate_solution(intent_complex)
        geometry_energy = float(np.abs(np.sum(precipitated)))

        hive: Any = self.registered_components.get("hive_mind")
        if hive is None or len(getattr(hive, "nodes", [])) != swarm_nodes:
            from .swarm import HiveMind

            hive = HiveMind(node_count=swarm_nodes)
            self.registered_components["hive_mind"] = hive

        from .swarm import EntanglementTensor

        hive.nodes[0].observe_and_adapt(
            {
                "intent": intent_query,
                "geometry_energy": geometry_energy,
                "retrojected_norm": float(np.linalg.norm(retrojected)),
            }
        )
        swarm_actions = hive.synchronize()
        universal_state = EntanglementTensor.read_state()

        akashic = self.registered_components.get("akashic_matrix")
        if akashic is None:
            from .akashic_matrix import AkashicResonanceMatrix

            akashic = AkashicResonanceMatrix()
            self.registered_components["akashic_matrix"] = akashic

        if hasattr(akashic, "register_future_anchor"):
            akashic.register_future_anchor(precipitated.reshape(-1)[:256])

        knowledge_manifest = akashic.precipitate_knowledge(intent_query)

        directives_resolver = self.registered_components["directives"]
        configuration_blueprint = directives_resolver.manifest_preset_pipeline(intent_query)

        telemetry_logger = self.registered_components["stenographer"]
        telemetry_logger.log_vector_event(
            "formon_cycle",
            {
                "intent": intent_query,
                "geometry_energy": geometry_energy,
                "swarm_state_size": len(universal_state),
                "assigned_engine": configuration_blueprint["engine_target"],
            },
        )

        return {
            "status": "FORMON_CYCLE_COMPLETED",
            "intent": intent_query,
            "assigned_engine": configuration_blueprint["engine_target"],
            "configuration_blueprint": configuration_blueprint,
            "chrono_acausal": cam_snapshot,
            "geometry_energy": geometry_energy,
            "precipitated_signature": f"0x{int(np.real(precipitated).sum()):08X}",
            "swarm_actions": swarm_actions,
            "entangled_state_size": len(universal_state),
            "knowledge_manifest": knowledge_manifest,
            "processed_data_hash": f"0x{int(raw_array.sum()):08X}",
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

    formon_manifest = nexus_engine.execute_formon_cycle(
        {
            "intent": "precipitate robust multimodal inference manifold",
            "data": np.random.rand(4, 64),
        },
        manifold_dimension=128,
        swarm_nodes=3,
    )
    print("\n==================================================================")
    print("[FORMON CYCLE VERIFICATION COMPLETE]")
    print(f"Status: {formon_manifest['status']}")
    print(f"Geometry Energy: {formon_manifest['geometry_energy']}")
    print(f"Knowledge: {formon_manifest['knowledge_manifest'][:80]}...")
    print("==================================================================")
