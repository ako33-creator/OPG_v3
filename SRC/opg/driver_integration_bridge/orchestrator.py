"""Orchestrator for Driver Integration Bridge."""

from __future__ import annotations

from typing import Any

from .context import DriverIntegrationContext
from .router import DriverIntegrationRouter


class DriverIntegrationOrchestrator:
    """
    High-level orchestrator for the integration bridge.

    Entry point that coordinates routing of:
    - Sync
    - Events
    - Diffs
    """

    def __init__(self, router: DriverIntegrationRouter) -> None:
        self.router = router

    def execute(self, context: DriverIntegrationContext) -> dict[str, Any]:
        """Execute full orchestration flow."""
        return self.router.route(context)