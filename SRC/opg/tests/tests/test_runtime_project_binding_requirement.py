"""Tests for runtime project binding requirement."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_guard import RuntimeProjectBindingGuard
from opg.runtime.project_binding_query import RuntimeProjectBindingQuery
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_requirement import (
    RuntimeProjectBindingRequirement,
)


class DummyProject:
    """Minimal project-like object used for requirement tests."""


def test_requirement_is_not_satisfied_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)
    requirement = RuntimeProjectBindingRequirement(guard)

    assert requirement.is_satisfied() is False


def test_requirement_is_satisfied_with_active_binding():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)
    requirement = RuntimeProjectBindingRequirement(guard)

    assert requirement.is_satisfied() is True


def test_requirement_reflects_binding_clear():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)
    requirement = RuntimeProjectBindingRequirement(guard)

    registry.clear()

    assert requirement.is_satisfied() is False


def test_requirement_reflects_new_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)
    requirement = RuntimeProjectBindingRequirement(guard)

    registry.bind(RuntimeProjectBinding(project=DummyProject()))

    assert requirement.is_satisfied() is True