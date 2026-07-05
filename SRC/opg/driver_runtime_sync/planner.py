"""Planner for driver runtime synchronization."""

from __future__ import annotations

from .operation import DriverRuntimeSyncOperation


class DriverRuntimeSyncPlanner:
    """Plan driver runtime synchronization operations."""

    def plan(
        self,
        operation: DriverRuntimeSyncOperation,
    ) -> list[DriverRuntimeSyncOperation]:
        """Return the synchronization operations to execute."""
        return [operation]