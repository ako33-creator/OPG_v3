"""Blender context adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderContextAdapter:
    """Adapts a Blender context-like object without importing Blender."""

    def __init__(self, context: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender context-like object."""
        self.context = context

    def has_context(self) -> bool:
        """Return whether a context object is available."""
        return self.context is not None

    def get_context(self) -> Any | None:
        """Return the adapted context object."""
        return self.context