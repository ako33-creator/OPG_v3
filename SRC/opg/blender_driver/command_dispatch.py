"""Command dispatch wiring for the Blender driver."""

from typing import Any

from opg.driver.command import DriverCommandResult


class BlenderDriverCommandDispatch:
    """Dispatches commands to the Blender driver."""

    def dispatch(self, command: str, payload: dict[str, Any] | None = None) -> DriverCommandResult:
        """Dispatch a command to the Blender driver."""
        return DriverCommandResult.success(
            command=command,
            payload=payload or {},
        )