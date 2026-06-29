"""
OPG Core Configuration.

Central configuration storage for the OPG application.

Rules:
- No Blender dependency.
- No external dependency.
- Configuration keys must be valid non-empty strings.
"""

from typing import Any, Dict, Optional

from .exceptions import OPGConfigurationError


DEFAULT_CONFIG: Dict[str, Any] = {
    "app.name": "OPG",
    "app.version": "3.0.0",
    "app.debug": False,
    "logging.level": "INFO",
}


class Configuration:
    """
    Central configuration container for OPG.

    Stores key/value settings and provides controlled access.
    """

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._defaults: Dict[str, Any] = dict(defaults or DEFAULT_CONFIG)
        self._values: Dict[str, Any] = dict(self._defaults)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Return a configuration value.
        """
        self._validate_key(key)
        return self._values.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        """
        self._validate_key(key)
        self._values[key] = value

    def has(self, key: str) -> bool:
        """
        Check whether a configuration key exists.
        """
        self._validate_key(key)
        return key in self._values

    def remove(self, key: str) -> None:
        """
        Remove a configuration value.

        Raises:
            OPGConfigurationError: If the key does not exist.
        """
        self._validate_key(key)

        if key not in self._values:
            raise OPGConfigurationError(f"Configuration key not found: {key}")

        del self._values[key]

    def update(self, values: Dict[str, Any]) -> None:
        """
        Merge multiple configuration values.
        """
        if not isinstance(values, dict):
            raise OPGConfigurationError("Configuration update expects a dictionary.")

        for key in values:
            self._validate_key(key)

        self._values.update(values)

    def reset(self) -> None:
        """
        Reset configuration to default values.
        """
        self._values = dict(self._defaults)

    def to_dict(self) -> Dict[str, Any]:
        """
        Export configuration as a dictionary copy.
        """
        return dict(self._values)

    def defaults(self) -> Dict[str, Any]:
        """
        Export default configuration as a dictionary copy.
        """
        return dict(self._defaults)

    def count(self) -> int:
        """
        Return the number of configuration entries.
        """
        return len(self._values)

    def _validate_key(self, key: str) -> None:
        """
        Validate a configuration key.
        """
        if not isinstance(key, str):
            raise OPGConfigurationError("Configuration key must be a string.")

        if not key.strip():
            raise OPGConfigurationError("Configuration key cannot be empty.")