"""Contract for driver runtime synchronization."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DriverRuntimeSync(ABC):
    """Define the contract for driver runtime synchronization."""

    @abstractmethod
    def synchronize(self, source: Any, target: Any) -> Any:
        """Synchronize a source with a target."""
        raise NotImplementedError