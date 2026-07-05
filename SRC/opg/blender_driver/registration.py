"""Registration helper for the Blender driver."""

from opg.blender_driver.factory import BlenderDriverFactory
from opg.driver.registry import DriverRegistry


def register_blender_driver(registry: DriverRegistry) -> None:
    """Register the Blender driver factory in a driver registry."""
    registry.register(
        name="blender",
        factory=BlenderDriverFactory(),
    )