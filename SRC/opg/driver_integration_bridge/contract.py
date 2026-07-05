"""Contract for the Driver Integration Bridge."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from opg.driver_runtime_event.diff import RuntimeDiff
from opg.driver_runtime_event.event import RuntimeEvent
from opg.driver_runtime_sync.operation import DriverRuntimeSyncOperation


class DriverIntegrationBridge(ABC):
    """
    Core contract that connects:
    - Sync layer (M-010)
    - Event/Diff system (M-011)
    - Drivers (Blender / others)
    """

    @abstractmethod
    def apply_sync(self, operation: DriverRuntimeSyncOperation) -> Any:
        """Apply a synchronization operation to the runtime/driver layer."""
        raise NotImplementedError

    @abstractmethod
    def dispatch_event(self, event: RuntimeEvent) -> None:
        """Dispatch a runtime event to the driver system."""
        raise NotImplementedError

    @abstractmethod
    def process_diff(self, diff: RuntimeDiff) -> None:
        """Process a runtime diff and translate it into driver actions."""
        raise NotImplementedError