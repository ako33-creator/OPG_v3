"""Diff adapter for Driver Integration Bridge."""

from __future__ import annotations

from typing import Any

from opg.driver_runtime_event.diff import RuntimeDiff
from .context import DriverIntegrationContext


class DriverIntegrationDiffAdapter:
    """
    Adapt runtime diffs (M-011)
    into integration bridge (M-012).
    """

    def translate(self, diff: RuntimeDiff, context: DriverIntegrationContext) -> Any:
        """Translate diff into integration-level action."""
        return {
            "path": diff.path,
            "old": diff.old_value,
            "new": diff.new_value,
            "context": context.runtime_state,
        }