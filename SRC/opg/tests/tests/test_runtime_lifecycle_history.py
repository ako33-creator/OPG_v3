"""Tests for the runtime lifecycle transition history."""

from opg.runtime import (
    RuntimeControlState,
    RuntimeLifecycleHistory,
    RuntimeLifecycleTransition,
)


def test_runtime_lifecycle_history_is_initially_empty() -> None:
    history = RuntimeLifecycleHistory()

    assert len(history) == 0
    assert history.get_transitions() == ()
    assert history.get_last_transition() is None


def test_runtime_lifecycle_history_records_transition() -> None:
    history = RuntimeLifecycleHistory()
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    history.record(transition)

    assert len(history) == 1
    assert history.get_transitions() == (transition,)


def test_runtime_lifecycle_history_preserves_insertion_order() -> None:
    history = RuntimeLifecycleHistory()
    first_transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )
    second_transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.RUNNING,
        next_state=RuntimeControlState.STOPPED,
        action="stop",
    )

    history.record(first_transition)
    history.record(second_transition)

    assert history.get_transitions() == (
        first_transition,
        second_transition,
    )


def test_runtime_lifecycle_history_returns_last_transition() -> None:
    history = RuntimeLifecycleHistory()
    first_transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )
    second_transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.RUNNING,
        next_state=RuntimeControlState.STOPPED,
        action="stop",
    )

    history.record(first_transition)
    history.record(second_transition)

    assert history.get_last_transition() is second_transition


def test_runtime_lifecycle_history_clear_removes_transitions() -> None:
    history = RuntimeLifecycleHistory()
    transition = RuntimeLifecycleTransition(
        previous_state=RuntimeControlState.CREATED,
        next_state=RuntimeControlState.RUNNING,
        action="start",
    )

    history.record(transition)
    history.clear()

    assert len(history) == 0
    assert history.get_transitions() == ()
    assert history.get_last_transition() is None