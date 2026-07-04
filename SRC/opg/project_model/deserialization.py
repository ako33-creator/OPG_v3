"""
Optimized Project Deserializer.

Rebuilds Project Model instances from serialized dicts.
"""

from __future__ import annotations

from typing import Any


class ProjectDeserializer:
    """Fast project deserializer."""

    def deserialize(self, data: dict) -> Any:
        """
        Rebuild a Project instance from serialized data.
        """

        from opg.project_model.project import Project

        project = Project(data.get("name"))

        if hasattr(project, "id") and data.get("id") is not None:
            try:
                object.__setattr__(project, "id", data.get("id"))
            except Exception:
                pass

        if hasattr(project, "project_id") and data.get("project_id") is not None:
            try:
                object.__setattr__(project, "project_id", data.get("project_id"))
            except Exception:
                pass

        if hasattr(project, "version") and data.get("version") is not None:
            try:
                object.__setattr__(project, "version", data.get("version"))
            except Exception:
                pass

        if hasattr(project, "project_model_version") and data.get("project_model_version") is not None:
            try:
                object.__setattr__(project, "project_model_version", data.get("project_model_version"))
            except Exception:
                pass

        if data.get("lifecycle_state") is not None:
            try:
                object.__setattr__(project, "lifecycle_state", data.get("lifecycle_state"))
            except Exception:
                pass

        return project