"""Controller for runtime project binding operations."""

from __future__ import annotations

from typing import Any

from .project_binding import RuntimeProjectBinding
from .project_binding_registry import RuntimeProjectBindingRegistry
from .project_binding_state import RuntimeProjectBindingState
from .project_binding_status import RuntimeProjectBindingStatus


class RuntimeProjectBindingController:
    """Control bind, unbind, and status operations for runtime project binding."""

    def __init__(self, registry: RuntimeProjectBindingRegistry) -> None:
        self._registry = registry

    def bind(self, project: Any) -> RuntimeProjectBinding:
        """Bind the runtime to a project model."""
        binding = RuntimeProjectBinding(project=project)
        self._registry.bind(binding)
        return binding

    def unbind(self) -> None:
        """Unbind the runtime from the active project model."""
        self._registry.clear()

    def get_status(self) -> RuntimeProjectBindingStatus:
        """Return the current runtime project binding status."""
        if self._registry.get_binding() is None:
            return RuntimeProjectBindingStatus(
                state=RuntimeProjectBindingState.UNBOUND
            )

        return RuntimeProjectBindingStatus(
            state=RuntimeProjectBindingState.BOUND
        )