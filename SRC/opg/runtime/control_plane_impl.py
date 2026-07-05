"""Default Runtime Control Plane implementation for OPG."""

from __future__ import annotations

from .control_plane import RuntimeControlPlane, RuntimeControlState
from .control_state import RuntimeControlSnapshot


class DefaultRuntimeControlPlane(RuntimeControlPlane):
    """Default in-memory implementation of the Runtime Control Plane."""

    def __init__(self) -> None:
        self._state = RuntimeControlState.CREATED
        self._restart_count = 0
        self._failure_count = 0

    def start(self) -> None:
        """Start the runtime."""
        if self._state is RuntimeControlState.RUNNING:
            return

        self._state = RuntimeControlState.STARTING
        self._state = RuntimeControlState.RUNNING

    def stop(self) -> None:
        """Stop the runtime."""
        if self._state is RuntimeControlState.STOPPED:
            return

        self._state = RuntimeControlState.STOPPING
        self._state = RuntimeControlState.STOPPED

    def restart(self) -> None:
        """Restart the runtime."""
        self._restart_count += 1
        self._state = RuntimeControlState.RESTARTING
        self.stop()
        self.start()

    def fail(self) -> None:
        """Mark the runtime as failed."""
        self._failure_count += 1
        self._state = RuntimeControlState.FAILED

    def get_state(self) -> RuntimeControlState:
        """Return the current runtime control state."""
        return self._state

    def get_snapshot(self) -> RuntimeControlSnapshot:
        """Return an immutable snapshot of the runtime control state."""
        return RuntimeControlSnapshot(
            state=self._state,
            restart_count=self._restart_count,
            failure_count=self._failure_count,
        )