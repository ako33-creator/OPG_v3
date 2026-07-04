"""Emitter for runtime project binding events."""

from __future__ import annotations

from typing import Callable

from .project_binding_events import (
    RuntimeProjectBoundEvent,
    RuntimeProjectUnboundEvent,
)


class RuntimeProjectBindingEventEmitter:
    """Emit runtime project binding events through a callback."""

    def __init__(self, emit: Callable[[object], None]) -> None:
        self._emit = emit

    def emit_bound(self, event: RuntimeProjectBoundEvent) -> None:
        """Emit a runtime project bound event."""
        self._emit(event)

    def emit_unbound(self, event: RuntimeProjectUnboundEvent) -> None:
        """Emit a runtime project unbound event."""
        self._emit(event)