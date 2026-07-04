"""Driver selection policy for OPG external runtime drivers."""

from __future__ import annotations

from .interface import DriverInterface
from .registry import DriverRegistry


class DriverSelectionPolicy:
    """Selects an available driver from a driver registry."""

    def select(self, registry: DriverRegistry, preferred_name: str | None = None) -> DriverInterface | None:
        """Select a driver using an optional preferred driver name."""
        if preferred_name is not None:
            preferred_driver = registry.get(preferred_name)
            if preferred_driver is not None and preferred_driver.is_available():
                return preferred_driver
            return None

        for name in registry.list_names():
            driver = registry.get(name)
            if driver is not None and driver.is_available():
                return driver

        return None