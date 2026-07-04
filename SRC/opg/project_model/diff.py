"""
Project diff utilities.

This module provides explicit diff helpers for the Project Model.
Differences are computed from serialized project representations.
"""

from __future__ import annotations

from typing import Any


class ProjectDiff:
    """Result of computing differences between two Project Model instances."""

    def __init__(
        self,
        added: dict[str, Any],
        removed: dict[str, Any],
        changed: dict[str, tuple[Any, Any]],
    ) -> None:
        self.added = added
        self.removed = removed
        self.changed = changed

    @property
    def has_changes(self) -> bool:
        """Return whether the diff contains any changes."""
        return bool(self.added or self.removed or self.changed)


class ProjectDiffer:
    """Compute differences between Project Model instances."""

    @staticmethod
    def diff(left_project: Any, right_project: Any) -> ProjectDiff:
        """Compute top-level differences between two projects."""
        from opg.project_model.serialization import ProjectSerializer

        serializer = ProjectSerializer()

        left_data = serializer.serialize(left_project)
        right_data = serializer.serialize(right_project)

        added = {
            key: right_data[key]
            for key in right_data.keys() - left_data.keys()
        }
        removed = {
            key: left_data[key]
            for key in left_data.keys() - right_data.keys()
        }
        changed = {
            key: (left_data[key], right_data[key])
            for key in left_data.keys() & right_data.keys()
            if left_data[key] != right_data[key]
        }

        return ProjectDiff(
            added=added,
            removed=removed,
            changed=changed,
        )