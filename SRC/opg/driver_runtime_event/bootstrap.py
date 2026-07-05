"""Bootstrap helper for driver runtime event system."""

from __future__ import annotations

from .factory import EventFactory
from .bus import RuntimeEventBus
from .listener_registry import EventListenerRegistry


class EventBootstrap:
    """Initialize event system components."""

    def __init__(
        self,
        bus: RuntimeEventBus | None = None,
        registry: EventListenerRegistry | None = None,
        factory: EventFactory | None = None,
    ) -> None:
        self.bus = bus or RuntimeEventBus()
        self.registry = registry or EventListenerRegistry()
        self.factory = factory or EventFactory()

    def bootstrap(self) -> tuple[RuntimeEventBus, EventListenerRegistry, EventFactory]:
        """Return initialized event system components."""
        return self.bus, self.registry, self.factory