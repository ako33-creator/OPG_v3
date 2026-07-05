"""Bootstrap helper for driver runtime synchronization layer."""

from __future__ import annotations

from .factory import DriverRuntimeSyncFactory
from .registry import DriverRuntimeSyncRegistry


class DriverRuntimeSyncBootstrap:
    """Prepare driver runtime synchronization services."""

    def __init__(
        self,
        registry: DriverRuntimeSyncRegistry | None = None,
        factory: DriverRuntimeSyncFactory | None = None,
    ) -> None:
        self.registry = registry or DriverRuntimeSyncRegistry()
        self.factory = factory or DriverRuntimeSyncFactory(self.registry)

    def bootstrap(self) -> DriverRuntimeSyncFactory:
        """Return a ready-to-use synchronization factory."""
        return self.factory