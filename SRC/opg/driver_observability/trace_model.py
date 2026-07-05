"""Trace model for runtime observability system."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class Trace:
    """Represents a runtime trace event."""

    name: str
    data: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        """Convert trace to dictionary format."""
        return {
            "name": self.name,
            "data": self.data,
            "timestamp": self.timestamp.isoformat(),
        }