"""Driver interface contract for OPG external runtime drivers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DriverInterface(ABC):
    """Abstract contract implemented by all OPG external drivers.

    A driver is responsible for adapting OPG runtime/project instructions
    to a concrete external environment such as Blender, Unreal, Unity,
    Godot, or a test/null runtime.

    This interface must remain technology-agnostic.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the unique driver name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        """Return the driver implementation version."""
        raise NotImplementedError

    @abstractmethod
    def initialize(self, context: Any | None = None) -> None:
        """Initialize the driver with an optional runtime context."""
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the driver and release any external resources."""
        raise NotImplementedError

    @abstractmethod
    def is_available(self) -> bool:
        """Return whether the driver can run in the current environment."""
        raise NotImplementedError