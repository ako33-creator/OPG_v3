"""State model for driver runtime synchronization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DriverRuntimeSyncState:
    """Represent the state of a driver runtime synchronization."""

    source: Any
    target: Any
    is_synchronized: bool = False