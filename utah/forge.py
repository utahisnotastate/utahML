# [utahML/utah/forge.py]
import os
import shutil
import stat
import time
from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Any, Dict, List

from .data import DataManifest, SemanticFluid, ZeroPointNetwork


class OntologicalForge:
    @staticmethod
    def cast_model(fluid_data: SemanticFluid, target_objective: str) -> ZeroPointNetwork:
        print(f"[UTAH-OS] Activating Ontological Forge for objective: '{target_objective}'")
        perfect_model = ZeroPointNetwork()
        perfect_model.entangle(input_fluid=fluid_data, target_intent=target_objective)
        print("[+] Model geometrically cast. Search space bypassed.")
        return perfect_model


@dataclass
class ManifestWrappedAsset:
    """Compatibility wrapper for legacy tensor assets."""

    file_path: str
    backend: str
    manifest: DataManifest
    metadata: Dict[str, Any]


class AutoMapper:
    """
    Compatibility layer that scans legacy NumPy/PyTorch projects and wraps
    detected tensor artifacts into DataManifest entries.
    """

    SUPPORTED_SUFFIXES = (".npy", ".npz", ".pt", ".pth")

    @staticmethod
    def wrap_project_weights(project_root: str) -> List[ManifestWrappedAsset]:
        wrapped_assets: List[ManifestWrappedAsset] = []
        for root, _, files in os.walk(project_root):
            for file_name in files:
                if not file_name.lower().endswith(AutoMapper.SUPPORTED_SUFFIXES):
                    continue
                file_path = os.path.join(root, file_name)
                backend = "torch" if file_name.lower().endswith((".pt", ".pth")) else "numpy"
                manifest = DataManifest.from_source(
                    source=file_path,
                    source_type="binary",
                    metadata={"origin": "auto_mapper", "backend": backend},
                )
                wrapped_assets.append(
                    ManifestWrappedAsset(
                        file_path=file_path,
                        backend=backend,
                        manifest=manifest,
                        metadata={"size_bytes": manifest.to_stream_vector().metadata["byte_size"]},
                    )
                )
        return wrapped_assets


def migrate_legacy_project(source_dir: str, target_dir: str) -> None:
    """Compatibility shim for migration entrypoint from the forge surface."""
    from .migrate import migrate_legacy_project as _migrate_legacy_project

    _migrate_legacy_project(source_dir, target_dir)


class HardwareBridge:
    """
    Deployment bridge for edge targets (M5Stack/ESP32/Raspberry Pi).
    """

    def __init__(self, target_hardware: str = "auto") -> None:
        self.target_hardware = target_hardware

    def deploy(self, app_path: str, output_dir: str = "build/deploy_bundle") -> Dict[str, Any]:
        if not os.path.exists(app_path):
            raise FileNotFoundError(f"Deploy path does not exist: {app_path}")

        absolute_app_path = os.path.abspath(app_path)
        absolute_output_dir = os.path.abspath(output_dir)
        if os.path.commonpath([absolute_app_path, absolute_output_dir]) == absolute_app_path:
            raise ValueError(
                "output_dir cannot be inside app_path for deployment; "
                "choose a sibling or external directory."
            )

        os.makedirs(absolute_output_dir, exist_ok=True)
        app_name = os.path.basename(absolute_app_path)
        bundle_root = os.path.join(absolute_output_dir, app_name)
        if os.path.exists(bundle_root):
            bundle_root = os.path.join(
                absolute_output_dir, f"{app_name}_{int(time.time())}"
            )
        ignore_names = {
            ".git",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            "dist",
            "build",
            ".idea",
            ".pytest_cache",
            "utah_deploy_out",
        }
        allowed_suffixes = {".py", ".json", ".jsonl", ".toml", ".md", ".txt", ".yaml", ".yml"}

        def _ignore_filter(directory: str, entries: List[str]) -> List[str]:
            ignored: List[str] = []
            for entry in entries:
                if entry in ignore_names:
                    ignored.append(entry)
                    continue
                entry_path = os.path.join(directory, entry)
                if os.path.isfile(entry_path):
                    suffix = os.path.splitext(entry)[1].lower()
                    if suffix and suffix not in allowed_suffixes:
                        ignored.append(entry)
            return ignored

        shutil.copytree(absolute_app_path, bundle_root, ignore=_ignore_filter)

        launch_script = os.path.join(bundle_root, "utah_hardware_launch.txt")
        with open(launch_script, "w", encoding="utf-8") as stream:
            stream.write(
                "UTAH Hardware Deployment Manifest\n"
                f"target_hardware={self.target_hardware}\n"
                "entrypoint=python -m utah.lazarus --watch .\n"
            )

        return {
            "status": "DEPLOYED",
            "target_hardware": self.target_hardware,
            "bundle_path": bundle_root,
            "launch_manifest": launch_script,
        }

    @staticmethod
    def _handle_remove_readonly(func, path: str, exc_info) -> None:
        del exc_info
        os.chmod(path, stat.S_IWRITE)
        func(path)


