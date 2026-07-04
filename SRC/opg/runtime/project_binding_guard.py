"""Guard utilities for runtime project binding."""

from __future__ import annotations

from .project_binding_query import RuntimeProjectBindingQuery


class RuntimeProjectBindingGuard:
    """Guard operations that require an active runtime project binding."""

    def __init__(self, query: RuntimeProjectBindingQuery) -> None:
        self._query = query

    def can_access_project(self) -> bool:
        """Return whether project access is currently allowed."""
        return self._query.is_bound()