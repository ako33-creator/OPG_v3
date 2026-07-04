"""
Project Query System.

Provides a lightweight query interface over the serialized Project Model.
Allows filtering and searching project data without modifying it.
"""

from __future__ import annotations

from typing import Any, Callable


class ProjectQuery:
    """Represents a query result."""

    def __init__(self, results: list[Any]) -> None:
        self.results = results

    def __len__(self) -> int:
        return len(self.results)


class ProjectQueryEngine:
    """Query engine for Project Model."""

    @staticmethod
    def query(project: Any, predicate: Callable[[dict[str, Any]], bool]) -> ProjectQuery:
        """
        Execute a query over a serialized project.

        Args:
            project: Project instance
            predicate: function applied on serialized dict

        Returns:
            ProjectQuery
        """
        from opg.project_model.serialization import ProjectSerializer

        serializer = ProjectSerializer()
        data = serializer.serialize(project)

        results: list[Any] = []

        # flat scan (safe minimal implementation)
        if predicate(data):
            results.append(data)

        return ProjectQuery(results)