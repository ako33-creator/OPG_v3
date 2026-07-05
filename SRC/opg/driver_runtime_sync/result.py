"""Result model for driver runtime synchronization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DriverRuntimeSyncResult:
    """Represent the result of a driver runtime synchronization."""

    success: bool
    source: Any
    target: Any
    message: str = ""