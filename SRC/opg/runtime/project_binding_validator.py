"""Validator for runtime project binding snapshots."""

from __future__ import annotations

from .project_binding_snapshot import RuntimeProjectBindingSnapshot
from .project_binding_state import RuntimeProjectBindingState


class RuntimeProjectBindingValidator:
    """Validate consistency of runtime project binding snapshots."""

    def validate(self, snapshot: RuntimeProjectBindingSnapshot) -> bool:
        """Return whether the snapshot state matches its project reference."""
        if snapshot.state == RuntimeProjectBindingState.BOUND:
            return snapshot.project is not None

        if snapshot.state == RuntimeProjectBindingState.UNBOUND:
            return snapshot.project is None

        return False