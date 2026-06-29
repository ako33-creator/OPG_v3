"""
OPG Core Application.

Official application lifecycle orchestrator for OPG.

Rules:
- No Blender dependency.
- No external dependency.
- Application lifecycle must be explicit and deterministic.
"""

from enum import Enum
from typing import Optional

from .exceptions import OPGApplicationError, OPGLifecycleError
from .module_manager import ModuleManager
from .service_registry import ServiceRegistry


class ApplicationState(str, Enum):
    """
    Official lifecycle states for the OPG application.
    """

    CREATED = "created"
    INITIALIZED = "initialized"
    RUNNING = "running"
    STOPPED = "stopped"
    FAILED = "failed"


class Application:
    """
    Main OPG application object.

    The Application coordinates:
    - service registry
    - module manager
    - initialization
    - startup
    - shutdown
    """

    def __init__(
        self,
        service_registry: Optional[ServiceRegistry] = None,
        module_manager: Optional[ModuleManager] = None,
    ) -> None:
        self._state = ApplicationState.CREATED
        self._service_registry = service_registry or ServiceRegistry()
        self._module_manager = module_manager or ModuleManager()
        self._last_error: Optional[Exception] = None

    @property
    def state(self) -> ApplicationState:
        """
        Return the current application state.
        """
        return self._state

    @property
    def services(self) -> ServiceRegistry:
        """
        Return the application service registry.
        """
        return self._service_registry

    @property
    def modules(self) -> ModuleManager:
        """
        Return the application module manager.
        """
        return self._module_manager

    @property
    def last_error(self) -> Optional[Exception]:
        """
        Return the last lifecycle error, if any.
        """
        return self._last_error

    def initialize(self) -> None:
        """
        Initialize the application.

        This method may only be called from CREATED or STOPPED.
        """
        if self._state not in (ApplicationState.CREATED, ApplicationState.STOPPED):
            raise OPGLifecycleError(
                f"Cannot initialize application from state: {self._state.value}"
            )

        try:
            self._module_manager.initialize_all()
            self._state = ApplicationState.INITIALIZED
            self._last_error = None
        except Exception as exc:
            self._state = ApplicationState.FAILED
            self._last_error = exc
            raise OPGApplicationError("Application initialization failed.") from exc

    def start(self) -> None:
        """
        Start the application.

        If the application is still CREATED, it is initialized first.
        """
        if self._state == ApplicationState.CREATED:
            self.initialize()

        if self._state != ApplicationState.INITIALIZED:
            raise OPGLifecycleError(
                f"Cannot start application from state: {self._state.value}"
            )

        try:
            self._module_manager.start_all()
            self._state = ApplicationState.RUNNING
            self._last_error = None
        except Exception as exc:
            self._state = ApplicationState.FAILED
            self._last_error = exc
            raise OPGApplicationError("Application start failed.") from exc

    def stop(self) -> None:
        """
        Stop the application.

        Stop is allowed from RUNNING or INITIALIZED.
        """
        if self._state not in (
            ApplicationState.RUNNING,
            ApplicationState.INITIALIZED,
        ):
            raise OPGLifecycleError(
                f"Cannot stop application from state: {self._state.value}"
            )

        try:
            self._module_manager.stop_all()
            self._state = ApplicationState.STOPPED
            self._last_error = None
        except Exception as exc:
            self._state = ApplicationState.FAILED
            self._last_error = exc
            raise OPGApplicationError("Application stop failed.") from exc

    def reset(self) -> None:
        """
        Reset the application to a clean CREATED state.

        Reset is only allowed when the application is STOPPED or FAILED.
        """
        if self._state not in (ApplicationState.STOPPED, ApplicationState.FAILED):
            raise OPGLifecycleError(
                f"Cannot reset application from state: {self._state.value}"
            )

        self._module_manager.clear()
        self._service_registry.clear()
        self._last_error = None
        self._state = ApplicationState.CREATED

    def is_created(self) -> bool:
        """
        Return True if the application is in CREATED state.
        """
        return self._state == ApplicationState.CREATED

    def is_initialized(self) -> bool:
        """
        Return True if the application is in INITIALIZED state.
        """
        return self._state == ApplicationState.INITIALIZED

    def is_running(self) -> bool:
        """
        Return True if the application is in RUNNING state.
        """
        return self._state == ApplicationState.RUNNING

    def is_stopped(self) -> bool:
        """
        Return True if the application is in STOPPED state.
        """
        return self._state == ApplicationState.STOPPED

    def is_failed(self) -> bool:
        """
        Return True if the application is in FAILED state.
        """
        return self._state == ApplicationState.FAILED