"""Tests for runtime project binding guard."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_guard import RuntimeProjectBindingGuard
from opg.runtime.project_binding_query import RuntimeProjectBindingQuery
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry


class DummyProject:
    """Minimal project-like object used for guard tests."""


def test_guard_denies_project_access_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)

    assert guard.can_access_project() is False


def test_guard_allows_project_access_with_active_binding():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)

    assert guard.can_access_project() is True


def test_guard_reflects_binding_clear():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)

    registry.clear()

    assert guard.can_access_project() is False


def test_guard_reflects_new_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    guard = RuntimeProjectBindingGuard(query)

    registry.bind(RuntimeProjectBinding(project=DummyProject()))

    assert guard.can_access_project() is True