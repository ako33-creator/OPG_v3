from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class RuntimeMetric:
    name: str
    value: float


class RuntimeMetricsSystem:
    def __init__(self) -> None:
        self._metrics: Dict[str, RuntimeMetric] = {}

    def set_metric(self, name: str, value: float) -> RuntimeMetric:
        metric = RuntimeMetric(name=name, value=float(value))
        self._metrics[name] = metric
        return metric

    def get_metric(self, name: str) -> RuntimeMetric:
        if name not in self._metrics:
            raise KeyError(f"Runtime metric not found: {name}")

        return self._metrics[name]

    def has_metric(self, name: str) -> bool:
        return name in self._metrics

    def remove_metric(self, name: str) -> None:
        self._metrics.pop(name, None)

    def metrics(self) -> Dict[str, RuntimeMetric]:
        return dict(self._metrics)

    def clear(self) -> None:
        self._metrics.clear()