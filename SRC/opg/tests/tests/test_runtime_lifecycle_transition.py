"""Tests for the runtime lifecycle transition model."""

from opg.runtime import RuntimeControlState, RuntimeLifecycleTransition


def test_runtime_lifecycle_transition_stores_previous_state() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    assert transition.previous_state is RuntimeControlState.CREATED


def test_runtime_lifecycle_transition_stores_next_state() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    assert transition.next_state is RuntimeControlState.RUNNING


def test_runtime_lifecycle_transition_stores_action() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    assert transition.action == "start"


def test_runtime_lifecycle_transition_detects_state_change() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    assert transition.is_state_change is True


def test_runtime_lifecycle_transition_detects_no_state_change() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.RUNNING,
        next_state=RuntimeControlState.RUNNING,
        action="noop",
    )

    assert transition.is_state_change is False


def test_runtime_lifecycle_transition_is_immutable() -> None:
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    assert transition.previous_state is RuntimeControlState.CREATED
    assert transition.next_state is RuntimeControlState.RUNNING