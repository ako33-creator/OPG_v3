"""Factory for driver runtime binding components."""

from opg.driver_runtime_binding.registry import DriverRuntimeBindingRegistry
from opg.driver_runtime_binding.validator import DriverRuntimeBindingValidator


class DriverRuntimeBindingFactory:
    """Creates driver runtime binding components."""

    def create_registry(self) -> DriverRuntimeBindingRegistry:
        """Create a driver runtime binding registry."""
        return DriverRuntimeBindingRegistry()

    def create_validator(self) -> DriverRuntimeBindingValidator:
        """Create a driver runtime binding validator."""
        return DriverRuntimeBindingValidator()