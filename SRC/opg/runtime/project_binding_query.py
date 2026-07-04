"""Query service for runtime project binding state."""

from __future__ import annotations

from typing import Any, Optional

from .project_binding_registry import RuntimeProjectBindingRegistry


class RuntimeProjectBindingQuery:
    """Read-only query service for runtime project binding."""

    def __init__(self, registry: RuntimeProjectBindingRegistry) -> None:
        self._registry = registry

    def is_bound(self) -> bool:
        """Return whether a project binding is currently active."""
        return self._registry.get_binding() is not None

    def get_project(self) -> Optional[Any]:
        """Return the active project model, if any."""
        binding = self._registry.get_binding()

        if binding is None:
            return None

        return binding.get_project()