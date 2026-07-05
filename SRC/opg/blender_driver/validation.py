"""Validation helper for the Blender driver."""

from opg.blender_driver.driver import BlenderDriver


def validate_blender_driver(driver: BlenderDriver) -> bool:
    """Validate a Blender driver instance."""
    return isinstance(driver, BlenderDriver)