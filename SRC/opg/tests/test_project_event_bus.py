"""Tests for Project Event Bus expansion."""

from opg.project_model.event import ProjectEvent, ProjectEventBus


def test_event_bus_subscribe_and_emit():
    bus = ProjectEventBus()
    result = []

    def handler(event):
        result.append(event.payload["value"])

    bus.subscribe("test", handler)

    bus.emit(ProjectEvent("test", {"value": 42}))

    assert result == [42]


def test_event_bus_unsubscribe():
    bus = ProjectEventBus()
    result = []

    def handler(event):
        result.append(1)

    bus.subscribe("test", handler)
    bus.unsubscribe("test", handler)

    bus.emit(ProjectEvent("test", {}))

    assert result == []


def test_event_bus_clear():
    bus = ProjectEventBus()
    result = []

    def handler(event):
        result.append(1)

    bus.subscribe("test", handler)
    bus.clear()

    bus.emit(ProjectEvent("test", {}))

    assert result == []


def test_event_bus_multiple_handlers():
    bus = ProjectEventBus()
    result = []

    def h1(event):
        result.append("a")

    def h2(event):
        result.append("b")

    bus.subscribe("test", h1)
    bus.subscribe("test", h2)

    bus.emit(ProjectEvent("test", {}))

    assert "a" in result
    assert "b" in result