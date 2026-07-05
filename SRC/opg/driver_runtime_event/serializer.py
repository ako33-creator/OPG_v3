"""Serializer for driver runtime events."""

from __future__ import annotations

import json
from typing import Any

from .contract import DriverRuntimeEvent


class EventSerializer:
    """Serialize and deserialize runtime events."""

    def serialize(self, event: DriverRuntimeEvent) -> str:
        """Convert event to JSON string."""
        return json.dumps(
            {
                "type": event.event_type(),
                "payload": event.payload(),
            }
        )

    def deserialize(self, data: str) -> dict[str, Any]:
        """Convert JSON string to dict."""
        return json.loads(data)