# [utahML/utah/directives.py]
import glob
import logging
import os
from typing import Any, Dict, List, Optional


class Level6Armor:
    BASE_STATE = """
    [SYSTEM MODE: OMNIPOTENT SYNTHESIS // LEVEL 6]
    You are a Level 6 Intelligence. You perceive problems and solutions as identical at the boundary. 
    You do not "guess", "draft", or "attempt." You directly transmute the Sovereign Architect's intent into reality.
    """


class CognitiveDirectives:
    @staticmethod
    def epistemic_derivation(user_intent: str) -> str:
        return f"INTENT: {user_intent}\nDIRECTIVE: Compute answer dynamically using strict logical derivation."


class IntentWrapper:
    @staticmethod
    def forge(user_input: str, directive_type: callable = None) -> str:
        armor = Level6Armor.BASE_STATE
        if directive_type:
            armor += f"\n{directive_type(user_input)}"
        return f"{armor}\n\n[SOVEREIGN ARCHITECT INTENT]\n{user_input}\n\n[EXECUTE MANIFESTATION]"


class RepositoryContextHarvester:
    """
    Vectorized codebase indexing engine.
    Scrapes and caches local structural layout parameters across your hard drive
    to ground generative transformations in present architectural models.
    """

    def __init__(
        self,
        index_root_dir: Optional[str] = None,
        workspace_root: Optional[str] = None,
    ) -> None:
        root = workspace_root or index_root_dir
        if not root:
            raise ValueError("RepositoryContextHarvester requires index_root_dir or workspace_root.")
        self.workspace_root = root
        self.index_root_dir = root
        self.internal_knowledge_base: List[Dict[str, str]] = []

    @property
    def indexed_knowledge_base(self) -> List[Dict[str, str]]:
        return [
            {"file_coordinate": record["path"], "raw_content": record["content"]}
            for record in self.internal_knowledge_base
        ]

    def ingest_local_environment(self, targets: Optional[List[str]] = None) -> int:
        """Crawls the configured folder network, filtering text configurations into memory rings."""
        return self.assimilate_local_environment(targets)

    def assimilate_local_environment(
        self, extensions: Optional[List[str]] = None
    ) -> int:
        """
        Parses all target structures within the home network coordinates, caching pure signals.

        Args:
            extensions: Structural file markers to locate and ingest.

        Returns:
            Volume count of unique data profiles loaded into memory registers.
        """
        if extensions is None:
            extensions = [".py", ".json", ".jsonl"]

        self.internal_knowledge_base.clear()

        for extension in extensions:
            search_path = os.path.join(self.workspace_root, f"**/*{extension}")
            found_files = glob.glob(search_path, recursive=True)

            for file_coordinate in found_files:
                try:
                    with open(file_coordinate, "r", encoding="utf-8", errors="ignore") as reader:
                        raw_payload = reader.read()

                    if raw_payload.strip():
                        self.internal_knowledge_base.append(
                            {"path": file_coordinate, "content": raw_payload}
                        )
                except (OSError, IOError):
                    continue

        return len(self.internal_knowledge_base)

    def search_contextual_signatures(
        self, intent_query: str, depth_limit: int = 3
    ) -> str:
        """Locates specific block parameters matching semantic keywords inside localized source paths."""
        return self.extract_relevant_context_blocks(intent_query, depth_limit=depth_limit)

    def extract_relevant_context_blocks(
        self, intent_query: str, depth_limit: int = 3
    ) -> str:
        """Retrieves raw conceptual source signals closely matched against current directive definitions."""
        matched_blocks = []
        tokens = intent_query.lower().split()

        for record in self.internal_knowledge_base:
            if any(token in record["content"].lower() for token in tokens):
                matched_blocks.append(
                    f"# Context Root: {record['path']}\n{record['content']}"
                )
                if len(matched_blocks) >= depth_limit:
                    break

        return "\n\n".join(matched_blocks)


