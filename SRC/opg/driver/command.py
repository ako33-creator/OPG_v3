"""Driver command model for OPG external runtime drivers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class DriverCommand:
    """Represents a technology-agnostic command sent to an OPG driver."""

    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    command_id: str = field(default_factory=lambda: str(uuid4()))

    def has_payload(self) -> bool:
        """Return whether the command carries payload data."""
        return bool(self.payload)