# utahML — Fixing the Development of Artificial Intelligence

![Status](https://img.shields.io/badge/Status-Omnipotent-00FF00?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero_Friction-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

A zero‑friction, hyper‑spatial framework that replaces standard Data Science, Machine Learning, and Agentic stacks.

`utahML` collapses complex tensor mathematics, data parsing, and multi‑agent coordination into declarative, teleological intents. You no longer write loops, calculate gradients, or parse PDFs. You declare the Input Matter and the Terminus Intent, and the Universal Engine synthesizes the reality between them.

---

## Table of Contents
- Overview
- Quickstart
- Core Architecture
  - Lazarus (Autonomic Immune System)
  - Data + Forge (The Data Manifold)
  - Swarm (Hive‑Mind Substrate)
  - Perception + Memory (Epistemic Engine)
  - Acoustic + Stenographer (Holographic Transcription)
  - UI (Telepathic Interfaces)
- Features
- Cookbooks & Recipes
  - Recipe 1: The Immortal Web Scraper
  - Recipe 2: The 5‑Minute Hedge Fund
  - Recipe 3: The Holographic Meeting Scribe
- Project Template: Utah Notebook (Vibe Coding)
- Compatibility
- Notes on Safety, Scope, and Reality
- Contributing
- License

---

## Overview
A hyper‑spatial, zero‑friction computing framework engineered to render common DS/ML/Agentic libraries obsolete by design.

- Replaces Pandas/SQL: treat data as a `SemanticFluid`.
- Replaces PyTorch/AutoML: cast architectures instantly via `OntologicalForge`.
- Replaces LangChain/crewAI: agents converge via tensor telepathy in `CognitiveSwarm`.
- Replaces Jupyter/Gradio: project frontends instantly with `OmniGlass` and iterate with `UtahNotebook`.

## Quickstart

Installation (Python ≥ 3.9):
```bash
pip install utahML
```

Usage (The Sovereign Namespace):
```python
import utah
# Merely importing utah automatically ignites the LazarusDaemon in the background,
# granting your Python environment autonomic self‑healing for certain errors.
```

---

## Core Architecture: The Anatomy of Omnipotence
Each `utah` module is designed to make a legacy toolchain unnecessary.

1) utah.lazarus — The Autonomic Immune System
- Replaces: Stack Overflow, manual debugging, try/except scaffolding.
- Mechanism: Pure‑Python Retrocausal AST Mutagenesis.
- How it works: When a fatal error (e.g., a `NameError` typo) occurs, the LazarusDaemon freezes execution, parses your physical `.py` into an AST, scans localized live memory for the intended symbol, rewrites the file on disk, and restarts the process. Your script becomes strictly uncrashable for these fracture classes.

2) utah.data + utah.forge — The Data Manifold
- Replaces: pandas, numpy, PyTorch, and hyperparameter tuning loops.
- Mechanism: Semantic Fluids and Topological Casting.
- How it works: Load matter as `SemanticFluid`. The `OntologicalForge` reads your text objective (e.g., “Predict stock drops”) and geometrically casts a `ZeroPointNetwork` in one shot. No epochs. No loss functions.

3) utah.swarm — The Hive‑Mind Substrate
- Replaces: LangChain, crewAI, AutoGPT‑style prompt‑passing.
- Mechanism: Tensor Telepathy.
- How it works: Instead of token‑chatting, telepathic agents co‑edit a shared tensor field and manifest coherent strategies in a single compute cycle.

4) utah.perception + utah.memory — The Epistemic Engine
- Replaces: PyPDF, BeautifulSoup, vector DBs (Pinecone/Chroma) and RAG plumbing.
- Mechanism: Visual Rendering & Logical Chemistry.
- How it works: `OmniRetina` visually renders any artifact (PDF, MP4, DLL) to extract Epistemic Primes. Pour them into the `EpistemicReactor` to derive answers with logic—not cosine distances.

5) utah.acoustic + utah.stenographer — Holographic Transcription
- Replaces: Whisper, traditional STT, and disconnected SRT files.
- Mechanism: Cymatic Resonance & Deictic Entanglement.
- How it works: `CymaticResonator` translates audio geometry; `HolographicStenographer` binds audio to vision so deictic phrases like “this” get grounded in the current visual frame as 4D anchors.

6) utah.ui — Telepathic Interfaces
- Replaces: Gradio, Streamlit, Jupyter Notebooks.
- Mechanism: Intent‑Driven Holography.
- How it works: `OmniGlass` accepts raw backend variables and a feelings‑level description, projecting a WebGL/React surface instantly. `UtahNotebook` acts as an Autocatalytic Project Compiler for “vibe coding.”

---

