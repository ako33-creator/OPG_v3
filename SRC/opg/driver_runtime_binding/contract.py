"""Contract for binding a driver to the OPG runtime."""

from abc import ABC, abstractmethod

from opg.driver.interface import DriverInterface


class DriverRuntimeBindingContract(ABC):
    """Defines the contract for driver runtime bindings."""

    @abstractmethod
    def bind(self, driver: DriverInterface) -> None:
        """Bind a driver to the runtime."""

    @abstractmethod
    def unbind(self) -> None:
        """Unbind the current driver from the runtime."""

    @abstractmethod
    def is_bound(self) -> bool:
        """Return whether a driver is currently bound."""