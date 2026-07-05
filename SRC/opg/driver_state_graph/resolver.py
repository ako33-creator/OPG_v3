"""State graph resolver."""

from __future__ import annotations

from typing import Any

from .contract import StateGraphContract


class StateGraphResolver:
    """
    Resolves the state graph into a computed runtime structure.
    """

    def resolve(self, graph: StateGraphContract) -> dict[str, Any]:
        """Resolve full graph state."""
        return graph.resolve()