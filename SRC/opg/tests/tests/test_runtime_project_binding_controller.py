"""Tests for runtime project binding controller."""

from opg.runtime.project_binding_controller import RuntimeProjectBindingController
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_state import RuntimeProjectBindingState


class DummyProject:
    """Minimal project-like object used for controller tests."""


def test_controller_starts_unbound():
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)

    status = controller.get_status()

    assert status.state == RuntimeProjectBindingState.UNBOUND
    assert status.is_bound() is False


def test_controller_binds_project():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)

    binding = controller.bind(project)

    assert binding.get_project() is project
    assert registry.get_binding() is binding


def test_controller_reports_bound_status():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)

    controller.bind(project)

    status = controller.get_status()

    assert status.state == RuntimeProjectBindingState.BOUND
    assert status.is_bound() is True


def test_controller_unbinds_project():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)
    controller.bind(project)

    controller.unbind()

    assert registry.get_binding() is None
    assert controller.get_status().state == RuntimeProjectBindingState.UNBOUND


def test_controller_replaces_existing_project_binding():
    first_project = DummyProject()
    second_project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)

    first_binding = controller.bind(first_project)
    second_binding = controller.bind(second_project)

    assert first_binding is not second_binding
    assert registry.get_binding() is second_binding
    assert registry.get_binding().get_project() is second_project