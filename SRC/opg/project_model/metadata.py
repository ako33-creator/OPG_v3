"""Metadata model for the OPG Project Model."""

from __future__ import annotations

from typing import Any


class Metadata:
    """Stores arbitrary metadata associated with a project model entity."""

    def __init__(self) -> None:
        self._values: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Store a metadata value."""
        self._values[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Return a metadata value."""
        return self._values.get(key, default)

    def remove(self, key: str) -> None:
        """Remove a metadata value if it exists."""
        self._values.pop(key, None)

    def has(self, key: str) -> bool:
        """Return whether a metadata key exists."""
        return key in self._values

    def clear(self) -> None:
        """Remove all metadata values."""
        self._values.clear()

    def to_dict(self) -> dict[str, Any]:
        """Return a copy of the metadata values."""
        return dict(self._values)
    