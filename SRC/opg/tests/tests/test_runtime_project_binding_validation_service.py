"""Tests for runtime project binding validation service."""

from opg.runtime.project_binding import RuntimeProjectBinding
from opg.runtime.project_binding_registry import RuntimeProjectBindingRegistry
from opg.runtime.project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from opg.runtime.project_binding_validation_service import (
    RuntimeProjectBindingValidationService,
)
from opg.runtime.project_binding_validator import RuntimeProjectBindingValidator


class DummyProject:
    """Minimal project-like object used for validation service tests."""


def test_validation_service_accepts_unbound_clean_state():
    registry = RuntimeProjectBindingRegistry()
    snapshotter = RuntimeProjectBindingSnapshotter(registry)
    validator = RuntimeProjectBindingValidator()
    service = RuntimeProjectBindingValidationService(snapshotter, validator)

    assert service.is_valid() is True


def test_validation_service_accepts_bound_clean_state():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    snapshotter = RuntimeProjectBindingSnapshotter(registry)
    validator = RuntimeProjectBindingValidator()
    service = RuntimeProjectBindingValidationService(snapshotter, validator)

    assert service.is_valid() is True


def test_validation_service_reflects_binding_clear():
    registry = RuntimeProjectBindingRegistry()
    registry.bind(RuntimeProjectBinding(project=DummyProject()))
    snapshotter = RuntimeProjectBindingSnapshotter(registry)
    validator = RuntimeProjectBindingValidator()
    service = RuntimeProjectBindingValidationService(snapshotter, validator)

    registry.clear()

    assert service.is_valid() is True