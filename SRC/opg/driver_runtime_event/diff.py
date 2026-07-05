"""Diff model for driver runtime events."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RuntimeDiff:
    """Represents a difference detected in runtime state."""

    path: str
    old_value: Any
    new_value: Any