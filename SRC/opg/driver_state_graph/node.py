"""State node model for runtime state graph."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class StateNode:
    """Represents a node in the runtime state graph."""

    node_id: str
    data: Any
    metadata: dict[str, Any] | None = None

    def update(self, data: Any) -> None:
        """Update node data."""
        self.data = data