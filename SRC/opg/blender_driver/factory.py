"""Factory for the Blender driver."""

from opg.blender_driver.adapter_bundle import BlenderDriverAdapterBundle
from opg.blender_driver.availability import BlenderDriverAvailability
from opg.blender_driver.command_dispatch import BlenderDriverCommandDispatch
from opg.blender_driver.context import BlenderDriverContext
from opg.blender_driver.driver import BlenderDriver
from opg.blender_driver.lifecycle import BlenderDriverLifecycle


class BlenderDriverFactory:
    """Creates Blender driver instances."""

    def create(self) -> BlenderDriver:
        """Create a Blender driver instance."""
        bundle = BlenderDriverAdapterBundle(
            availability=BlenderDriverAvailability(),
            lifecycle=BlenderDriverLifecycle(),
            command_dispatch=BlenderDriverCommandDispatch(),
            context=BlenderDriverContext(),
        )

        return BlenderDriver(adapter_bundle=bundle)