"""Runtime Control Plane contract for OPG.

The Runtime Control Plane coordinates high-level runtime lifecycle operations.

This module defines the public contract only. Concrete lifecycle orchestration
will be implemented in later M-015 tickets.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class RuntimeControlState(str, Enum):
    """Lifecycle states managed by the runtime control plane."""

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    RESTARTING = "restarting"
    FAILED = "failed"


class RuntimeControlPlane(ABC):
    """Abstract contract for runtime lifecycle orchestration."""

    @abstractmethod
    def start(self) -> None:
        """Start the runtime."""

    @abstractmethod
    def stop(self) -> None:
        """Stop the runtime."""

    @abstractmethod
    def restart(self) -> None:
        """Restart the runtime."""

    @abstractmethod
    def get_state(self) -> RuntimeControlState:
        """Return the current runtime control state."""