"""Serialization support for the OPG Project Model."""

from __future__ import annotations

from typing import Any


class ProjectSerializer:
    """Serializes Project Model data to dictionaries."""

    def serialize(self, project: Any) -> dict[str, Any]:
        """Serialize a project into a dictionary."""
        return {
            "name": project.name,
        }