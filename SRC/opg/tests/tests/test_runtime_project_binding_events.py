"""Tests for runtime project binding events."""

from opg.runtime.project_binding_events import (
    RuntimeProjectBoundEvent,
    RuntimeProjectUnboundEvent,
)


class DummyProject:
    """Minimal project-like object used for event tests."""


def test_bound_event_preserves_project():
    project = DummyProject()

    event = RuntimeProjectBoundEvent(project=project)

    assert event.project is project


def test_unbound_event_preserves_project():
    project = DummyProject()

    event = RuntimeProjectUnboundEvent(project=project)

    assert event.project is project


def test_bound_event_is_immutable():
    project = DummyProject()
    other_project = DummyProject()
    event = RuntimeProjectBoundEvent(project=project)

    try:
        event.project = other_project
    except Exception:
        pass

    assert event.project is project


def test_unbound_event_is_immutable():
    project = DummyProject()
    other_project = DummyProject()
    event = RuntimeProjectUnboundEvent(project=project)

    try:
        event.project = other_project
    except Exception:
        pass

    assert event.project is project
    