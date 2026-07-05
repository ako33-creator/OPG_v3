"""Bootstrap helper for Driver Integration Bridge."""

from __future__ import annotations

from .registry import DriverIntegrationRegistry
from .orchestrator import DriverIntegrationOrchestrator
from .router import DriverIntegrationRouter
from .pipeline import DriverIntegrationPipeline
from .sync_adapter import DriverIntegrationSyncAdapter
from .event_adapter import DriverIntegrationEventAdapter
from .diff_adapter import DriverIntegrationDiffAdapter


class DriverIntegrationBootstrap:
    """
    Initializes the full Driver Integration Bridge stack.
    """

    def __init__(self) -> None:
        self.registry = DriverIntegrationRegistry()

        self.sync_adapter = DriverIntegrationSyncAdapter(executor=None)  # injected later
        self.event_adapter = DriverIntegrationEventAdapter(bus=None)  # injected later
        self.diff_adapter = DriverIntegrationDiffAdapter()

        self.pipeline = DriverIntegrationPipeline(
            sync_adapter=self.sync_adapter,
            event_adapter=self.event_adapter,
            diff_adapter=self.diff_adapter,
        )

        self.router = DriverIntegrationRouter(pipeline=self.pipeline)

        self.orchestrator = DriverIntegrationOrchestrator(router=self.router)

        self.registry.register("orchestrator", self.orchestrator)
        self.registry.register("router", self.router)
        self.registry.register("pipeline", self.pipeline)

    def get_orchestrator(self) -> DriverIntegrationOrchestrator:
        """Return main orchestrator."""
        return self.orchestrator