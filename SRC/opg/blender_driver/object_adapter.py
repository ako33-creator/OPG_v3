"""Blender object access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderObjectAccessAdapter:
    """Adapts access to a Blender object-like value without importing Blender."""

    def __init__(self, object_value: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender object-like value."""
        self.object_value = object_value

    def has_object(self) -> bool:
        """Return whether an object value is available."""
        return self.object_value is not None

    def get_object(self) -> Any | None:
        """Return the adapted object value."""
        return self.object_value
    