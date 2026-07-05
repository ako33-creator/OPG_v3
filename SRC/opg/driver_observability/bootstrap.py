"""Bootstrap helper for observability system."""

from __future__ import annotations

from .contract import ObservabilityContract
from .log_collector import LogCollector
from .metrics_collector import MetricsCollector
from .trace_collector import TraceCollector
from .aggregator import ObservabilityAggregator
from .router import ObservabilityRouter


class ObservabilityBootstrap:
    """
    Initializes full observability stack:
    - logs
    - metrics
    - traces
    - aggregation
    - routing
    """

    def __init__(self, contract: ObservabilityContract) -> None:
        self.contract = contract

        self.log_collector = LogCollector()
        self.metrics_collector = MetricsCollector()
        self.trace_collector = TraceCollector()

        self.aggregator = ObservabilityAggregator(
            logs=self.log_collector,
            metrics=self.metrics_collector,
            traces=self.trace_collector,
        )

        self.router = ObservabilityRouter(
            contract=self.contract,
            aggregator=self.aggregator,
        )

    def get_router(self) -> ObservabilityRouter:
        """Return main observability router."""
        return self.router