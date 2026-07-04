"""Driver result model for OPG external runtime drivers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class DriverResult:
    """Represents the result returned by an OPG driver command."""

    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    message: str = ""

    def has_data(self) -> bool:
        """Return whether the result contains data."""
        return bool(self.data)

    def is_success(self) -> bool:
        """Return whether the driver operation succeeded."""
        return self.success