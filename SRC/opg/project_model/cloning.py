"""
Optimized Project Cloner.

Uses fast serialize/deserialize pipeline.
"""

from __future__ import annotations

from typing import Any


class ProjectCloner:
    """High-performance project cloner."""

    @staticmethod
    def clone(project: Any) -> Any:
        from opg.project_model.serialization import ProjectSerializer
        from opg.project_model.deserialization import ProjectDeserializer

        serializer = ProjectSerializer()
        deserializer = ProjectDeserializer()

        data = serializer.serialize(project)
        return deserializer.deserialize(data)