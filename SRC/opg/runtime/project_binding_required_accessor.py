"""Required accessor for runtime project binding."""

from __future__ import annotations

from typing import Any

from .project_binding_error import RuntimeProjectBindingError
from .project_binding_query import RuntimeProjectBindingQuery


class RuntimeProjectBindingRequiredAccessor:
    """Return the active project model or raise when none is bound."""

    def __init__(self, query: RuntimeProjectBindingQuery) -> None:
        self._query = query

    def get_required_project(self) -> Any:
        """Return the active project model or raise a binding error."""
        project = self._query.get_project()

        if project is None:
            raise RuntimeProjectBindingError("Active project binding required")

        return project