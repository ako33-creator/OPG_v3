"""Tests for runtime project binding snapshotter."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from opg.runtime.project_binding_state import RuntimeProjectBindingState


class DummyProject:
    """Minimal project-like object used for snapshotter tests."""


def test_snapshotter_returns_unbound_snapshot_without_binding():
    registry = RuntimeProjectBindingRegistry()
    snapshotter = RuntimeProjectBindingSnapshotter(registry)

    snapshot = snapshotter.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.UNBOUND
    assert snapshot.project is None
    assert snapshot.has_project() is False


def test_snapshotter_returns_bound_snapshot_with_project():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    snapshotter = RuntimeProjectBindingSnapshotter(registry)

    snapshot = snapshotter.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.BOUND
    assert snapshot.project is project
    assert snapshot.has_project() is True


def test_snapshotter_reflects_binding_replacement():
    first_project = DummyProject()
    second_project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    snapshotter = RuntimeProjectBindingSnapshotter(registry)

    registry.bind(RuntimeProjectBinding(project=first_project))
    first_snapshot = snapshotter.snapshot()

    registry.bind(RuntimeProjectBinding(project=second_project))
    second_snapshot = snapshotter.snapshot()

    assert first_snapshot.project is first_project
    assert second_snapshot.project is second_project


def test_snapshotter_reflects_binding_clear():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    snapshotter = RuntimeProjectBindingSnapshotter(registry)

    registry.clear()
    snapshot = snapshotter.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.UNBOUND
    assert snapshot.project is None