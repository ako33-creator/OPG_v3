"""Tests for runtime project binding query."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_query import RuntimeProjectBindingQuery
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry


class DummyProject:
    """Minimal project-like object used for query tests."""


def test_query_reports_unbound_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)

    assert query.is_bound() is False


def test_query_returns_none_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)

    assert query.get_project() is None


def test_query_reports_bound_with_active_binding():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    query = RuntimeProjectBindingQuery(registry)

    assert query.is_bound() is True


def test_query_returns_active_project():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    query = RuntimeProjectBindingQuery(registry)

    assert query.get_project() is project


def test_query_reflects_binding_replacement():
    first_project = DummyProject()
    second_project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)

    registry.bind(RuntimeProjectBinding(project=first_project))
    assert query.get_project() is first_project

    registry.bind(RuntimeProjectBinding(project=second_project))

    assert query.get_project() is second_project


def test_query_reflects_binding_clear():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    query = RuntimeProjectBindingQuery(registry)

    registry.clear()

    assert query.is_bound() is False
    assert query.get_project() is None