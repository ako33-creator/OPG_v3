"""Blender driver implementation for OPG."""

from __future__ import annotations

from typing import Any

from opg.driver import DriverInterface

from .availability import is_blender_available
from .identity import BLENDER_DRIVER_NAME, BLENDER_DRIVER_VERSION
from .lifecycle import BlenderDriverLifecycle


class BlenderDriver(DriverInterface):
    """OPG driver implementation for Blender.

    This class wires the Blender Driver Foundation into the generic
    DriverInterface contract without importing Blender directly.
    """

    def __init__(self) -> None:
        """Initialize the Blender driver."""
        self.lifecycle = BlenderDriverLifecycle()
        self.context: Any | None = None

    @property
    def name(self) -> str:
        """Return the Blender driver name."""
        return BLENDER_DRIVER_NAME

    @property
    def version(self) -> str:
        """Return the Blender driver version."""
        return BLENDER_DRIVER_VERSION

    def initialize(self, context: Any | None = None) -> None:
        """Initialize the Blender driver with an optional context."""
        self.context = context
        self.lifecycle.initialize()

    def shutdown(self) -> None:
        """Shutdown the Blender driver."""
        self.context = None
        self.lifecycle.shutdown()

    def is_available(self) -> bool:
        """Return whether Blender is available."""
        return is_blender_available()