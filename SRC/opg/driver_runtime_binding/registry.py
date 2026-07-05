"""Registry for driver runtime bindings."""

from opg.driver.interface import DriverInterface


class DriverRuntimeBindingRegistry:
    """Stores drivers available for runtime binding."""

    def __init__(self) -> None:
        """Initialize an empty binding registry."""
        self._drivers: dict[str, DriverInterface] = {}

    def register(self, name: str, driver: DriverInterface) -> None:
        """Register a driver."""
        self._drivers[name] = driver

    def get(self, name: str) -> DriverInterface | None:
        """Return a registered driver by name."""
        return self._drivers.get(name)

    def unregister(self, name: str) -> None:
        """Remove a registered driver."""
        self._drivers.pop(name, None)