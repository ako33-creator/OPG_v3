"""Tests for runtime project binding facade."""

import pytest

from opg.runtime.project_binding_controller import RuntimeProjectBindingController
from opg.runtime.project_binding_error import RuntimeProjectBindingError
from opg.runtime.project_binding_facade import RuntimeProjectBindingFacade
from opg.runtime.project_binding_query import RuntimeProjectBindingQuery
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_required_accessor import (
    RuntimeProjectBindingRequiredAccessor,
)
from opg.runtime.project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from opg.runtime.project_binding_state import RuntimeProjectBindingState
from opg.runtime.project_binding_validation_service import (
    RuntimeProjectBindingValidationService,
)
from opg.runtime.project_binding_validator import RuntimeProjectBindingValidator


class DummyProject:
    """Minimal project-like object used for facade tests."""


def create_facade():
    registry = RuntimeProjectBindingRegistry()
    controller = RuntimeProjectBindingController(registry)
    query = RuntimeProjectBindingQuery(registry)
    required_accessor = RuntimeProjectBindingRequiredAccessor(query)
    snapshotter = RuntimeProjectBindingSnapshotter(registry)
    validator = RuntimeProjectBindingValidator()
    validation_service = RuntimeProjectBindingValidationService(
        snapshotter,
        validator,
    )

    facade = RuntimeProjectBindingFacade(
        controller,
        query,
        required_accessor,
        snapshotter,
        validation_service,
    )

    return facade


def test_facade_reports_unbound_initial_state():
    facade = create_facade()

    assert facade.is_bound() is False
    assert facade.get_project() is None


def test_facade_binds_and_returns_project():
    project = DummyProject()
    facade = create_facade()

    facade.bind(project)

    assert facade.is_bound() is True
    assert facade.get_project() is project
    assert facade.get_required_project() is project


def test_facade_unbinds_active_project():
    project = DummyProject()
    facade = create_facade()
    facade.bind(project)

    facade.unbind()

    assert facade.is_bound() is False
    assert facade.get_project() is None


def test_facade_required_project_raises_without_binding():
    facade = create_facade()

    with pytest.raises(RuntimeProjectBindingError):
        facade.get_required_project()


def test_facade_returns_binding_status():
    facade = create_facade()

    assert facade.get_status().state == RuntimeProjectBindingState.UNBOUND

    facade.bind(DummyProject())

    assert facade.get_status().state == RuntimeProjectBindingState.BOUND


def test_facade_returns_binding_snapshot():
    project = DummyProject()
    facade = create_facade()
    facade.bind(project)

    snapshot = facade.snapshot()

    assert snapshot.state == RuntimeProjectBindingState.BOUND
    assert snapshot.project is project


def test_facade_reports_valid_binding_state():
    facade = create_facade()

    assert facade.is_valid() is True

    facade.bind(DummyProject())

    assert facade.is_valid() is True