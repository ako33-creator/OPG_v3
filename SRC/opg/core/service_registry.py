"""
OPG Core Service Registry.

Central registry for application-level services.

Rules:
- No Blender dependency.
- No external dependency.
- No service should be overwritten silently.
"""

from typing import Any, Dict, Iterator, Optional, Type, TypeVar

from .exceptions import OPGServiceError


T = TypeVar("T")


class ServiceRegistry:
    """
    Stores and retrieves application services by name.

    A service is any object shared across the OPG application lifecycle.
    """

    def __init__(self) -> None:
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any, *, replace: bool = False) -> None:
        """
        Register a service.

        Args:
            name: Unique service name.
            service: Service instance.
            replace: Allow replacing an existing service.

        Raises:
            OPGServiceError: If the name is invalid, service is None,
            or service already exists without replace=True.
        """
        self._validate_name(name)

        if service is None:
            raise OPGServiceError("Cannot register a None service.")

        if name in self._services and not replace:
            raise OPGServiceError(f"Service already registered: {name}")

        self._services[name] = service

    def get(self, name: str, expected_type: Optional[Type[T]] = None) -> T:
        """
        Retrieve a registered service.

        Args:
            name: Service name.
            expected_type: Optional expected Python type.

        Returns:
            The registered service.

        Raises:
            OPGServiceError: If the service does not exist or has an invalid type.
        """
        self._validate_name(name)

        if name not in self._services:
            raise OPGServiceError(f"Service not registered: {name}")

        service = self._services[name]

        if expected_type is not None and not isinstance(service, expected_type):
            raise OPGServiceError(
                f"Service '{name}' has invalid type. "
                f"Expected {expected_type.__name__}, got {type(service).__name__}."
            )

        return service

    def has(self, name: str) -> bool:
        """
        Check whether a service exists.
        """
        self._validate_name(name)
        return name in self._services

    def unregister(self, name: str) -> None:
        """
        Remove a registered service.

        Raises:
            OPGServiceError: If the service does not exist.
        """
        self._validate_name(name)

        if name not in self._services:
            raise OPGServiceError(f"Cannot unregister missing service: {name}")

        del self._services[name]

    def clear(self) -> None:
        """
        Remove all registered services.
        """
        self._services.clear()

    def names(self) -> Iterator[str]:
        """
        Iterate over registered service names.
        """
        return iter(self._services.keys())

    def services(self) -> Iterator[Any]:
        """
        Iterate over registered service instances.
        """
        return iter(self._services.values())

    def items(self) -> Iterator[tuple[str, Any]]:
        """
        Iterate over service name / instance pairs.
        """
        return iter(self._services.items())

    def count(self) -> int:
        """
        Return the number of registered services.
        """
        return len(self._services)

    def _validate_name(self, name: str) -> None:
        """
        Validate a service name.
        """
        if not isinstance(name, str):
            raise OPGServiceError("Service name must be a string.")

        if not name.strip():
            raise OPGServiceError("Service name cannot be empty.")