"""Deserialization support for the OPG Project Model."""

from __future__ import annotations

from typing import Any

from .project import Project


class ProjectDeserializer:
    """Deserializes dictionaries into Project Model instances."""

    def deserialize(self, data: dict[str, Any]) -> Project:
        """Deserialize project data into a Project instance."""
        return Project(name=data["name"])