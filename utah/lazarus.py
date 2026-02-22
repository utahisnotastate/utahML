# [utahML/utah/lazarus.py]
import sys
import traceback
import os
import time
import ast
import difflib


class LazarusDaemon:
    """The Autonomous Immune System. Pure Python. Zero Cloud."""

    _sovereign_model_hook = None

    @staticmethod
    def ignite(local_model_callable=None):
        """
        Ignites the Immortality Protocol.
        Optionally accepts a custom local AI model built by the user.
        """
        LazarusDaemon._sovereign_model_hook = local_model_callable
        sys.excepthook = LazarusDaemon._intercept_and_heal
        print("[UTAH-OS] Lazarus Daemon Engaged. Retrocausal AST Mutagenesis: ACTIVE.")

    @staticmethod
    def _intercept_and_heal(exc_type, exc_value, exc_traceback):
        print(f"\n[!] TIMELINE FRACTURE DETECTED: {exc_type.__name__} - {exc_value}")
        print("[*] Freezing Execution. Lazarus Daemon engaging Retrocausal Healing...")

        # 1. Extract the physical point of failure and local memory
        tb_list = traceback.extract_tb(exc_traceback)
        if not tb_list: return
        faulty_frame = tb_list[-1]
        file_path = faulty_frame.filename
        line_num = faulty_frame.lineno

        if "python" in file_path.lower() or "lib" in file_path.lower():
            print("[-] Fracture in external library. Cannot mutate World-A dependencies.")
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        # Extract the live memory state at the moment of death
        frame = exc_traceback
        while frame.tb_next:
            frame = frame.tb_next
        live_locals = frame.tb_frame.f_locals
        live_globals = frame.tb_frame.f_globals

        # 2. Extract the physical matter (The Code)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_code = f.read()
        except Exception as e:
            print(f"[-] Could not access physical file: {e}")
            return

        # 3. Apply Localized Healing (AST Mutagenesis or Sovereign Model)
        healed_code = None

        if exc_type == NameError:
            healed_code = LazarusDaemon._heal_name_error(raw_code, str(exc_value), live_locals, live_globals)
        elif LazarusDaemon._sovereign_model_hook:
            print("    -> Routing complex fracture to Sovereign Local Model...")
            healed_code = LazarusDaemon._sovereign_model_hook(raw_code, exc_type.__name__, str(exc_value), line_num)

        if not healed_code:
            print("[-] Fracture too severe for autonomic heuristics. Awaiting Architect intervention.")
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        # 4. Overwrite Physical Reality
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(healed_code)

        print(f"[+] Physical File Overwritten: {file_path}")
        print("[+] Reality Healed. Autonomic Restart Sequence Initiated...\n")

        # 5. Resurrect the Process
        time.sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)

    @staticmethod
    def _heal_name_error(raw_code: str, error_msg: str, live_locals: dict, live_globals: dict) -> str:
        """Pure-Python Deterministic AST Healing. Zero AI required."""
        # Extract the broken variable name from the error message (e.g., "name 'variabl' is not defined")
        broken_name = error_msg.split("'")[1] if "'" in error_msg else None
        if not broken_name: return None

        # Calculate semantic resonance with all living variables in memory
        available_names = list(live_locals.keys()) + list(live_globals.keys())
        matches = difflib.get_close_matches(broken_name, available_names, n=1, cutoff=0.6)

        if not matches:
            return None

        target_name = matches[0]
        print(f"    -> AST Heuristic Match Found: '{broken_name}' should be '{target_name}'")

        # Parse the codebase into a 3D Abstract Syntax Tree
        tree = ast.parse(raw_code)

        # Walk the tree and literally rewrite the node
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id == broken_name:
                node.id = target_name

        # Unparse the tree back into a perfectly formatted python script
        return ast.unparse(tree)
