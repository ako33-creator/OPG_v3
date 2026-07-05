"""Context wiring for the Blender driver."""

from typing import Any


class BlenderDriverContext:
    """Stores runtime context for the Blender driver."""

    def __init__(self) -> None:
        """Initialize an empty Blender driver context."""
        self._values: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Set a context value."""
        self._values[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Return a context value."""
        return self._values.get(key, default)

    def clear(self) -> None:
        """Clear all context values."""
        self._values.clear()