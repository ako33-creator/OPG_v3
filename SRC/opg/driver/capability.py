"""Driver capability model for OPG external runtime drivers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DriverCapability:
    """Represents one capability supported by an OPG driver.

    Capabilities describe what a driver can do without binding OPG to
    a specific external technology.
    """

    name: str
    description: str = ""
    enabled: bool = True

    def is_enabled(self) -> bool:
        """Return whether this capability is enabled."""
        return self.enabled