"""Listener registry for driver runtime events."""

from __future__ import annotations

from typing import Any, Callable

from .contract import DriverRuntimeEvent


class EventListenerRegistry:
    """Registry for event listeners."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable[[DriverRuntimeEvent], Any]]] = {}

    def register(
        self,
        event_type: str,
        listener: Callable[[DriverRuntimeEvent], Any],
    ) -> None:
        """Register a listener for an event type."""
        self._listeners.setdefault(event_type, []).append(listener)

    def get(self, event_type: str) -> list[Callable[[DriverRuntimeEvent], Any]]:
        """Return listeners for a given event type."""
        return self._listeners.get(event_type, [])

    def all(self) -> dict[str, list[Callable[[DriverRuntimeEvent], Any]]]:
        """Return all registered listeners."""
        return dict(self._listeners)