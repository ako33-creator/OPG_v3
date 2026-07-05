"""Bootstrap helper for driver runtime binding services."""

from __future__ import annotations

from .factory import DriverRuntimeBindingFactory
from .registry import DriverRuntimeBindingRegistry


class DriverRuntimeBindingBootstrap:
    """Prepare driver runtime binding services."""

    def __init__(
        self,
        registry: DriverRuntimeBindingRegistry | None = None,
        factory: DriverRuntimeBindingFactory | None = None,
    ) -> None:
        self.registry = registry or DriverRuntimeBindingRegistry()
        self.factory = factory or DriverRuntimeBindingFactory(self.registry)

    def bootstrap(self) -> DriverRuntimeBindingFactory:
        """Return a ready-to-use driver runtime binding factory."""
        return self.factory