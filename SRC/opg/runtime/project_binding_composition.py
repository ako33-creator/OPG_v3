"""Composition factory for runtime project binding services."""

from __future__ import annotations

from .project_binding_controller import RuntimeProjectBindingController
from .project_binding_facade import RuntimeProjectBindingFacade
from .project_binding_guard import RuntimeProjectBindingGuard
from .project_binding_query import RuntimeProjectBindingQuery
from .project_binding_registry import RuntimeProjectBindingRegistry
from .project_binding_required_accessor import (
    RuntimeProjectBindingRequiredAccessor,
)
from .project_binding_requirement import RuntimeProjectBindingRequirement
from .project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from .project_binding_validation_service import (
    RuntimeProjectBindingValidationService,
)
from .project_binding_validator import RuntimeProjectBindingValidator


def create_runtime_project_binding_facade() -> RuntimeProjectBindingFacade:
    """Create a fully composed runtime project binding facade."""
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

    return RuntimeProjectBindingFacade(
        controller=controller,
        query=query,
        required_accessor=required_accessor,
        snapshotter=snapshotter,
        validation_service=validation_service,
    )