import pytest

from opg.runtime.runtime_recovery_system import (
    RuntimeRecoveryResult,
    RuntimeRecoveryState,
    RuntimeRecoverySystem,
)


def test_recovery_system_starts_idle():
    recovery = RuntimeRecoverySystem()

    assert recovery.state == RuntimeRecoveryState.IDLE
    assert recovery.last_result is None


def test_recovery_system_registers_action():
    recovery = RuntimeRecoverySystem()

    recovery.register_action("restart.scheduler", lambda: None)

    assert recovery.has_action("restart.scheduler") is True


def test_recovery_system_rejects_duplicate_action():
    recovery = RuntimeRecoverySystem()

    recovery.register_action("restart.scheduler", lambda: None)

    with pytest.raises(ValueError):
        recovery.register_action("restart.scheduler", lambda: None)


def test_recovery_system_recovers_registered_action():
    recovery = RuntimeRecoverySystem()
    executed = []

    recovery.register_action(
        "restart.scheduler",
        lambda: executed.append("restart.scheduler"),
    )

    result = recovery.recover("restart.scheduler")

    assert executed == ["restart.scheduler"]
    assert isinstance(result, RuntimeRecoveryResult)
    assert result.state == RuntimeRecoveryState.RECOVERED
    assert result.error is None
    assert recovery.state == RuntimeRecoveryState.RECOVERED
    assert recovery.last_result == result


def test_recovery_system_raises_for_unknown_action():
    recovery = RuntimeRecoverySystem()

    with pytest.raises(KeyError):
        recovery.recover("missing")


def test_recovery_system_returns_failed_result_on_error():
    recovery = RuntimeRecoverySystem()

    def failing_action():
        raise RuntimeError("boom")

    recovery.register_action("restart.scheduler", failing_action)

    result = recovery.recover("restart.scheduler")

    assert result.state == RuntimeRecoveryState.FAILED
    assert isinstance(result.error, RuntimeError)
    assert recovery.state == RuntimeRecoveryState.FAILED
    assert recovery.last_result == result


def test_recovery_system_reset_returns_to_idle():
    recovery = RuntimeRecoverySystem()

    recovery.register_action("restart.scheduler", lambda: None)
    recovery.recover("restart.scheduler")

    recovery.reset()

    assert recovery.state == RuntimeRecoveryState.IDLE
    assert recovery.last_result is None
    assert recovery.has_action("restart.scheduler") is True


def test_recovery_system_clear_removes_actions_and_resets_state():
    recovery = RuntimeRecoverySystem()

    recovery.register_action("restart.scheduler", lambda: None)
    recovery.recover("restart.scheduler")

    recovery.clear()

    assert recovery.state == RuntimeRecoveryState.IDLE
    assert recovery.last_result is None
    assert recovery.has_action("restart.scheduler") is False