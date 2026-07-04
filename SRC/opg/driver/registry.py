"""Driver registry for OPG external runtime drivers."""

from __future__ import annotations

from typing import Dict

from .interface import DriverInterface


class DriverRegistry:
    """Registry storing available OPG drivers by name."""

    def __init__(self) -> None:
        """Initialize an empty driver registry."""
        self._drivers: Dict[str, DriverInterface] = {}

    def register(self, driver: DriverInterface) -> None:
        """Register a driver by its unique name."""
        self._drivers[driver.name] = driver

    def unregister(self, name: str) -> None:
        """Remove a driver from the registry if it exists."""
        self._drivers.pop(name, None)

    def get(self, name: str) -> DriverInterface | None:
        """Return a registered driver by name."""
        return self._drivers.get(name)

    def has(self, name: str) -> bool:
        """Return whether a driver is registered."""
        return name in self._drivers

    def list_names(self) -> list[str]:
        """Return all registered driver names."""
        return list(self._drivers.keys())