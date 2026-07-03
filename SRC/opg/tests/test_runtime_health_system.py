import pytest

from opg.runtime.runtime_health_system import (
    RuntimeHealthCheck,
    RuntimeHealthStatus,
    RuntimeHealthSystem,
)


def test_health_system_starts_healthy():
    health = RuntimeHealthSystem()

    assert health.overall_status() == RuntimeHealthStatus.HEALTHY
    assert health.checks() == {}


def test_health_system_registers_check():
    health = RuntimeHealthSystem()

    check = health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    assert isinstance(check, RuntimeHealthCheck)
    assert check.name == "database"
    assert check.status == RuntimeHealthStatus.HEALTHY


def test_health_system_returns_registered_check():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    check = health.get_check("database")

    assert check.name == "database"


def test_health_system_raises_for_unknown_check():
    health = RuntimeHealthSystem()

    with pytest.raises(KeyError):
        health.get_check("missing")


def test_health_system_detects_degraded():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.DEGRADED,
    )

    assert health.overall_status() == RuntimeHealthStatus.DEGRADED


def test_health_system_detects_unhealthy():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    health.register_check(
        "plugins",
        RuntimeHealthStatus.UNHEALTHY,
    )

    assert health.overall_status() == RuntimeHealthStatus.UNHEALTHY


def test_health_system_removes_check():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    health.remove_check("database")

    assert health.has_check("database") is False


def test_health_system_returns_copy():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    snapshot = health.checks()
    snapshot.clear()

    assert len(health.checks()) == 1


def test_health_system_clear():
    health = RuntimeHealthSystem()

    health.register_check(
        "database",
        RuntimeHealthStatus.HEALTHY,
    )

    health.clear()

    assert health.checks() == {}