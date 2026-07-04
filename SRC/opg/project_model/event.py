"""
Project Event System.

Extended event bus with unsubscribe and safety guarantees.
"""

from __future__ import annotations

from typing import Any, Callable


class ProjectEvent:
    """Represents a domain event."""

    def __init__(self, name: str, payload: dict[str, Any]) -> None:
        self.name = name
        self.payload = payload


class ProjectEventBus:
    """In-memory event bus with subscription management."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[ProjectEvent], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[ProjectEvent], None]) -> None:
        """Subscribe to event."""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: Callable[[ProjectEvent], None]) -> None:
        """Remove a subscription."""
        if event_name in self._subscribers:
            if handler in self._subscribers[event_name]:
                self._subscribers[event_name].remove(handler)

    def clear(self) -> None:
        """Remove all subscriptions."""
        self._subscribers.clear()

    def emit(self, event: ProjectEvent) -> None:
        """Emit event safely to all subscribers."""
        handlers = list(self._subscribers.get(event.name, []))
        for handler in handlers:
            handler(event)