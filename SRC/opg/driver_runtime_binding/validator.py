"""Validator for driver runtime bindings."""

from opg.driver.interface import DriverInterface


class DriverRuntimeBindingValidator:
    """Validates driver runtime binding inputs."""

    def validate_driver(self, driver: DriverInterface) -> bool:
        """Validate that a driver can be bound to the runtime."""
        return isinstance(driver, DriverInterface)