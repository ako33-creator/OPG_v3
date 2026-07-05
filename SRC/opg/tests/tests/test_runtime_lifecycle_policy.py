"""Tests for the runtime lifecycle policy system."""

from opg.runtime import (
    DefaultRuntimeLifecyclePolicy,
    RuntimeControlState,
    RuntimeLifecyclePolicy,
)


def test_default_runtime_lifecycle_policy_is_runtime_lifecycle_policy() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert isinstance(policy, RuntimeLifecyclePolicy)


def test_runtime_lifecycle_policy_allows_start_from_created() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_start(RuntimeControlState.CREATED) is True


def test_runtime_lifecycle_policy_allows_start_from_stopped() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_start(RuntimeControlState.STOPPED) is True


def test_runtime_lifecycle_policy_allows_start_from_failed() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_start(RuntimeControlState.FAILED) is True


def test_runtime_lifecycle_policy_rejects_start_from_running() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_start(RuntimeControlState.RUNNING) is False


def test_runtime_lifecycle_policy_allows_stop_from_running() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_stop(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_policy_rejects_stop_from_created() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_stop(RuntimeControlState.CREATED) is False


def test_runtime_lifecycle_policy_allows_restart_from_running() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_restart(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_policy_allows_restart_from_failed() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_restart(RuntimeControlState.FAILED) is True


def test_runtime_lifecycle_policy_rejects_restart_from_stopped() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_restart(RuntimeControlState.STOPPED) is False


def test_runtime_lifecycle_policy_allows_fail_from_running() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_fail(RuntimeControlState.RUNNING) is True


def test_runtime_lifecycle_policy_rejects_fail_from_failed() -> None:
    policy = DefaultRuntimeLifecyclePolicy()

    assert policy.can_fail(RuntimeControlState.FAILED) is False