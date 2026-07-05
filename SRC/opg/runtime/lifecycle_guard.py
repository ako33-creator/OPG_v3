"""Runtime lifecycle transition guard."""

from __future__ import annotations

from .control_plane import RuntimeControlState
from .lifecycle_policy import RuntimeLifecyclePolicy


class RuntimeLifecycleGuard:
    """Guards runtime lifecycle transitions using a lifecycle policy."""

    def __init__(self, policy: RuntimeLifecyclePolicy) -> None:
        self._policy = policy

    def can_start(self, state: RuntimeControlState) -> bool:
        """Return whether start is allowed from the current state."""
        return self._policy.can_start(state)

    def can_stop(self, state: RuntimeControlState) -> bool:
        """Return whether stop is allowed from the current state."""
        return self._policy.can_stop(state)

    def can_restart(self, state: RuntimeControlState) -> bool:
        """Return whether restart is allowed from the current state."""
        return self._policy.can_restart(state)

    def can_fail(self, state: RuntimeControlState) -> bool:
        """Return whether failure transition is allowed from the current state."""
        return self._policy.can_fail(state)