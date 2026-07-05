"""Contract for the runtime state graph system."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class StateGraphContract(ABC):
    """Base contract for runtime state graph systems."""

    @abstractmethod
    def add_node(self, node_id: str, data: Any) -> None:
        """Add a node to the state graph."""
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, source: str, target: str) -> None:
        """Add a dependency edge between nodes."""
        raise NotImplementedError

    @abstractmethod
    def get_node(self, node_id: str) -> Any:
        """Retrieve a node from the graph."""
        raise NotImplementedError

    @abstractmethod
    def resolve(self) -> dict[str, Any]:
        """Resolve full graph state."""
        raise NotImplementedError