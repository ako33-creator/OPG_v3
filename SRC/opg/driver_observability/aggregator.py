"""Observability aggregator for runtime system."""

from __future__ import annotations

from typing import Any

from .log_collector import LogCollector
from .metrics_collector import MetricsCollector
from .trace_collector import TraceCollector


class ObservabilityAggregator:
    """
    Aggregates logs, metrics, and traces into a unified view.
    """

    def __init__(
        self,
        logs: LogCollector,
        metrics: MetricsCollector,
        traces: TraceCollector,
    ) -> None:
        self.logs = logs
        self.metrics = metrics
        self.traces = traces

    def snapshot(self) -> dict[str, Any]:
        """Return full observability snapshot."""
        return {
            "logs": self.logs.query(),
            "metrics": self.metrics.query(),
            "traces": self.traces.query(),
        }