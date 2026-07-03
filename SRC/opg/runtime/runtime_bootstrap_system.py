from __future__ import annotations

from enum import Enum

from opg.runtime.runtime_execution_engine import RuntimeExecutionEngine


class RuntimeBootstrapState(str, Enum):
    NOT_BOOTSTRAPPED = "not_bootstrapped"
    BOOTSTRAPPING = "bootstrapping"
    BOOTSTRAPPED = "bootstrapped"
    FAILED = "failed"


class RuntimeBootstrapSystem:
    def __init__(self, execution_engine: RuntimeExecutionEngine) -> None:
        self._execution_engine = execution_engine
        self._state = RuntimeBootstrapState.NOT_BOOTSTRAPPED

    @property
    def state(self) -> RuntimeBootstrapState:
        return self._state

    @property
    def is_bootstrapped(self) -> bool:
        return self._state == RuntimeBootstrapState.BOOTSTRAPPED

    def bootstrap(self) -> None:
        if self.is_bootstrapped:
            return

        self._state = RuntimeBootstrapState.BOOTSTRAPPING

        result = self._execution_engine.execute()

        if result.error is not None:
            self._state = RuntimeBootstrapState.FAILED
            raise result.error

        self._state = RuntimeBootstrapState.BOOTSTRAPPED

    def reset(self) -> None:
        self._execution_engine.reset()
        self._state = RuntimeBootstrapState.NOT_BOOTSTRAPPED