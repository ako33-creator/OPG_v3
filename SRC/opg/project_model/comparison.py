"""
Project comparison utilities.

This module provides explicit comparison helpers for the Project Model.
Comparison is performed on serialized project data so two independent
project instances can be compared by value.
"""

from __future__ import annotations

from typing import Any


class ProjectComparison:
    """Result of comparing two Project Model instances."""

    def __init__(self, are_equal: bool, left_data: dict[str, Any], right_data: dict[str, Any]) -> None:
        self.are_equal = are_equal
        self.left_data = left_data
        self.right_data = right_data


class ProjectComparator:
    """Compare Project Model instances."""

    @staticmethod
    def compare(left_project: Any, right_project: Any) -> ProjectComparison:
        """Compare two projects by their serialized representation."""
        from opg.project_model.serialization import ProjectSerializer

        serializer = ProjectSerializer()

        left_data = serializer.serialize(left_project)
        right_data = serializer.serialize(right_project)

        return ProjectComparison(
            are_equal=left_data == right_data,
            left_data=left_data,
            right_data=right_data,
        )