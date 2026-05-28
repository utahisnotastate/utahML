# [utahML/utah/__init__.py]
from .core import (
    Manifold,
    OracleEyeBridge,
    UtahApp,
    UtahSingularityNexus,
    VoxelMapDebugger,
    detect_hardware_target,
    hardware_optimized,
)
from .directives import IntentDirectiveResolver, RepositoryContextHarvester
from .perception import GeometricFeatureExtractor, NativeVisionProcessor, OmniRetina

if NativeVisionProcessor is None:
    del GeometricFeatureExtractor, NativeVisionProcessor
from .memory import EpistemicReactor, SequenceContextStore
from .evolution import (
    HyperparameterGenome,
    ParameterEvolutionManager,
    TopologicalEvolutionPool,
    Transmuter,
)
from .data import (
    BinarySensorDataSource,
    CSVDataSource,
    DataManifest,
    JSONLDataSource,
    SemanticFluid,
    StreamVector,
    ZeroPointNetwork,
)
from .ui import OmniGlass, UtahNotebook
from .acoustic import (
    AcousticConceptEncoder,
    AudioSignalMatrixProcessor,
    AuditoryConceptEncoder,
    CymaticResonator,
    WaveformMatrixParser,
)

if WaveformMatrixParser is None:
    del AcousticConceptEncoder, AuditoryConceptEncoder, WaveformMatrixParser
from .stenographer import HighDensityTelemetryLogger, HolographicStenographer
from .lazarus import (
    ExecutionSnapshot,
    ImmunityKernel,
    LazarusCodeSynthesizer,
    LazarusDaemon,
    LazarusStateGuardian,
    LazarusWishFileWatcher,
    LocalInferenceStub,
    MockInferenceBridge,
)
from .forge import (
    AutoMapper,
    GenerativeBlock,
    HardwareBridge,
    ManifestWrappedAsset,
    OntologicalForge,
    UtahSynthesisEngine,
    migrate_legacy_project,
)

if GenerativeBlock is None:
    del GenerativeBlock, UtahSynthesisEngine
from .swarm import (
    CognitiveSwarm,
    DistributedSwarmOrchestrator,
    SwarmNodeCoordinate,
)
from .migrate import migrate_legacy_project as migrate_project_structure

# Ignite Immortality Protocol automatically upon library import
LazarusDaemon.ignite()
