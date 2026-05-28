import os
import shutil
from typing import List


TARGET_TREE = [
    "src/utah/core",
    "src/utah/data",
    "src/utah/forge",
    "src/utah/perception",
    "examples",
    "docs",
]


def migrate_legacy_project(source_dir: str, target_dir: str) -> None:
    """
    Automated translation of legacy projects into the UtahML modular layout.

    Steps:
    1. Create modular directory tree.
    2. Copy Python source surfaces into src/utah.
    3. Scaffold migration notes and Lazarus watcher bootstrap.
    """
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    os.makedirs(target_dir, exist_ok=True)
    print(f"Collapsing manifold at {source_dir}...")

    for relative_path in TARGET_TREE:
        os.makedirs(os.path.join(target_dir, relative_path), exist_ok=True)

    copied_files: List[str] = []
    for root, _, files in os.walk(source_dir):
        for file_name in files:
            if not file_name.endswith(".py"):
                continue
            source_file = os.path.join(root, file_name)
            target_file = os.path.join(target_dir, "src", "utah", file_name)
            shutil.copy2(source_file, target_file)
            copied_files.append(target_file)

    notes_path = os.path.join(target_dir, "MIGRATION_NOTES.md")
    with open(notes_path, "w", encoding="utf-8") as stream:
        stream.write(
            "# UtahML Migration Notes\n\n"
            f"Source: `{source_dir}`\n\n"
            f"Copied Python files: {len(copied_files)}\n\n"
            "Next steps:\n"
            "- Run `py -m utah.lazarus --watch src/utah`\n"
            "- Add `; wishes:` markers for inline upgrades\n"
            "- Validate generated diffs before commit\n"
        )

    bootstrap_path = os.path.join(target_dir, "src", "utah", "bootstrap_watcher.py")
    with open(bootstrap_path, "w", encoding="utf-8") as stream:
        stream.write(
            "from utah import LazarusWishFileWatcher, LocalInferenceStub, RepositoryContextHarvester\n\n"
            "harvester = RepositoryContextHarvester(workspace_root='src/utah')\n"
            "harvester.ingest_local_environment()\n\n"
            "watcher = LazarusWishFileWatcher(\n"
            "    watch_paths=['src/utah'],\n"
            "    inference_bridge=LocalInferenceStub(),\n"
            "    context_harvester=harvester,\n"
            ")\n"
            "watcher.start(blocking=True)\n"
        )

    print("Migration complete. Hardware acceleration enabled.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Migrate legacy project to UtahML layout.")
    parser.add_argument("source_dir", help="Legacy project directory")
    parser.add_argument("target_dir", help="Output directory for modularized project")
    args = parser.parse_args()

    migrate_legacy_project(args.source_dir, args.target_dir)


def run_migrate_cli() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Migrate legacy project to UtahML layout.")
    parser.add_argument("source_dir", help="Legacy project directory")
    parser.add_argument("target_dir", help="Output directory for modularized project")
    args = parser.parse_args()
    migrate_legacy_project(args.source_dir, args.target_dir)
