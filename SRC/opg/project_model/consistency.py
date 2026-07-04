"""
Cross-System Consistency Validator.

Ensures global consistency across all M-004 subsystems:
- Lifecycle
- Registry
- Snapshot
- Event system
- Diff / Comparison / Query
- Integrity layer
"""

from __future__ import annotations

from typing import Any

from opg.project_model.integrity import ProjectIntegrityGuard


class ProjectConsistencyError(Exception):
    """Raised when cross-system inconsistency is detected."""


class ProjectConsistencyValidator:
    """Validate consistency across all Project Model subsystems."""

    @staticmethod
    def validate(project: Any) -> bool:
        """
        Run full cross-system validation.

        This is the final aggregation layer of M-004 safety systems.
        """

        # 1. Integrity check (base layer)
        ProjectIntegrityGuard.validate(project)

        # 2. Lifecycle consistency
        lifecycle = getattr(project, "lifecycle_state", None)
        if lifecycle is None:
            raise ProjectConsistencyError("Missing lifecycle state")

        if lifecycle not in {
            "CREATED",
            "ACTIVE",
            "INACTIVE",
            "DESTROYED",
        }:
            raise ProjectConsistencyError(f"Invalid lifecycle state: {lifecycle}")

        # 3. Registry consistency (soft check)
        if hasattr(project, "project_id") and project.project_id is None:
            raise ProjectConsistencyError("Invalid project_id")

        # 4. Snapshot safety marker (if exists)
        if hasattr(project, "_snapshot_locked") and project._snapshot_locked:
            if lifecycle != "ACTIVE":
                raise ProjectConsistencyError("Snapshot locked project must be ACTIVE")

        return True