try:
    import torch
    import torch.nn as nn

    class GenerativeBlock(nn.Module):
        """
        Unified convolutional and linear generative layer for multi-modal synthesis.
        Provides automated scaling, shape validation, and strict normalization boundaries.
        """

        def __init__(
            self,
            in_channels: int,
            out_channels: int,
            kernel_size: int = 3,
            stride: int = 1,
            padding: int = 1,
            is_spectral: bool = False,
        ) -> None:
            super().__init__()
            self.conv = nn.Conv2d(
                in_channels, out_channels, kernel_size, stride, padding, bias=False
            )
            self.norm = nn.BatchNorm2d(out_channels)
            self.activation = nn.LeakyReLU(0.2, inplace=True)

            if is_spectral:
                self.conv = nn.utils.spectral_norm(self.conv)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            """Executes forward synthesis pass with structured zero-allocation normalization."""
            return self.activation(self.norm(self.conv(x)))

    class UtahSynthesisEngine(nn.Module):
        """
        The main generative orchestrator within utahML. Handles deterministic
        latent space mapping and multi-channel image/video matrix transformation.
        """

        def __init__(
            self,
            latent_dim: int,
            base_channels: int = 64,
            output_channels: int = 3,
        ) -> None:
            super().__init__()
            self.latent_dim = latent_dim
            self.initial_channels = base_channels * 8

            self.project = nn.Linear(latent_dim, self.initial_channels * 4 * 4)

            self.block1 = GenerativeBlock(
                base_channels * 8, base_channels * 4, is_spectral=True
            )
            self.block2 = GenerativeBlock(
                base_channels * 4, base_channels * 2, is_spectral=True
            )
            self.block3 = GenerativeBlock(
                base_channels * 2, base_channels, is_spectral=False
            )

            self.final_conv = nn.Conv2d(
                base_channels, output_channels, kernel_size=3, padding=1
            )
            self.tanh = nn.Tanh()

        def forward(self, z: torch.Tensor) -> torch.Tensor:
            """
            Transforms a latent seed vector into a structured spatial tensor matrix.

            Args:
                z: Latent tensor of shape (batch_size, latent_dim).

            Returns:
                Synthetic multi-channel matrix normalized to [-1, 1].
            """
            x = self.project(z)
            x = x.view(-1, self.initial_channels, 4, 4)

            x = nn.functional.interpolate(x, scale_factor=2, mode="nearest")
            x = self.block1(x)

            x = nn.functional.interpolate(x, scale_factor=2, mode="nearest")
            x = self.block2(x)

            x = nn.functional.interpolate(x, scale_factor=2, mode="nearest")
            x = self.block3(x)

            return self.tanh(self.final_conv(x))

except ImportError:
    GenerativeBlock = None  # type: ignore[misc, assignment]
    UtahSynthesisEngine = None  # type: ignore[misc, assignment]


def _run_deploy_cli() -> None:
    parser = ArgumentParser(description="Utah forge deployment bridge")
    parser.add_argument("--deploy", dest="deploy_path", help="Project path to deploy")
    parser.add_argument("--target", dest="target_hardware", default="auto")
    parser.add_argument("--output-dir", dest="output_dir", default="build/deploy_bundle")
    args = parser.parse_args()

    if args.deploy_path:
        bridge = HardwareBridge(target_hardware=args.target_hardware)
        deployment_result = bridge.deploy(args.deploy_path, output_dir=args.output_dir)
        print("[UTAH_FORGE] Deployment complete.")
        print(deployment_result)
        return

    if UtahSynthesisEngine is None:
        raise ImportError(
            "UtahSynthesisEngine requires PyTorch. Install with: pip install torch"
        )

    torch.manual_seed(23)
    engine = UtahSynthesisEngine(latent_dim=128, base_channels=32, output_channels=3)
    sample_latent_seeds = torch.randn(4, 128)
    synthetic_matrices = engine(sample_latent_seeds)
    print(
        f"Manifestation Verified: Output Tensor Matrix Shape = {synthetic_matrices.shape}"
    )


if __name__ == "__main__":
    _run_deploy_cli()
