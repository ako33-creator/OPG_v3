"""Null driver implementation for OPG external runtime drivers."""

from __future__ import annotations

from typing import Any

from .interface import DriverInterface


class NullDriver(DriverInterface):
    """Technology-agnostic no-op driver implementation.

    The null driver is useful for tests, dry runs, and environments where
    no external runtime driver is available.
    """

    @property
    def name(self) -> str:
        """Return the null driver name."""
        return "null"

    @property
    def version(self) -> str:
        """Return the null driver version."""
        return "0.1.0"

    def initialize(self, context: Any | None = None) -> None:
        """Initialize the null driver without side effects."""

    def shutdown(self) -> None:
        """Shutdown the null driver without side effects."""

    def is_available(self) -> bool:
        """Return whether the null driver is available."""
        return True