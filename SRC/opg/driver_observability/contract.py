"""Contract for runtime observability system."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ObservabilityContract(ABC):
    """Base contract for runtime observability."""

    @abstractmethod
    def log(self, level: str, message: str, context: dict[str, Any] | None = None) -> None:
        """Emit a structured log."""
        raise NotImplementedError

    @abstractmethod
    def metric(self, name: str, value: float, tags: dict[str, Any] | None = None) -> None:
        """Emit a metric."""
        raise NotImplementedError

    @abstractmethod
    def trace(self, name: str, data: dict[str, Any]) -> None:
        """Emit a trace event."""
        raise NotImplementedError