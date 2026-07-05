"""Runtime lifecycle coordination system."""

from __future__ import annotations

from .control_plane import RuntimeControlState
from .control_plane_impl import DefaultRuntimeControlPlane


class RuntimeLifecycleCoordinator:
    """Coordinates runtime lifecycle operations through a control plane."""

    def __init__(self, control_plane: DefaultRuntimeControlPlane) -> None:
        self._control_plane = control_plane

    def start(self) -> RuntimeControlState:
        """Start the runtime through the control plane."""
        self._control_plane.start()
        return self._control_plane.get_state()

    def stop(self) -> RuntimeControlState:
        """Stop the runtime through the control plane."""
        self._control_plane.stop()
        return self._control_plane.get_state()

    def restart(self) -> RuntimeControlState:
        """Restart the runtime through the control plane."""
        self._control_plane.restart()
        return self._control_plane.get_state()

    def fail(self) -> RuntimeControlState:
        """Mark the runtime as failed through the control plane."""
        self._control_plane.fail()
        return self._control_plane.get_state()

    def get_state(self) -> RuntimeControlState:
        """Return the current runtime control state."""
        return self._control_plane.get_state()