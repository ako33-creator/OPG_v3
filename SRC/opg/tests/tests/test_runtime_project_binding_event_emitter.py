"""Tests for runtime project binding event emitter."""

from opg.runtime.project_binding_event_emitter import (
    RuntimeProjectBindingEventEmitter,
)
from opg.runtime.project_binding_events import (
    RuntimeProjectBoundEvent,
    RuntimeProjectUnboundEvent,
)


class DummyProject:
    """Minimal project-like object used for emitter tests."""


def test_emitter_emits_bound_event():
    emitted_events = []
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    event = RuntimeProjectBoundEvent(project=DummyProject())

    emitter.emit_bound(event)

    assert emitted_events == [event]


def test_emitter_emits_unbound_event():
    emitted_events = []
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    event = RuntimeProjectUnboundEvent(project=DummyProject())

    emitter.emit_unbound(event)

    assert emitted_events == [event]


def test_emitter_preserves_bound_event_identity():
    emitted_events = []
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    event = RuntimeProjectBoundEvent(project=DummyProject())

    emitter.emit_bound(event)

    assert emitted_events[0] is event


def test_emitter_preserves_unbound_event_identity():
    emitted_events = []
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    event = RuntimeProjectUnboundEvent(project=DummyProject())

    emitter.emit_unbound(event)

    assert emitted_events[0] is event