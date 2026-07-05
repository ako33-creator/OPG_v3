"""Adapter bundle for the Blender driver."""

from dataclasses import dataclass

from opg.blender_driver.availability import BlenderDriverAvailability
from opg.blender_driver.command_dispatch import BlenderDriverCommandDispatch
from opg.blender_driver.context import BlenderDriverContext
from opg.blender_driver.lifecycle import BlenderDriverLifecycle


@dataclass(slots=True)
class BlenderDriverAdapterBundle:
    """Bundles Blender driver runtime adapters."""

    availability: BlenderDriverAvailability
    lifecycle: BlenderDriverLifecycle
    command_dispatch: BlenderDriverCommandDispatch
    context: BlenderDriverContext