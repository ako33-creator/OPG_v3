"""Blender camera access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderCameraAccessAdapter:
    """Adapts access to a Blender camera-like value without importing Blender."""

    def __init__(self, camera: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender camera-like value."""
        self.camera = camera

    def has_camera(self) -> bool:
        """Return whether a camera value is available."""
        return self.camera is not None

    def get_camera(self) -> Any | None:
        """Return the adapted camera value."""
        return self.camera