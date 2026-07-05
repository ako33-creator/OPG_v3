"""Runtime bootstrap helper for the Blender driver."""

from opg.blender_driver.driver import BlenderDriver
from opg.blender_driver.factory import BlenderDriverFactory


def bootstrap_blender_driver() -> BlenderDriver:
    """Create and return a Blender driver ready for runtime integration."""
    return BlenderDriverFactory().create()