"""Router for Driver Integration Bridge."""

from __future__ import annotations

from typing import Any

from .context import DriverIntegrationContext
from .pipeline import DriverIntegrationPipeline


class DriverIntegrationRouter:
    """
    Routes integration requests to the pipeline.
    """

    def __init__(self, pipeline: DriverIntegrationPipeline) -> None:
        self.pipeline = pipeline

    def route(self, context: DriverIntegrationContext) -> dict[str, Any]:
        """Route context through integration pipeline."""
        return self.pipeline.run(context)