"""Requirement helpers for runtime project binding."""

from __future__ import annotations

from .project_binding_guard import RuntimeProjectBindingGuard


class RuntimeProjectBindingRequirement:
    """Reusable requirement for operations that need an active project binding."""

    def __init__(self, guard: RuntimeProjectBindingGuard) -> None:
        self._guard = guard

    def is_satisfied(self) -> bool:
        """Return whether the active project binding requirement is satisfied."""
        return self._guard.can_access_project()