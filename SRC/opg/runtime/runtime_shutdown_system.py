from __future__ import annotations

from enum import Enum

from opg.runtime.runtime_bootstrap_system import RuntimeBootstrapSystem


class RuntimeShutdownState(str, Enum):
    NOT_SHUTDOWN = "not_shutdown"
    SHUTTING_DOWN = "shutting_down"
    SHUTDOWN = "shutdown"
    FAILED = "failed"


class RuntimeShutdownSystem:
    def __init__(self, bootstrap_system: RuntimeBootstrapSystem) -> None:
        self._bootstrap_system = bootstrap_system
        self._state = RuntimeShutdownState.NOT_SHUTDOWN

    @property
    def state(self) -> RuntimeShutdownState:
        return self._state

    @property
    def is_shutdown(self) -> bool:
        return self._state == RuntimeShutdownState.SHUTDOWN

    def shutdown(self) -> None:
        if self.is_shutdown:
            return

        self._state = RuntimeShutdownState.SHUTTING_DOWN

        try:
            self._bootstrap_system.reset()
        except Exception:
            self._state = RuntimeShutdownState.FAILED
            raise

        self._state = RuntimeShutdownState.SHUTDOWN

    def reset(self) -> None:
        self._state = RuntimeShutdownState.NOT_SHUTDOWN