"""Runtime lifecycle transition model."""

from __future__ import annotations

from dataclasses import dataclass

from .control_plane import RuntimeControlState


@dataclass(frozen=True)
class RuntimeLifecycleTransition:
    """Represents a runtime lifecycle transition."""

    previous_state: RuntimeControlState
    next_state: RuntimeControlState
    action: str

    @property
    def is_state_change(self) -> bool:
        """Return whether the transition changes the runtime state."""
        return self.previous_state is not self.next_state