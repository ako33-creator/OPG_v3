"""Blender driver lifecycle implementation for OPG."""

from __future__ import annotations


class BlenderDriverLifecycle:
    """Tracks Blender driver lifecycle state without importing Blender."""

    def __init__(self) -> None:
        """Initialize the Blender driver lifecycle."""
        self._initialized = False

    def initialize(self) -> None:
        """Mark the Blender driver lifecycle as initialized."""
        self._initialized = True

    def shutdown(self) -> None:
        """Mark the Blender driver lifecycle as shut down."""
        self._initialized = False

    def is_initialized(self) -> bool:
        """Return whether the Blender driver lifecycle is initialized."""
        return self._initialized