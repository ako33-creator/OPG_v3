"""Operation model for driver runtime synchronization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DriverRuntimeSyncOperation:
    """Represent a synchronization operation."""

    name: str
    source: Any
    target: Any