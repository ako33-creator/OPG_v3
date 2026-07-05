"""Registry for driver runtime synchronization services."""

from __future__ import annotations

from .contract import DriverRuntimeSync


class DriverRuntimeSyncRegistry:
    """Register and retrieve driver runtime synchronization services."""

    def __init__(self) -> None:
        self._items: dict[str, DriverRuntimeSync] = {}

    def register(self, name: str, sync: DriverRuntimeSync) -> None:
        """Register a synchronization service by name."""
        self._items[name] = sync

    def get(self, name: str) -> DriverRuntimeSync | None:
        """Return a synchronization service by name."""
        return self._items.get(name)

    def all(self) -> dict[str, DriverRuntimeSync]:
        """Return all registered synchronization services."""
        return dict(self._items)