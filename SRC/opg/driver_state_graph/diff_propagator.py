"""Diff propagator for state graph."""

from __future__ import annotations

from typing import Any

from opg.driver_runtime_event.diff import RuntimeDiff
from .contract import StateGraphContract


class StateGraphDiffPropagator:
    """
    Propagates runtime diffs into the state graph.
    """

    def propagate(self, graph: StateGraphContract, diff: RuntimeDiff) -> Any:
        """Apply diff to graph state."""
        node = graph.get_node(diff.path)

        if node is None:
            graph.add_node(diff.path, diff.new_value)
        else:
            graph.add_node(diff.path, diff.new_value)

        return graph.resolve()