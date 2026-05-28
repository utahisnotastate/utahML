# [utahML/utah/__init__.py]
from .core import UtahApp, UtahSingularityNexus
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
from .data import SemanticFluid, ZeroPointNetwork
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
    LazarusCodeSynthesizer,
    LazarusDaemon,
    LazarusStateGuardian,
    LazarusWishFileWatcher,
    LocalInferenceStub,
    MockInferenceBridge,
)
from .forge import GenerativeBlock, OntologicalForge, UtahSynthesisEngine

if GenerativeBlock is None:
    del GenerativeBlock, UtahSynthesisEngine
from .swarm import (
    CognitiveSwarm,
    DistributedSwarmOrchestrator,
    SwarmNodeCoordinate,
)

# Ignite Immortality Protocol automatically upon library import
LazarusDaemon.ignite()
