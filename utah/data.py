# [utahML/utah/data.py]
import csv
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional

import numpy as np


class SemanticFluid:
    def __init__(self, raw_matter: str):
        self.state = raw_matter
        print("[UTAH-OS] Assimilating Raw Matter into Fluid Matrix...")

    def purify(self, intent: str):
        print(f"[*] Purifying data intent: {intent}")
        return self


class ZeroPointNetwork:
    def entangle(self, input_fluid, target_intent: str):
        print(f"[*] Zero-Iteration Training locked to: '{target_intent}'")
        self.ready = True

    def manifest(self, new_data: str):
        return f"[Absolute Prediction Synthesized for {new_data}]"


@dataclass
class StreamVector:
    """Standardized input payload for the decoupled Data Plane."""

    source_type: str
    payload: Any
    metadata: Dict[str, Any]


class CSVDataSource:
    """CSV ingestion agent returning row dictionaries."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> List[Dict[str, str]]:
        with open(self.file_path, "r", encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            return list(reader)


class JSONLDataSource:
    """JSONL ingestion agent returning object rows."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []
        with open(self.file_path, "r", encoding="utf-8") as stream:
            for line in stream:
                line = line.strip()
                if not line:
                    continue
                records.append(json.loads(line))
        return records


class BinarySensorDataSource:
    """Raw binary ingestion agent for telemetry/sensor streams."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> bytes:
        with open(self.file_path, "rb") as stream:
            return stream.read()


class DataManifest:
    """
    Standardized manifest layer that decouples ingestion from execution.

    Any source (CSV, JSONL, binary telemetry, in-memory arrays) is normalized
    to a StreamVector so the Core execution manifold does not require source-specific logic.
    """

    def __init__(self, stream_vector: StreamVector) -> None:
        self.stream_vector = stream_vector

    @classmethod
    def from_source(
        cls, source: Any, source_type: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None
    ) -> "DataManifest":
        source_kind = source_type or cls._infer_source_type(source)
        metadata = metadata or {}
        payload = cls._materialize_payload(source, source_kind)
        merged_metadata = {
            "source_kind": source_kind,
            "byte_size": cls._estimate_size(payload),
            **metadata,
        }
        return cls(StreamVector(source_type=source_kind, payload=payload, metadata=merged_metadata))

    @staticmethod
    def _infer_source_type(source: Any) -> str:
        if isinstance(source, (bytes, bytearray)):
            return "binary"
        if isinstance(source, np.ndarray):
            return "ndarray"
        if isinstance(source, str):
            lowered = source.lower()
            if lowered.endswith(".csv"):
                return "csv"
            if lowered.endswith(".jsonl"):
                return "jsonl"
            return "text"
        if isinstance(source, list):
            return "list"
        if isinstance(source, dict):
            return "dict"
        return "generic"

    @staticmethod
    def _materialize_payload(source: Any, source_kind: str) -> Any:
        if source_kind == "csv" and isinstance(source, str):
            return CSVDataSource(source).read()
        if source_kind == "jsonl" and isinstance(source, str):
            return JSONLDataSource(source).read()
        if source_kind == "binary" and isinstance(source, str):
            return BinarySensorDataSource(source).read()
        return source

    @staticmethod
    def _estimate_size(payload: Any) -> int:
        if isinstance(payload, np.ndarray):
            return int(payload.nbytes)
        if isinstance(payload, (bytes, bytearray)):
            return int(len(payload))
        if isinstance(payload, str):
            return int(len(payload.encode("utf-8")))
        if isinstance(payload, list):
            return int(sum(DataManifest._estimate_size(item) for item in payload))
        if isinstance(payload, dict):
            return int(DataManifest._estimate_size(json.dumps(payload)))
        return 0

    def to_stream_vector(self) -> StreamVector:
        return self.stream_vector
