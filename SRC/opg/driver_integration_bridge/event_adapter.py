"""Event adapter for Driver Integration Bridge."""

from __future__ import annotations

from typing import Any

from opg.driver_runtime_event.event import RuntimeEvent
from opg.driver_runtime_event.bus import RuntimeEventBus
from .context import DriverIntegrationContext


class DriverIntegrationEventAdapter:
    """
    Adapt runtime events (M-011)
    into the integration bridge (M-012).
    """

    def __init__(self, bus: RuntimeEventBus) -> None:
        self.bus = bus

    def publish(self, event: RuntimeEvent, context: DriverIntegrationContext) -> Any:
        """Publish event into runtime event bus."""
        # context kept for future routing logic
        return self.bus.publish(event)