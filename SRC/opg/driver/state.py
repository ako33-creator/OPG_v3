"""Driver state model for OPG external runtime drivers."""

from __future__ import annotations

from enum import Enum


class DriverState(str, Enum):
    """Lifecycle states for an OPG driver."""

    CREATED = "created"
    INITIALIZED = "initialized"
    RUNNING = "running"
    STOPPED = "stopped"
    FAILED = "failed"