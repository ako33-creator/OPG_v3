"""Sync adapter for Driver Integration Bridge."""

from __future__ import annotations

from typing import Any

from opg.driver_runtime_sync.operation import DriverRuntimeSyncOperation
from opg.driver_runtime_sync.executor import DriverRuntimeSyncExecutor
from .context import DriverIntegrationContext


class DriverIntegrationSyncAdapter:
    """
    Adapts synchronization layer (M-010)
    to the integration bridge (M-012).
    """

    def __init__(self, executor: DriverRuntimeSyncExecutor) -> None:
        self.executor = executor

    def apply(self, context: DriverIntegrationContext) -> Any:
        """Apply synchronization using runtime context."""
        operation = DriverRuntimeSyncOperation(
            name="sync",
            source=context.runtime_state,
            target=context.driver_state,
        )
        return self.executor.execute(operation)