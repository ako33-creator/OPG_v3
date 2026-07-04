"""
Project Registry System.

Now integrated with Project Event System.
"""

from __future__ import annotations

from typing import Dict, Optional, Any

from opg.project_model.event import ProjectEvent, ProjectEventBus


class ProjectRegistry:
    """Global registry for Project instances with event integration."""

    _projects: Dict[str, Any] = {}
    _event_bus = ProjectEventBus()

    @classmethod
    def get_event_bus(cls) -> ProjectEventBus:
        """Return registry event bus."""
        return cls._event_bus

    @classmethod
    def register(cls, project: Any) -> None:
        """Register a project and emit event."""
        project_id = getattr(project, "project_id", None) or getattr(project, "id", None)

        if project_id is None:
            raise ValueError("Project must have an id or project_id")

        cls._projects[project_id] = project

        cls._event_bus.emit(
            ProjectEvent(
                name="project_registered",
                payload={"project_id": project_id},
            )
        )

    @classmethod
    def get(cls, project_id: str) -> Optional[Any]:
        """Retrieve a project."""
        return cls._projects.get(project_id)

    @classmethod
    def unregister(cls, project_id: str) -> None:
        """Remove project and emit event."""
        project = cls._projects.pop(project_id, None)

        cls._event_bus.emit(
            ProjectEvent(
                name="project_unregistered",
                payload={"project_id": project_id, "project": project},
            )
        )

    @classmethod
    def clear(cls) -> None:
        """Clear registry and emit event."""
        cls._projects.clear()

        cls._event_bus.emit(
            ProjectEvent(
                name="registry_cleared",
                payload={},
            )
        )