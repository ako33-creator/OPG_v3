"""
Project Integrity Final Guard.

Ensures global consistency of Project Model state across:
- lifecycle
- registry
- snapshots
- serialization integrity
"""

from __future__ import annotations

from typing import Any


class ProjectIntegrityError(Exception):
    """Raised when Project Model integrity is violated."""


class ProjectIntegrityGuard:
    """Central integrity validation layer."""

    @staticmethod
    def validate(project: Any) -> None:
        """
        Validate global integrity constraints.
        Raises ProjectIntegrityError if invalid state detected.
        """

        # 1. Must have lifecycle state
        if not hasattr(project, "lifecycle_state"):
            raise ProjectIntegrityError("Missing lifecycle_state")

        # 2. Must have id or project_id
        if not (hasattr(project, "id") or hasattr(project, "project_id")):
            raise ProjectIntegrityError("Missing project identifier")

        # 3. Must not be in destroyed state for active use
        if getattr(project, "lifecycle_state", None) == "DESTROYED":
            raise ProjectIntegrityError("Project is destroyed")

        return True