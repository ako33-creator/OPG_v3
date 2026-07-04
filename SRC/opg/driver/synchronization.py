"""Driver synchronization contract for OPG external runtime drivers."""

from __future__ import annotations

from typing import Any, Protocol


class DriverSynchronizationContract(Protocol):
    """Technology-agnostic synchronization contract for OPG drivers."""

    def synchronize_from_project(self, project: Any) -> None:
        """Synchronize the external runtime from an OPG project."""
        ...

    def synchronize_to_project(self, project: Any) -> None:
        """Synchronize an OPG project from the external runtime."""
        ...