"""
Project Lifecycle Manager.

Frozen-safe lifecycle management using attribute replacement via object.__setattr__.
"""

from __future__ import annotations

from typing import Any


class ProjectLifecycleState:
    CREATED = "CREATED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DESTROYED = "DESTROYED"


class ProjectLifecycleManager:
    """Manage lifecycle state of a frozen Project Model."""

    @staticmethod
    def create(project: Any) -> None:
        object.__setattr__(project, "lifecycle_state", ProjectLifecycleState.CREATED)

    @staticmethod
    def activate(project: Any) -> None:
        object.__setattr__(project, "lifecycle_state", ProjectLifecycleState.ACTIVE)

    @staticmethod
    def deactivate(project: Any) -> None:
        object.__setattr__(project, "lifecycle_state", ProjectLifecycleState.INACTIVE)

    @staticmethod
    def destroy(project: Any) -> None:
        object.__setattr__(project, "lifecycle_state", ProjectLifecycleState.DESTROYED)