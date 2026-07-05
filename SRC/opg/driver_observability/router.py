"""Observability router for runtime system."""

from __future__ import annotations

from typing import Any

from .aggregator import ObservabilityAggregator
from .contract import ObservabilityContract


class ObservabilityRouter:
    """
    Routes observability signals to the appropriate collectors.
    """

    def __init__(
        self,
        contract: ObservabilityContract,
        aggregator: ObservabilityAggregator,
    ) -> None:
        self.contract = contract
        self.aggregator = aggregator

    def route_log(self, level: str, message: str, context: dict[str, Any] | None = None) -> None:
        """Route log event."""
        self.contract.log(level, message, context)

    def route_metric(self, name: str, value: float, tags: dict[str, Any] | None = None) -> None:
        """Route metric event."""
        self.contract.metric(name, value, tags)

    def route_trace(self, name: str, data: dict[str, Any]) -> None:
        """Route trace event."""
        self.contract.trace(name, data)

    def snapshot(self) -> dict[str, Any]:
        """Return aggregated observability snapshot."""
        return self.aggregator.snapshot()