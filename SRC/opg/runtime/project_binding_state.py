"""Runtime project binding state definitions."""

from __future__ import annotations

from enum import Enum


class RuntimeProjectBindingState(str, Enum):
    """Known states for runtime project binding lifecycle."""

    UNBOUND = "unbound"
    BOUND = "bound"