"""Factory for driver runtime events."""

from __future__ import annotations

from typing import Any

from .event import RuntimeEvent


class EventFactory:
    """Create runtime events."""

    def create(self, event_type: str, payload: dict[str, Any]) -> RuntimeEvent:
        """Create a runtime event instance."""
        return RuntimeEvent(
            _type=event_type,
            _payload=payload,
        )