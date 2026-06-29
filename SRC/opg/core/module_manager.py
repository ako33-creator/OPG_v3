"""
OPG Core Module Manager.

Central registry and lifecycle coordinator for OPG modules.

Rules:
- No Blender dependency.
- No external dependency.
- No silent overwrite.
"""

from enum import Enum
from typing import Any, Dict, Iterator, Optional

from .exceptions import OPGModuleError


class ModuleState(str, Enum):
    """
    Official lifecycle states for OPG modules.
    """

    REGISTERED = "registered"
    INITIALIZED = "initialized"
    STARTED = "started"
    STOPPED = "stopped"
    FAILED = "failed"


class ModuleRecord:
    """
    Internal record describing a registered module.
    """

    def __init__(self, name: str, module: Any) -> None:
        if not isinstance(name, str) or not name.strip():
            raise OPGModuleError("Module name must be a non-empty string.")

        if module is None:
            raise OPGModuleError("Module instance cannot be None.")

        self.name = name
        self.module = module
        self.state = ModuleState.REGISTERED
        self.error: Optional[Exception] = None

    def mark_initialized(self) -> None:
        self.state = ModuleState.INITIALIZED
        self.error = None

    def mark_started(self) -> None:
        self.state = ModuleState.STARTED
        self.error = None

    def mark_stopped(self) -> None:
        self.state = ModuleState.STOPPED
        self.error = None

    def mark_failed(self, error: Exception) -> None:
        self.state = ModuleState.FAILED
        self.error = error


class ModuleManager:
    """
    Registers modules and coordinates their lifecycle.

    A module may optionally expose the following methods:

    - initialize()
    - start()
    - stop()

    Missing lifecycle methods are ignored.
    """

    def __init__(self) -> None:
        self._modules: Dict[str, ModuleRecord] = {}

    def register(self, name: str, module: Any, *, replace: bool = False) -> None:
        """
        Register a module.

        Args:
            name: Unique module name.
            module: Module instance.
            replace: Allow replacing an existing module.

        Raises:
            OPGModuleError: If name/module is invalid or already registered.
        """
        self._validate_name(name)

        if module is None:
            raise OPGModuleError("Cannot register a None module.")

        if name in self._modules and not replace:
            raise OPGModuleError(f"Module already registered: {name}")

        self._modules[name] = ModuleRecord(name, module)

    def get(self, name: str) -> Any:
        """
        Return a registered module instance.
        """
        return self.get_record(name).module

    def get_record(self, name: str) -> ModuleRecord:
        """
        Return the internal record for a registered module.
        """
        self._validate_name(name)

        if name not in self._modules:
            raise OPGModuleError(f"Module not registered: {name}")

        return self._modules[name]

    def has(self, name: str) -> bool:
        """
        Check whether a module exists.
        """
        self._validate_name(name)
        return name in self._modules

    def unregister(self, name: str) -> None:
        """
        Remove a registered module.

        Raises:
            OPGModuleError: If the module does not exist.
        """
        self._validate_name(name)

        if name not in self._modules:
            raise OPGModuleError(f"Cannot unregister missing module: {name}")

        del self._modules[name]

    def initialize(self, name: str) -> None:
        """
        Initialize a single module.

        If the module exposes initialize(), it is called.
        """
        record = self.get_record(name)

        try:
            method = getattr(record.module, "initialize", None)
            if callable(method):
                method()
            record.mark_initialized()
        except Exception as exc:
            record.mark_failed(exc)
            raise OPGModuleError(f"Failed to initialize module: {name}") from exc

    def start(self, name: str) -> None:
        """
        Start a single module.

        If the module exposes start(), it is called.
        """
        record = self.get_record(name)

        try:
            method = getattr(record.module, "start", None)
            if callable(method):
                method()
            record.mark_started()
        except Exception as exc:
            record.mark_failed(exc)
            raise OPGModuleError(f"Failed to start module: {name}") from exc

    def stop(self, name: str) -> None:
        """
        Stop a single module.

        If the module exposes stop(), it is called.
        """
        record = self.get_record(name)

        try:
            method = getattr(record.module, "stop", None)
            if callable(method):
                method()
            record.mark_stopped()
        except Exception as exc:
            record.mark_failed(exc)
            raise OPGModuleError(f"Failed to stop module: {name}") from exc

    def initialize_all(self) -> None:
        """
        Initialize all registered modules in registration order.
        """
        for name in list(self._modules.keys()):
            self.initialize(name)

    def start_all(self) -> None:
        """
        Start all registered modules in registration order.
        """
        for name in list(self._modules.keys()):
            self.start(name)

    def stop_all(self) -> None:
        """
        Stop all started/initialized modules in reverse registration order.
        """
        for name in reversed(list(self._modules.keys())):
            record = self._modules[name]
            if record.state in (ModuleState.STARTED, ModuleState.INITIALIZED):
                self.stop(name)

    def clear(self) -> None:
        """
        Remove all registered modules.
        """
        self._modules.clear()

    def names(self) -> Iterator[str]:
        """
        Iterate over registered module names.
        """
        return iter(self._modules.keys())

    def modules(self) -> Iterator[Any]:
        """
        Iterate over registered module instances.
        """
        for record in self._modules.values():
            yield record.module

    def records(self) -> Iterator[ModuleRecord]:
        """
        Iterate over module records.
        """
        return iter(self._modules.values())

    def items(self) -> Iterator[tuple[str, Any]]:
        """
        Iterate over module name / instance pairs.
        """
        for name, record in self._modules.items():
            yield name, record.module

    def count(self) -> int:
        """
        Return the number of registered modules.
        """
        return len(self._modules)

    def _validate_name(self, name: str) -> None:
        """
        Validate a module name.
        """
        if not isinstance(name, str):
            raise OPGModuleError("Module name must be a string.")

        if not name.strip():
            raise OPGModuleError("Module name cannot be empty.")