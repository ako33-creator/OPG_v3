"""
Project Snapshot System.

Provides immutable snapshots of a Project Model state.
Snapshots are serialized representations used for caching,
recovery, and temporal comparisons.
"""

from __future__ import annotations

from typing import Any


class ProjectSnapshot:
    """Immutable snapshot of a project state."""

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    @property
    def data(self) -> dict[str, Any]:
        return self._data


class ProjectSnapshotter:
    """Create snapshots from Project Model instances."""

    @staticmethod
    def snapshot(project: Any) -> ProjectSnapshot:
        """Create a snapshot from a project."""
        from opg.project_model.serialization import ProjectSerializer

        serializer = ProjectSerializer()
        data = serializer.serialize(project)

        return ProjectSnapshot(data)