"""Dependency edge model for runtime state graph."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DependencyEdge:
    """Represents a dependency between two state nodes."""

    source: str
    target: str
    weight: float = 1.0