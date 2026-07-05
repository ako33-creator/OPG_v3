"""Factory for driver runtime synchronization."""

from __future__ import annotations

from .contract import DriverRuntimeSync
from .registry import DriverRuntimeSyncRegistry


class DriverRuntimeSyncFactory:
    """Create and manage synchronization instances."""

    def __init__(self, registry: DriverRuntimeSyncRegistry) -> None:
        self.registry = registry

    def create(self, name: str, sync: DriverRuntimeSync) -> None:
        """Create and register a synchronization instance."""
        self.registry.register(name, sync)

    def get(self, name: str) -> DriverRuntimeSync | None:
        """Retrieve a synchronization instance by name."""
        return self.registry.get(name)