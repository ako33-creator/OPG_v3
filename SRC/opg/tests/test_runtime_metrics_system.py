import pytest

from opg.runtime.runtime_metrics_system import (
    RuntimeMetric,
    RuntimeMetricsSystem,
)


def test_metrics_system_starts_empty():
    metrics = RuntimeMetricsSystem()

    assert metrics.metrics() == {}


def test_metrics_system_registers_metric():
    metrics = RuntimeMetricsSystem()

    metric = metrics.set_metric("runtime.tasks", 5)

    assert isinstance(metric, RuntimeMetric)
    assert metric.name == "runtime.tasks"
    assert metric.value == 5.0


def test_metrics_system_has_metric():
    metrics = RuntimeMetricsSystem()

    metrics.set_metric("runtime.tasks", 3)

    assert metrics.has_metric("runtime.tasks") is True


def test_metrics_system_returns_metric():
    metrics = RuntimeMetricsSystem()

    metrics.set_metric("runtime.tasks", 12)

    metric = metrics.get_metric("runtime.tasks")

    assert metric.value == 12.0


def test_metrics_system_raises_for_unknown_metric():
    metrics = RuntimeMetricsSystem()

    with pytest.raises(KeyError):
        metrics.get_metric("unknown")


def test_metrics_system_removes_metric():
    metrics = RuntimeMetricsSystem()

    metrics.set_metric("runtime.tasks", 7)
    metrics.remove_metric("runtime.tasks")

    assert metrics.has_metric("runtime.tasks") is False


def test_metrics_system_returns_copy():
    metrics = RuntimeMetricsSystem()

    metrics.set_metric("runtime.tasks", 2)

    snapshot = metrics.metrics()
    snapshot.clear()

    assert len(metrics.metrics()) == 1


def test_metrics_system_clear():
    metrics = RuntimeMetricsSystem()

    metrics.set_metric("a", 1)
    metrics.set_metric("b", 2)

    metrics.clear()

    assert metrics.metrics() == {}