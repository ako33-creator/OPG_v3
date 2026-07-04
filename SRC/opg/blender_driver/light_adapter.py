"""Blender light access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderLightAccessAdapter:
    """Adapts access to a Blender light-like value without importing Blender."""

    def __init__(self, light: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender light-like value."""
        self.light = light

    def has_light(self) -> bool:
        """Return whether a light value is available."""
        return self.light is not None

    def get_light(self) -> Any | None:
        """Return the adapted light value."""
        return self.light