"""State graph updater."""

from __future__ import annotations

from typing import Any

from .contract import StateGraphContract
from .node import StateNode


class StateGraphUpdater:
    """
    Updates nodes inside the state graph.
    """

    def update_node(self, graph: StateGraphContract, node_id: str, data: Any) -> None:
        """Update a node inside the graph."""
        node = graph.get_node(node_id)

        if node is None:
            # implicit creation if missing
            graph.add_node(node_id, data)
        else:
            if isinstance(node, StateNode):
                node.update(data)
            else:
                graph.add_node(node_id, data)