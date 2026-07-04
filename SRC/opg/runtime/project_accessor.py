"""Accessor utilities for runtime project bindings."""

from __future__ import annotations

from typing import Any, Optional

from .project_binding_registry import RuntimeProjectBindingRegistry


class RuntimeProjectAccessor:
    """Expose the project model from the active runtime binding."""

    def __init__(self, registry: RuntimeProjectBindingRegistry) -> None:
        self._registry = registry

    def get_project(self) -> Optional[Any]:
        """Return the active project model, if a binding exists."""
        binding = self._registry.get_binding()

        if binding is None:
            return None

        return binding.get_project()