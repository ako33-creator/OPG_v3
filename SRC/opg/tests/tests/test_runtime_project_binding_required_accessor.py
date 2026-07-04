"""Tests for runtime project binding required accessor."""

import pytest

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_error import RuntimeProjectBindingError
from opg.runtime.project_binding_query import RuntimeProjectBindingQuery
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_required_accessor import (
    RuntimeProjectBindingRequiredAccessor,
)


class DummyProject:
    """Minimal project-like object used for required accessor tests."""


def test_required_accessor_raises_without_active_binding():
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    accessor = RuntimeProjectBindingRequiredAccessor(query)

    with pytest.raises(
        RuntimeProjectBindingError,
        match="Active project binding required",
    ):
        accessor.get_required_project()


def test_required_accessor_returns_active_project():
    project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=project))
    query = RuntimeProjectBindingQuery(registry)
    accessor = RuntimeProjectBindingRequiredAccessor(query)

    assert accessor.get_required_project() is project


def test_required_accessor_reflects_binding_replacement():
    first_project = DummyProject()
    second_project = DummyProject()
    registry = RuntimeProjectBindingRegistry()
    query = RuntimeProjectBindingQuery(registry)
    accessor = RuntimeProjectBindingRequiredAccessor(query)

    registry.bind(RuntimeProjectBinding(project=first_project))
    assert accessor.get_required_project() is first_project

    registry.bind(RuntimeProjectBinding(project=second_project))

    assert accessor.get_required_project() is second_project


def test_required_accessor_raises_after_binding_clear():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    query = RuntimeProjectBindingQuery(registry)
    accessor = RuntimeProjectBindingRequiredAccessor(query)

    registry.clear()

    with pytest.raises(RuntimeProjectBindingError):
        accessor.get_required_project()