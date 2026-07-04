"""Runtime project binding status object."""

from __future__ import annotations

from dataclasses import dataclass

from .project_binding_state import RuntimeProjectBindingState


@dataclass(frozen=True)
class RuntimeProjectBindingStatus:
    """Immutable status for the runtime project binding."""

    state: RuntimeProjectBindingState

    def is_bound(self) -> bool:
        """Return whether the runtime is currently bound to a project."""
        return self.state == RuntimeProjectBindingState.BOUND