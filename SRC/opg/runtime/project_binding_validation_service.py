"""Validation service for runtime project binding state."""

from __future__ import annotations

from .project_binding_snapshotter import RuntimeProjectBindingSnapshotter
from .project_binding_validator import RuntimeProjectBindingValidator


class RuntimeProjectBindingValidationService:
    """Create and validate runtime project binding snapshots."""

    def __init__(
        self,
        snapshotter: RuntimeProjectBindingSnapshotter,
        validator: RuntimeProjectBindingValidator,
    ) -> None:
        self._snapshotter = snapshotter
        self._validator = validator

    def is_valid(self) -> bool:
        """Return whether the current runtime project binding state is valid."""
        snapshot = self._snapshotter.snapshot()
        return self._validator.validate(snapshot)