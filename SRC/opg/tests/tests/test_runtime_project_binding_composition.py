"""Tests for runtime project binding composition."""

import pytest

from opg.runtime.project_binding_composition import (
    create_runtime_project_binding_facade,
)
from opg.runtime.project_binding_error import RuntimeProjectBindingError
from opg.runtime.project_binding_facade import RuntimeProjectBindingFacade
from opg.runtime.project_binding_state import RuntimeProjectBindingState


class DummyProject:
    """Minimal project-like object used for composition tests."""


def test_composition_returns_runtime_project_binding_facade():
    facade = create_runtime_project_binding_facade()

    assert isinstance(facade, RuntimeProjectBindingFacade)


def test_composed_facade_starts_unbound():
    facade = create_runtime_project_binding_facade()

    assert facade.is_bound() is False
    assert facade.get_project() is None
    assert facade.get_status().state == RuntimeProjectBindingState.UNBOUND


def test_composed_facade_supports_binding_lifecycle():
    project = DummyProject()
    facade = create_runtime_project_binding_facade()

    facade.bind(project)

    assert facade.is_bound() is True
    assert facade.get_project() is project
    assert facade.get_required_project() is project
    assert facade.get_status().state == RuntimeProjectBindingState.BOUND

    facade.unbind()

    assert facade.is_bound() is False
    assert facade.get_project() is None


def test_composed_facade_required_accessor_raises_without_binding():
    facade = create_runtime_project_binding_facade()

    with pytest.raises(RuntimeProjectBindingError):
        facade.get_required_project()


def test_composed_facade_produces_valid_snapshots():
    project = DummyProject()
    facade = create_runtime_project_binding_facade()

    assert facade.is_valid() is True

    facade.bind(project)

    snapshot = facade.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.BOUND
    assert snapshot.project is project
    assert facade.is_valid() is True

    facade.unbind()

    snapshot = facade.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.UNBOUND
    assert snapshot.project is None
    assert facade.is_valid() is True


def test_composed_facades_use_independent_binding_registries():
    first_facade = create_runtime_project_binding_facade()
    second_facade = create_runtime_project_binding_facade()
    project = DummyProject()

    first_facade.bind(project)

    assert first_facade.is_bound() is True
    assert second_facade.is_bound() is False
    assert second_facade.get_project() is None