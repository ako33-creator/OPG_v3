from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict


class RuntimeHealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass(frozen=True)
class RuntimeHealthCheck:
    name: str
    status: RuntimeHealthStatus
    message: str = ""


class RuntimeHealthSystem:
    def __init__(self) -> None:
        self._checks: Dict[str, RuntimeHealthCheck] = {}

    def register_check(
        self,
        name: str,
        status: RuntimeHealthStatus,
        message: str = "",
    ) -> RuntimeHealthCheck:
        check = RuntimeHealthCheck(
            name=name,
            status=status,
            message=message,
        )
        self._checks[name] = check
        return check

    def get_check(self, name: str) -> RuntimeHealthCheck:
        if name not in self._checks:
            raise KeyError(f"Runtime health check not found: {name}")

        return self._checks[name]

    def has_check(self, name: str) -> bool:
        return name in self._checks

    def remove_check(self, name: str) -> None:
        self._checks.pop(name, None)

    def overall_status(self) -> RuntimeHealthStatus:
        if not self._checks:
            return RuntimeHealthStatus.HEALTHY

        statuses = {check.status for check in self._checks.values()}

        if RuntimeHealthStatus.UNHEALTHY in statuses:
            return RuntimeHealthStatus.UNHEALTHY

        if RuntimeHealthStatus.DEGRADED in statuses:
            return RuntimeHealthStatus.DEGRADED

        return RuntimeHealthStatus.HEALTHY

    def checks(self) -> Dict[str, RuntimeHealthCheck]:
        return dict(self._checks)

    def clear(self) -> None:
        self._checks.clear()