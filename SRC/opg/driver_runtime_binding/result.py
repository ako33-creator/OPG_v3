"""Result model for driver runtime binding operations."""

from dataclasses import dataclass

from opg.driver_runtime_binding.state import DriverRuntimeBindingState


@dataclass(frozen=True, slots=True)
class DriverRuntimeBindingResult:
    """Represents the result of a driver runtime binding operation."""

    success: bool
    state: DriverRuntimeBindingState
    message: str = ""