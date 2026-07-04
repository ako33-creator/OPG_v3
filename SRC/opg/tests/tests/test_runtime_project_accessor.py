"""Tests for runtime project accessor."""

from opg.runtime.project_accessor import RuntimeProjectAccessor
from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry


class DummyProject:
    """Minimal project-like object used for accessor tests."""


def test_accessor_returns_none_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    accessor = RuntimeProjectAccessor(registry)

    assert accessor.get_project() is None


def test_accessor_returns_project_from_active_binding():
    project = DummyProject()
    binding = RuntimeProjectBinding(project=project)
    registry = RuntimeProjectBindingRegistry()
    registry.bind(binding)
    accessor = RuntimeProjectAccessor(registry)

    assert accessor.get_project() is project


def test_accessor_reflects_binding_replacement():
    first_project = DummyProject()
    second_project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    accessor = RuntimeProjectAccessor(registry)

    registry.bind(RuntimeProjectBinding(project=first_project))
    assert accessor.get_project() is first_project

    registry.bind(RuntimeProjectBinding(project=second_project))
    assert accessor.get_project() is second_project


def test_accessor_returns_none_after_binding_clear():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    accessor = RuntimeProjectAccessor(registry)

    registry.clear()

    assert accessor.get_project() is None