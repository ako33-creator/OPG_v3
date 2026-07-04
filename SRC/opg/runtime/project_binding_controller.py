"""Controller for runtime project binding operations."""

from __future__ import annotations

from typing import Any, Optional

from .project_binding import RuntimeProjectBinding
from .project_binding_event_emitter import RuntimeProjectBindingEventEmitter
from .project_binding_events import (
    RuntimeProjectBoundEvent,
    RuntimeProjectUnboundEvent,
)
from .project_binding_registry import RuntimeProjectBindingRegistry
from .project_binding_state import RuntimeProjectBindingState
from .project_binding_status import RuntimeProjectBindingStatus


class RuntimeProjectBindingController:
    """Control bind, unbind, and status operations for runtime project binding."""

    def __init__(
        self,
        registry: RuntimeProjectBindingRegistry,
        event_emitter: Optional[RuntimeProjectBindingEventEmitter] = None,
    ) -> None:
        self._registry = registry
        self._event_emitter = event_emitter

    def bind(self, project: Any) -> RuntimeProjectBinding:
        """Bind the runtime to a project model."""
        binding = RuntimeProjectBinding(project=project)
        self._registry.bind(binding)

        if self._event_emitter is not None:
            self._event_emitter.emit_bound(
                RuntimeProjectBoundEvent(project=project)
            )

        return binding

    def unbind(self) -> None:
        """Unbind the runtime from the active project model."""
        binding = self._registry.get_binding()
        self._registry.clear()

        if binding is not None and self._event_emitter is not None:
            self._event_emitter.emit_unbound(
                RuntimeProjectUnboundEvent(project=binding.get_project())
            )

    def get_status(self) -> RuntimeProjectBindingStatus:
        """Return the current runtime project binding status."""
        if self._registry.get_binding() is None:
            return RuntimeProjectBindingStatus(
                state=RuntimeProjectBindingState.UNBOUND
            )

        return RuntimeProjectBindingStatus(
            state=RuntimeProjectBindingState.BOUND
        )