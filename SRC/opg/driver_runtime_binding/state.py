"""State model for driver runtime bindings."""

from enum import Enum


class DriverRuntimeBindingState(Enum):
    """Represents the state of a driver runtime binding."""

    UNBOUND = "unbound"
    BOUND = "bound"