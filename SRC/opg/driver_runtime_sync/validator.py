"""Validator for driver runtime synchronization."""

from __future__ import annotations

from .operation import DriverRuntimeSyncOperation


class DriverRuntimeSyncValidator:
    """Validate driver runtime synchronization operations."""

    def validate(self, operation: DriverRuntimeSyncOperation) -> bool:
        """Return True when a synchronization operation is valid."""
        return bool(operation.name)