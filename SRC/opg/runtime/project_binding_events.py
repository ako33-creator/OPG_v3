"""Runtime project binding event definitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RuntimeProjectBoundEvent:
    """Event emitted when the runtime is bound to a project model."""

    project: Any


@dataclass(frozen=True)
class RuntimeProjectUnboundEvent:
    """Event emitted when the runtime is unbound from a project model."""

    project: Any