"""Tests for runtime project binding registry."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry


class DummyProject:
    """Minimal project-like object used for registry tests."""


def test_registry_starts_without_binding():
    registry = RuntimeProjectBindingRegistry()

    assert registry.get_binding() is None


def test_registry_stores_binding():
    project = DummyProject()
    binding = RuntimeProjectBinding(project=project)
    registry = RuntimeProjectBindingRegistry()

    registry.bind(binding)

    assert registry.get_binding() is binding


def test_registry_replaces_existing_binding():
    first_binding = RuntimeProjectBinding(project=DummyProject())
    second_binding = RuntimeProjectBinding(project=DummyProject())
    registry = RuntimeProjectBindingRegistry()

    registry.bind(first_binding)
    registry.bind(second_binding)

    assert registry.get_binding() is second_binding


def test_registry_clears_binding():
    binding = RuntimeProjectBinding(project=DummyProject())
    registry = RuntimeProjectBindingRegistry()
    registry.bind(binding)

    registry.clear()

    assert registry.get_binding() is None