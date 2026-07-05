"""Bootstrap helper for driver runtime event system."""

from __future__ import annotations

from .bootstrap import EventBootstrap


class EventBootstrapHelper:
    """Helper wrapper around event bootstrap process."""

    def create(self) -> EventBootstrap:
        """Create a fully initialized bootstrap instance."""
        return EventBootstrap()

    def initialize(self) -> EventBootstrap:
        """Alias for create()."""
        return self.create()