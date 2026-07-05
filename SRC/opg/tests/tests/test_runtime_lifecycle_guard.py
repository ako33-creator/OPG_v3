"""Tests for the runtime lifecycle guard."""

from opg.runtime import (
    DefaultRuntimeLifecyclePolicy,
    RuntimeControlState,
    RuntimeLifecycleGuard,
)


def test_runtime_lifecycle_guard_allows_start_when_policy_allows_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_start(RuntimeControlState.CREATED) is True


def test_runtime_lifecycle_guard_rejects_start_when_policy_rejects_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_start(RuntimeControlState.RUNNING) is False


def test_runtime_lifecycle_guard_allows_stop_when_policy_allows_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_stop(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_guard_rejects_stop_when_policy_rejects_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_stop(RuntimeControlState.CREATED) is False


def test_runtime_lifecycle_guard_allows_restart_when_policy_allows_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_restart(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_guard_rejects_restart_when_policy_rejects_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_restart(RuntimeControlState.STOPPED) is False


def test_runtime_lifecycle_guard_allows_fail_when_policy_allows_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_fail(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_guard_rejects_fail_when_policy_rejects_it() -> None:
    policy = DefaultRuntimeLifecyclePolicy()
    guard = RuntimeLifecycleGuard(policy)

    assert guard.can_fail(RuntimeControlState.FAILED) is False