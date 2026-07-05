"""Trace collector for runtime observability system."""

from __future__ import annotations

from typing import Any

from .trace_model import Trace


class TraceCollector:
    """Collects runtime trace events."""

    def __init__(self) -> None:
        self.traces: list[Trace] = []

    def collect(self, trace: Trace) -> None:
        """Store a trace event."""
        self.traces.append(trace)

    def query(self, name: str | None = None) -> list[dict[str, Any]]:
        """Return traces optionally filtered by name."""
        if name is None:
            return [t.to_dict() for t in self.traces]

        return [t.to_dict() for t in self.traces if t.name == name]