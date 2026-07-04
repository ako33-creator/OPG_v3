"""Facade for runtime project binding services."""

from __future__ import annotations

from typing import Any, Optional

from .project_binding_controller import RuntimeProjectBindingController
from .project_binding_query import RuntimeProjectBindingQuery
from .project_binding_required_accessor import (
    RuntimeProjectBindingRequiredAccessor,
)
from .project_binding_snapshot import RuntimeProjectBindingSnapshot
from .project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from .project_binding_status import RuntimeProjectBindingStatus
from .project_binding_validation_service import (
    RuntimeProjectBindingValidationService,
)


class RuntimeProjectBindingFacade:
    """Facade exposing the main runtime project binding operations."""

    def __init__(
        self,
        controller: RuntimeProjectBindingController,
        query: RuntimeProjectBindingQuery,
        required_accessor: RuntimeProjectBindingRequiredAccessor,
        snapshotter: RuntimeProjectBindingSnapshotter,
        validation_service: RuntimeProjectBindingValidationService,
    ) -> None:
        self._controller = controller
        self._query = query
        self._required_accessor = required_accessor
        self._snapshotter = snapshotter
        self._validation_service = validation_service

    def bind(self, project: Any) -> Any:
        """Bind the runtime to a project model."""
        return self._controller.bind(project)

    def unbind(self) -> None:
        """Unbind the runtime from the active project model."""
        self._controller.unbind()

    def is_bound(self) -> bool:
        """Return whether a project binding is active."""
        return self._query.is_bound()

    def get_project(self) -> Optional[Any]:
        """Return the active project model, if any."""
        return self._query.get_project()

    def get_required_project(self) -> Any:
        """Return the active project model or raise if unavailable."""
        return self._required_accessor.get_required_project()

    def get_status(self) -> RuntimeProjectBindingStatus:
        """Return the current binding status."""
        return self._controller.get_status()

    def snapshot(self) -> RuntimeProjectBindingSnapshot:
        """Return a snapshot of the current binding state."""
        return self._snapshotter.snapshot()

    def is_valid(self) -> bool:
        """Return whether the current binding state is valid."""
        return self._validation_service.is_valid()