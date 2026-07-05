"""Logging model for runtime observability system."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class LogEntry:
    """Represents a structured log entry."""

    level: str
    message: str
    context: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        """Convert log entry to dictionary."""
        return {
            "level": self.level,
            "message": self.message,
            "context": self.context,
            "timestamp": self.timestamp.isoformat(),
        }