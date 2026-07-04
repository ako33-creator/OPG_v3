"""Snapshotter for runtime project binding state."""

from __future__ import annotations

from .project_binding_registry import RuntimeProjectBindingRegistry
from .project_binding_snapshot import RuntimeProjectBindingSnapshot
from .project_binding_state import RuntimeProjectBindingState


class RuntimeProjectBindingSnapshotter:
    """Create snapshots from the active runtime project binding."""

    def __init__(self, registry: RuntimeProjectBindingRegistry) -> None:
        self._registry = registry

    def snapshot(self) -> RuntimeProjectBindingSnapshot:
        """Return a snapshot of the current runtime project binding."""
        binding = self._registry.get_binding()

        if binding is None:
            return RuntimeProjectBindingSnapshot(
                state=RuntimeProjectBindingState.UNBOUND,
                project=None,
            )

        return RuntimeProjectBindingSnapshot(
            state=RuntimeProjectBindingState.BOUND,
            project=binding.get_project(),
        )