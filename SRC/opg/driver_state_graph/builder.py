"""State graph builder for runtime dependency graph."""

from __future__ import annotations

from typing import Any

from .node import StateNode
from .edge import DependencyEdge
from .contract import StateGraphContract


class StateGraphBuilder:
    """Builds a state graph from nodes and edges."""

    def __init__(self) -> None:
        self.nodes: dict[str, StateNode] = {}
        self.edges: list[DependencyEdge] = []

    def add_node(self, node_id: str, data: Any) -> None:
        self.nodes[node_id] = StateNode(node_id=node_id, data=data)

    def add_edge(self, source: str, target: str) -> None:
        self.edges.append(DependencyEdge(source=source, target=target))

    def build(self) -> StateGraphContract:
        """Return a built graph contract implementation."""

        class BuiltGraph(StateGraphContract):
            def __init__(self, nodes, edges):
                self._nodes = nodes
                self._edges = edges

            def add_node(self, node_id: str, data: Any) -> None:
                self._nodes[node_id] = StateNode(node_id, data)

            def add_edge(self, source: str, target: str) -> None:
                self._edges.append(DependencyEdge(source, target))

            def get_node(self, node_id: str) -> Any:
                return self._nodes.get(node_id)

            def resolve(self) -> dict[str, Any]:
                return {
                    "nodes": self._nodes,
                    "edges": self._edges,
                }

        return BuiltGraph(self.nodes, self.edges)