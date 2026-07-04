"""Blender driver command dispatcher for OPG."""

from __future__ import annotations

from typing import Callable

from opg.driver import DriverCommand, DriverResult


class BlenderDriverCommandDispatcher:
    """Dispatches Blender driver commands to registered handlers."""

    def __init__(self) -> None:
        """Initialize an empty Blender driver command dispatcher."""
        self._handlers: dict[str, Callable[[DriverCommand], DriverResult]] = {}

    def register_handler(
        self,
        command_name: str,
        handler: Callable[[DriverCommand], DriverResult],
    ) -> None:
        """Register a handler for a command name."""
        self._handlers[command_name] = handler

    def unregister_handler(self, command_name: str) -> None:
        """Remove a handler for a command name if it exists."""
        self._handlers.pop(command_name, None)

    def has_handler(self, command_name: str) -> bool:
        """Return whether a handler exists for a command name."""
        return command_name in self._handlers

    def dispatch(self, command: DriverCommand) -> DriverResult:
        """Dispatch a command to its registered handler."""
        handler = self._handlers.get(command.name)
        if handler is None:
            return DriverResult(
                success=False,
                message=f"No Blender command handler registered for '{command.name}'.",
            )

        return handler(command)