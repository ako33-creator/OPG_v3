"""Tests for runtime project binding event integration."""

from opg.runtime.project_binding_controller import (
    RuntimeProjectBindingController,
)
from opg.runtime.project_binding_event_emitter import (
    RuntimeProjectBindingEventEmitter,
)
from opg.runtime.project_binding_events import (
    RuntimeProjectBoundEvent,
    RuntimeProjectUnboundEvent,
)
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry


class DummyProject:
    """Minimal project-like object used for integration tests."""


def test_controller_emits_bound_event_when_binding_project():
    project = DummyProject()
    emitted_events = []
    registry = RuntimeProjectBindingRegistry()
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    controller = RuntimeProjectBindingController(registry, emitter)

    controller.bind(project)

    assert len(emitted_events) == 1
    assert isinstance(emitted_events[0], RuntimeProjectBoundEvent)
    assert emitted_events[0].project is project


def test_controller_emits_unbound_event_when_unbinding_project():
    project = DummyProject()
    emitted_events = []
    registry = RuntimeProjectBindingRegistry()
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    controller = RuntimeProjectBindingController(registry, emitter)
    controller.bind(project)
    emitted_events.clear()

    controller.unbind()

    assert len(emitted_events) == 1
    assert isinstance(emitted_events[0], RuntimeProjectUnboundEvent)
    assert emitted_events[0].project is project


def test_controller_does_not_emit_unbound_event_without_active_binding():
    emitted_events = []
    registry = RuntimeProjectBindingRegistry()
    emitter = RuntimeProjectBindingEventEmitter(emitted_events.append)
    controller = RuntimeProjectBindingController(registry, emitter)

    controller.unbind()

    assert emitted_events == []


def test_controller_works_without_event_emitter():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)

    binding = controller.bind(project)
    controller.unbind()

    assert binding.get_project() is project
    assert registry.get_binding() is None