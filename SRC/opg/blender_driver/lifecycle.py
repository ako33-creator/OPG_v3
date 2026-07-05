"""Lifecycle wiring for the Blender driver."""

from opg.driver.lifecycle import DriverLifecycleState


class BlenderDriverLifecycle:
    """Manages Blender driver lifecycle state."""

    def __init__(self) -> None:
        """Initialize the Blender driver lifecycle."""
        self._state = DriverLifecycleState.CREATED

    @property
    def state(self) -> DriverLifecycleState:
        """Return the current lifecycle state."""
        return self._state

    def initialize(self) -> None:
        """Initialize the Blender driver."""
        self._state = DriverLifecycleState.INITIALIZED

    def start(self) -> None:
        """Start the Blender driver."""
        self._state = DriverLifecycleState.STARTED

    def stop(self) -> None:
        """Stop the Blender driver."""
        self._state = DriverLifecycleState.STOPPED

    def shutdown(self) -> None:
        """Shutdown the Blender driver."""
        self._state = DriverLifecycleState.SHUTDOWN