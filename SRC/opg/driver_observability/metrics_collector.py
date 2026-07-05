"""Metrics collector for runtime observability system."""

from __future__ import annotations

from typing import Any

from .metrics_model import Metric


class MetricsCollector:
    """Collects runtime metrics."""

    def __init__(self) -> None:
        self.metrics: list[Metric] = []

    def collect(self, metric: Metric) -> None:
        """Store a metric."""
        self.metrics.append(metric)

    def query(self, name: str | None = None) -> list[dict[str, Any]]:
        """Return metrics optionally filtered by name."""
        if name is None:
            return [m.to_dict() for m in self.metrics]

        return [m.to_dict() for m in self.metrics if m.name == name]