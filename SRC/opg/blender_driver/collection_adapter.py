"""Blender collection access adapter for OPG."""

from __future__ import annotations

from typing import Any


class BlenderCollectionAccessAdapter:
    """Adapts access to a Blender collection-like value without importing Blender."""

    def __init__(self, collection: Any | None = None) -> None:
        """Initialize the adapter with an optional Blender collection-like value."""
        self.collection = collection

    def has_collection(self) -> bool:
        """Return whether a collection value is available."""
        return self.collection is not None

    def get_collection(self) -> Any | None:
        """Return the adapted collection value."""
        return self.collection