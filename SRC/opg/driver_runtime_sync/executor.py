"""Executor for driver runtime synchronization."""

from __future__ import annotations

from .operation import DriverRuntimeSyncOperation
from .result import DriverRuntimeSyncResult


class DriverRuntimeSyncExecutor:
    """Execute driver runtime synchronization operations."""

    def execute(
        self,
        operation: DriverRuntimeSyncOperation,
    ) -> DriverRuntimeSyncResult:
        """Execute a synchronization operation."""
        return DriverRuntimeSyncResult(
            success=True,
            source=operation.source,
            target=operation.target,
            message=operation.name,
        )