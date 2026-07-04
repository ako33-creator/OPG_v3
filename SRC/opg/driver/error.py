"""Driver error model for OPG external runtime drivers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DriverError:
    """Represents a technology-agnostic driver error."""

    code: str
    message: str
    recoverable: bool = False

    def is_recoverable(self) -> bool:
        """Return whether the driver error can be recovered from."""
        return self.recoverable