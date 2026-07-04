"""
Project cloning utilities.

This module provides explicit cloning helpers for the Project Model.
Cloning is implemented through serialization/deserialization so the
clone remains independent from the original object graph.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


class ProjectCloner:
    """Clone Project Model instances."""

    @staticmethod
    def clone(project: Any) -> Any:
        """Return a deep, independent clone of a project."""
        from opg.project_model.deserialization import ProjectDeserializer
        from opg.project_model.serialization import ProjectSerializer

        serializer = ProjectSerializer()
        deserializer = ProjectDeserializer()

        data = serializer.serialize(project)
        cloned_data = deepcopy(data)

        return deserializer.deserialize(cloned_data)