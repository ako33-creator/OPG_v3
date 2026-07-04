"""Snapshot object for runtime project binding state."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from .project_binding_state import RuntimeProjectBindingState


@dataclass(frozen=True)
class RuntimeProjectBindingSnapshot:
    """Immutable snapshot of the runtime project binding."""

    state: RuntimeProjectBindingState
    project: Optional[Any]

    def has_project(self) -> bool:
        """Return whether the snapshot contains a project reference."""
        return self.project is not None