"""Availability wiring for the Blender driver."""

from opg.driver.availability import DriverAvailability


class BlenderDriverAvailability:
    """Provides Blender driver availability state."""

    def get_availability(self) -> DriverAvailability:
        """Return the current Blender driver availability."""
        return DriverAvailability.AVAILABLE