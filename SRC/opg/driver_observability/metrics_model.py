"""Metrics model for runtime observability system."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Metric:
    """Represents a runtime metric."""

    name: str
    value: float
    tags: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert metric to dictionary format."""
        return {
            "name": self.name,
            "value": self.value,
            "tags": self.tags,
        }