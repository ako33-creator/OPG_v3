"""Event model for driver runtime events."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .contract import DriverRuntimeEvent


@dataclass(frozen=True)
class RuntimeEvent(DriverRuntimeEvent):
    """Concrete implementation of a runtime event."""

    _type: str
    _payload: dict[str, Any]

    def event_type(self) -> str:
        return self._type

    def payload(self) -> dict[str, Any]:
        return self._payload