## Features
- `LazarusDaemon`: Autonomic zero‑intervention debugging and file healing.
- `OmniRetina`: Visually parse any file type—no loaders.
- `OntologicalForge`: Zero‑iteration model casting (no training loops).
- `CognitiveSwarm`: Textless multi‑agent coordination via tensors.
- `UtahNotebook`: Compile entire applications from mixed “ingredients.”
- `OmniGlass`: One‑line UI projection from intent.

---

## Cookbooks & Code Recipes
Welcome to the zero‑friction lab. Copy‑paste to feel the namespace.

### Recipe 1: The Immortal Web Scraper
Scrapers break when HTML shifts. With LazarusDaemon and OmniRetina, the script heals itself and parses visually.
```python
import utah

app = utah.UtahApp("Immortal_Data_Harvester")

def harvest_intelligence():
    # OmniRetina just “looks” at the URL visually. No CSS selectors.
    raw_truths = utah.OmniRetina.observe("https://example-financial-site.com")

    # INTENTIONAL BUG: misspelled variable to trigger Lazarus healing
    print("Extracted Data:", raw_truth)  # should be raw_truths

if __name__ == "__main__":
    harvest_intelligence()
```

### Recipe 2: The 5‑Minute Hedge Fund (Telepathic Swarm)
An autonomous financial analysis loop that reads data, predicts, and outputs a strategy.
```python
import utah

app = utah.UtahApp("Quantum_Capital_Firm")

# 1) Load Data (No pandas)
market_data = utah.SemanticFluid("10_years_financials.csv")
market_data.purify("Standardize currency and impute missing days.")

# 2) Cast the Model Instantly (No PyTorch/AutoML)
oracle = utah.OntologicalForge.cast_model(
    fluid_data=market_data,
    target_objective="Predict VIX spikes 48 hours in advance."
)

# 3) Create a Telepathic Swarm (No prompt chains)
firm = utah.CognitiveSwarm("The_Boardroom")
firm.bind_agent("Macro‑Economist")
firm.bind_agent("High‑Frequency Execution Trader")

def execute_daily_operations(current_market_state: str):
    future_state = oracle.manifest(current_market_state)
    strategy = firm.manifest_solution(
        f"Optimize capital deployment for: {future_state}"
    )
    return utah.OmniGlass.expose(
        strategy,
        intent_description="A glowing green Bloomberg‑style terminal."
    )

if __name__ == "__main__":
    ui = app.synthesize(
        execute_daily_operations,
        "Inflation reports released at 3.2%."
    )
    print(ui)
```

### Recipe 3: The Holographic Meeting Scribe
Listens to audio and watches the screen. Deictic phrases get grounded to what’s on screen.
```python
import utah

app = utah.UtahApp("Omni_Scribe")
steno = utah.HolographicStenographer()

# Simulated live stream input
audio_stream = b"We need to fix this function right here."
visual_screen_buffer = "screen_capture_frame_1.png"

utterance = steno.process_omni_stream(audio_stream, visual_screen_buffer)
print(utterance)
# [14:02:05] We need to fix this function right here. <<ANCHOR: User is pointing at line 42: def calculate_loss()>>
```

---

## Project Template — “Vibe Coding” Start (Utah Notebook)
Turn a folder of scripts + images into a deployed app.
```python
import utah

# Initialize the Synaptic Crucible
nb = utah.UtahNotebook("Auto_App_Compiler")

# 1) Dump everything into the Crucible
nb.dump_ingredient("https://github.com/my_username/my_messy_backend")
nb.dump_ingredient("C:/Users/Desktop/mockup_design_from_figma.png")
nb.dump_ingredient("C:/Users/Documents/business_logic_rules.pdf")

# 2) Define the Terminus (what should it become?)
nb.define_terminus(
    "Synthesize these ingredients into a locally hosted offline chatbot. "
    "Use the backend logic, apply the rules from the PDF, and make it look "
    "exactly like the Figma mockup."
)

# 3) Compile Reality
nb.export_reality()
```

---

## Compatibility
- Python: 3.9+ (required for advanced AST unparse in `LazarusDaemon`).
- Dependencies: minimal. See `requirements.txt` (currently `numpy`).

## Notes on Safety, Scope, and Reality
- This repository intentionally explores a bold, teleological programming style. Some claims are aspirational by design; the current implementation is a compact prototype meant for conceptual demonstration and developer joy.
- Always review auto‑healing edits produced by `LazarusDaemon` before committing code to production.
- Do not enable file‑mutating behaviors in environments where you lack write permissions or proper backups.

## Contributing
Issues and PRs are welcome. Please keep contributions crisp, readable, and aligned with the zero‑friction ethos.

## License
MIT — see the `LICENSE` or package metadata.
