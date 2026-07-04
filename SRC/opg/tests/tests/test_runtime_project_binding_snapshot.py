"""Tests for runtime project binding snapshot."""

from opg.runtime.project_binding_snapshot import RuntimeProjectBindingSnapshot
from opg.runtime.project_binding_state import RuntimeProjectBindingState


class DummyProject:
    """Minimal project-like object used for snapshot tests."""


def test_bound_snapshot_preserves_project():
    project = DummyProject()

    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.BOUND,
        project=project,
    )

    assert snapshot.project is project


def test_bound_snapshot_has_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.BOUND,
        project=DummyProject(),
    )

    assert snapshot.has_project() is True


def test_unbound_snapshot_has_no_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.UNBOUND,
        project=None,
    )

    assert snapshot.has_project() is False


def test_snapshot_preserves_state():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.UNBOUND,
        project=None,
    )

    assert snapshot.state == RuntimeProjectBindingState.UNBOUND


def test_snapshot_is_immutable():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.UNBOUND,
        project=None,
    )

    try:
        snapshot.project = DummyProject()
    except Exception:
        pass

    assert snapshot.project is None