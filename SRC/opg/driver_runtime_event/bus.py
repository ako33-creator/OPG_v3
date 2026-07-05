"""Event bus for driver runtime events."""

from __future__ import annotations

from typing import Any, Callable

from .contract import DriverRuntimeEvent


class RuntimeEventBus:
    """Simple in-memory event bus."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[DriverRuntimeEvent], Any]]] = {}

    def subscribe(
        self,
        event_type: str,
        callback: Callable[[DriverRuntimeEvent], Any],
    ) -> None:
        """Subscribe to a specific event type."""
        self._subscribers.setdefault(event_type, []).append(callback)

    def publish(self, event: DriverRuntimeEvent) -> None:
        """Publish an event to all subscribers."""
        for callback in self._subscribers.get(event.event_type(), []):
            callback(event)