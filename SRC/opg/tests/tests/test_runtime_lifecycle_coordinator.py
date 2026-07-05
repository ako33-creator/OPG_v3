"""Tests for the runtime lifecycle coordinator."""

from opg.runtime import (
    DefaultRuntimeControlPlane,
    RuntimeControlState,
    RuntimeLifecycleCoordinator,
)


def test_runtime_lifecycle_coordinator_initial_state() -> None:
    control_plane = DefaultRuntimeControlPlane()
    coordinator = RuntimeLifecycleCoordinator(control_plane)

    assert coordinator.get_state() is RuntimeControlState.CREATED


def test_runtime_lifecycle_coordinator_starts_runtime() -> None:
    control_plane = DefaultRuntimeControlPlane()
    coordinator = RuntimeLifecycleCoordinator(control_plane)

    state = coordinator.start()

    assert state is RuntimeControlState.RUNNING
    assert coordinator.get_state() is RuntimeControlState.RUNNING


def test_runtime_lifecycle_coordinator_stops_runtime() -> None:
    control_plane = DefaultRuntimeControlPlane()
    coordinator = RuntimeLifecycleCoordinator(control_plane)

    coordinator.start()
    state = coordinator.stop()

    assert state is RuntimeControlState.STOPPED
    assert coordinator.get_state() is RuntimeControlState.STOPPED


def test_runtime_lifecycle_coordinator_restarts_runtime() -> None:
    control_plane = DefaultRuntimeControlPlane()
    coordinator = RuntimeLifecycleCoordinator(control_plane)

    coordinator.start()
    state = coordinator.restart()

    assert state is RuntimeControlState.RUNNING
    assert coordinator.get_state() is RuntimeControlState.RUNNING


def test_runtime_lifecycle_coordinator_marks_runtime_failed() -> None:
    control_plane = DefaultRuntimeControlPlane()
    coordinator = RuntimeLifecycleCoordinator(control_plane)

    state = coordinator.fail()

    assert state is RuntimeControlState.FAILED
    assert coordinator.get_state() is RuntimeControlState.FAILED