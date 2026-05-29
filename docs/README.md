# utahML Documentation Hub

This hub organizes guides and tutorials by audience so each reader can start at the right depth.

## Choose Your Path

- Technical decision-makers and platform teams: `docs/technical/enterprise-architecture.md`
- Experienced AI/ML engineers: `docs/technical/ml-dev-guide.md`
- Data scientists: `docs/technical/data-scientist-guide.md`
- Migration from lint-only workflows: `docs/technical/migration-from-linters.md`
- Non-technical users and project managers: `docs/non-technical/project-manager-overview.md`
- Children and absolute beginners: `docs/non-technical/child-blacksmith-guide.md`
- New to programming: `docs/non-technical/new-programmer-quickstart.md`
- New to machine learning: `docs/non-technical/new-to-ml-guide.md`

## Tutorial Track

- Tutorial 1: First `; wishes` auto-mutation: `docs/tutorials/01-first-wish-mutation.md`
- Tutorial 2: Enable continuous watch mode: `docs/tutorials/02-watch-mode.md`
- Tutorial 3: Context-grounded mutation with repository harvesting: `docs/tutorials/03-context-grounded-mutation.md`
- Tutorial 4: Core orchestration with directives: `docs/tutorials/04-nexus-directives-walkthrough.md`
- Tutorial 5: Immunity kernel and deploy bundle: `docs/tutorials/05-immunity-kernel-and-deploy.md`
- Tutorial 6: ZEO-Architect patterns: `docs/tutorials/06-zeo-architect-patterns.md`

## Core Concepts

- `LazarusCodeSynthesizer` rewrites functions that contain `; wishes: ...`.
- `LazarusWishFileWatcher` monitors files and triggers mutation on save events.
- `RepositoryContextHarvester` indexes nearby files to reduce style and architecture drift.
- `LazarusStateGuardian` wraps runtime execution with remediation hooks and checkpoint rollback.
- `HighDensityTelemetryLogger` records structured JSONL telemetry for diagnostics.

## Operational Safety

- Always review generated patches before commit.
- Keep source control enabled so changes are easy to inspect and revert.
- Start on a branch when enabling watch mode in large repositories.
