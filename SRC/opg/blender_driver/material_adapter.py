"""Blender material access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderMaterialAccessAdapter:
    """Adapts access to a Blender material-like value without importing Blender."""

    def __init__(self, material: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender material-like value."""
        self.material = material

    def has_material(self) -> bool:
        """Return whether a material value is available."""
        return self.material is not None

    def get_material(self) -> Any | None:
        """Return the adapted material value."""
        return self.material