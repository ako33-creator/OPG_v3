"""
Optimized Project Serializer.

Performance-focused serialization layer for Project Model.
"""

from __future__ import annotations

from typing import Any


class ProjectSerializer:
    """Fast project serializer."""

    def serialize(self, project: Any) -> dict:
        """
        Convert project into lightweight dict.

        Optimized:
        - direct attribute access
        - no recursion
        - minimal allocations
        """

        return {
            "id": getattr(project, "id", None),
            "project_id": getattr(project, "project_id", None),
            "name": getattr(project, "name", None),
            "version": getattr(project, "version", None),
            "project_model_version": getattr(project, "project_model_version", None),
            "lifecycle_state": getattr(project, "lifecycle_state", None),
        }