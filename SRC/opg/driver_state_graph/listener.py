"""Event listener for state graph updates."""

from __future__ import annotations

from typing import Any, Callable

from .contract import StateGraphContract


class StateGraphEventListener:
    """
    Listens to runtime events and updates the state graph.
    """

    def __init__(self) -> None:
        self._handlers: list[Callable[[StateGraphContract, dict[str, Any]], Any]] = []

    def register(self, handler: Callable[[StateGraphContract, dict[str, Any]], Any]) -> None:
        """Register an event handler."""
        self._handlers.append(handler)

    def notify(self, graph: StateGraphContract, event: dict[str, Any]) -> None:
        """Notify all listeners of a graph event."""
        for handler in self._handlers:
            handler(graph, event)