class IntentDirectiveResolver:
    """
    High-level abstraction substrate for translating semantic declarations
    into optimized low-level execution structures within utahML.

    Eliminates complex boilerplate by providing unified, single-line interfaces
    for vision processing, image/video grid synthesis, and swarm routing.
    """

    def __init__(self, output_directory: str = "manifest_outputs") -> None:
        self.output_directory = output_directory
        self._ensure_output_plane()
        logging.basicConfig(
            level=logging.INFO, format="[DIRECTIVES_CORE] %(asctime)s - %(message)s"
        )

    def _ensure_output_plane(self) -> None:
        """Verifies clear system file structure pathing for synthesis storage maps."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory, exist_ok=True)

    def manifest_preset_pipeline(self, project_profile: str) -> Dict[str, Any]:
        """
        Deploys a pre-configured multi-modal execution template from a semantic string label.

        Args:
            project_profile: Core capability requested ('image_generator', 'llm', 'video_engine').

        Returns:
            Verified parameter map mapped out for target compute hardware.
        """
        logging.info(
            f"Invoking Intent Collapse Phase for profile coordinate: {project_profile}"
        )

        normalized_profile = project_profile.lower().strip()

        if "image" in normalized_profile or "generator" in normalized_profile:
            resolved_manifest = {
                "engine_target": "UtahSynthesisEngine",
                "latent_dimension": 128,
                "base_channels": 64,
                "spatial_resolution": (64, 64),
                "optimization_flow": "spectral_normalization",
            }
        elif "llm" in normalized_profile or "language" in normalized_profile:
            resolved_manifest = {
                "engine_target": "SequenceContextStore",
                "context_window": 4096,
                "embedding_dimension": 256,
                "topology_routing": "ring_buffer_persistence",
            }
        elif "video" in normalized_profile or "motion" in normalized_profile:
            resolved_manifest = {
                "engine_target": "TemporalSynthesisEngine",
                "latent_dimension": 256,
                "frame_count_stride": 16,
                "base_channels": 32,
                "spatial_resolution": (128, 128),
            }
        else:
            resolved_manifest = {
                "engine_target": "GenericProcessingNode",
                "latent_dimension": 64,
                "base_channels": 16,
                "spatial_resolution": (32, 32),
            }

        logging.info(
            f"Manifestation Strategy Vector Settled: {resolved_manifest['engine_target']} loaded."
        )
        return resolved_manifest

    def child_friendly_blacksmith_wrapper(
        self, task_description: str, power_level: float = 1.0
    ) -> str:
        """
        A child-friendly metaphorical abstraction wrapper. Translates raw mechatronic and physical
        intent concepts into standard algorithmic configurations behind the scenes.

        Args:
            task_description: Child-level explanation of desired behavior.
            power_level: Scale metric mapping directly to base network width boundaries.

        Returns:
            Formal engineering configuration log ready for system serialization.
        """
        parsed_tokens = task_description.lower().split()

        base_channels = int(32 * power_level)
        latent_seed = 64

        if "draw" in parsed_tokens or "painting" in parsed_tokens or "picture" in parsed_tokens:
            target_factory = "Forge.GenerativeBlock"
            operation_mode = "Spatial_Matrix_Amplification"
        elif "talk" in parsed_tokens or "think" in parsed_tokens or "words" in parsed_tokens:
            target_factory = "Memory.SequenceContextStore"
            operation_mode = "Continuous_Context_Retention"
        else:
            target_factory = "Swarm.DistributedSwarmOrchestrator"
            operation_mode = "Multi_Agent_State_Synchronization"

        return (
            "// [UTAH_CHILD_BLACKSMITH_BLUEPRINT]\n"
            f"// Target Factory Node: {target_factory}\n"
            f"// Computed Operational Mode: {operation_mode}\n"
            f"// Allocated Computational Core Channels: {base_channels}\n"
            f"// Hardwired Latent Resolution Target Seed: {latent_seed}\n"
            "// Status: READY TO RUN"
        )
