"""Registry for the active runtime project binding."""

from __future__ import annotations

from typing import Optional

from .project_binding import RuntimeProjectBinding


class RuntimeProjectBindingRegistry:
    """Store and expose the active runtime project binding."""

    def __init__(self) -> None:
        self._binding: Optional[RuntimeProjectBinding] = None

    def bind(self, binding: RuntimeProjectBinding) -> None:
        """Register the active runtime project binding."""
        self._binding = binding

    def get_binding(self) -> Optional[RuntimeProjectBinding]:
        """Return the active runtime project binding, if any."""
        return self._binding

    def clear(self) -> None:
        """Remove the active runtime project binding."""
        self._binding = None