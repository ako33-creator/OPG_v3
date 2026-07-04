"""Driver lifecycle hooks for OPG external runtime drivers."""

from __future__ import annotations

from typing import Protocol


class DriverLifecycleHooks(Protocol):
    """Optional lifecycle hooks implemented by OPG drivers."""

    def before_initialize(self) -> None:
        """Run before driver initialization."""
        ...

    def after_initialize(self) -> None:
        """Run after driver initialization."""
        ...

    def before_shutdown(self) -> None:
        """Run before driver shutdown."""
        ...

    def after_shutdown(self) -> None:
        """Run after driver shutdown."""
        ...