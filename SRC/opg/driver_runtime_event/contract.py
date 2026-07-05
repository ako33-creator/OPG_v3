"""Contract for driver runtime events."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DriverRuntimeEvent(ABC):
    """Base contract for runtime events emitted by drivers."""

    @abstractmethod
    def event_type(self) -> str:
        """Return the type of the event."""
        raise NotImplementedError

    @abstractmethod
    def payload(self) -> dict[str, Any]:
        """Return the event payload."""
        raise NotImplementedError