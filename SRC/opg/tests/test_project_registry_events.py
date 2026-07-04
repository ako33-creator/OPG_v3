"""Tests for Project Registry Event Integration."""

from opg.project_model.registry import ProjectRegistry


class DummyProject:
    def __init__(self, pid: str):
        self.project_id = pid


def test_registry_emits_register_event():
    bus = ProjectRegistry.get_event_bus()
    events = []

    def handler(event):
        events.append(event.name)

    bus.subscribe("project_registered", handler)

    project = DummyProject("123")
    ProjectRegistry.register(project)

    assert "project_registered" in events


def test_registry_emits_unregister_event():
    bus = ProjectRegistry.get_event_bus()
    events = []

    def handler(event):
        events.append(event.name)

    bus.subscribe("project_unregistered", handler)

    project = DummyProject("456")
    ProjectRegistry.register(project)
    ProjectRegistry.unregister("456")

    assert "project_unregistered" in events


def test_registry_emits_clear_event():
    bus = ProjectRegistry.get_event_bus()
    events = []

    def handler(event):
        events.append(event.name)

    bus.subscribe("registry_cleared", handler)

    project = DummyProject("789")
    ProjectRegistry.register(project)

    ProjectRegistry.clear()

    assert "registry_cleared" in events