"""Runtime Control Plane state model for OPG."""

from __future__ import annotations

from dataclasses import dataclass

from .control_plane import RuntimeControlState


@dataclass(frozen=True, slots=True)
class RuntimeControlSnapshot:
    """Immutable snapshot of the Runtime Control Plane state."""

    state: RuntimeControlState
    restart_count: int = 0
    failure_count: int = 0

    @property
    def is_running(self) -> bool:
        """Return whether the runtime is currently running."""
        return self.state is RuntimeControlState.RUNNING

    @property
    def is_failed(self) -> bool:
        """Return whether the runtime is currently failed."""
        return self.state is RuntimeControlState.FAILED