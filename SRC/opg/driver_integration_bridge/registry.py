"""Registry for Driver Integration Bridge components."""

from __future__ import annotations

from typing import Any


class DriverIntegrationRegistry:
    """
    Central registry for integration bridge components.

    Stores adapters, routers, and orchestrators.
    """

    def __init__(self) -> None:
        self._items: dict[str, Any] = {}

    def register(self, name: str, component: Any) -> None:
        """Register a component."""
        self._items[name] = component

    def get(self, name: str) -> Any:
        """Retrieve a component by name."""
        return self._items.get(name)

    def all(self) -> dict[str, Any]:
        """Return all registered components."""
        return dict(self._items)