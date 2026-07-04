"""Driver runtime adapter for OPG external runtime drivers."""

from __future__ import annotations

from typing import Any

from .interface import DriverInterface


class DriverRuntimeAdapter:
    """Adapts an OPG driver to runtime lifecycle operations."""

    def __init__(self, driver: DriverInterface) -> None:
        """Initialize the adapter with a driver."""
        self.driver = driver

    def start(self, context: Any | None = None) -> None:
        """Start the adapted driver."""
        self.driver.initialize(context)

    def stop(self) -> None:
        """Stop the adapted driver."""
        self.driver.shutdown()

    def is_available(self) -> bool:
        """Return whether the adapted driver is available."""
        return self.driver.is_available()