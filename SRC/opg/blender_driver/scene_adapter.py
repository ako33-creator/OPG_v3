"""Blender scene access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderSceneAccessAdapter:
    """Adapts access to a Blender scene-like object without importing Blender."""

    def __init__(self, scene: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender scene-like object."""
        self.scene = scene

    def has_scene(self) -> bool:
        """Return whether a scene object is available."""
        return self.scene is not None

    def get_scene(self) -> Any | None:
        """Return the adapted scene object."""
        return self.scene