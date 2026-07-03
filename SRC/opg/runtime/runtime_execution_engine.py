from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from opg.runtime.runtime_scheduler import RuntimeScheduler


class RuntimeExecutionState(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class RuntimeExecutionResult:
    state: RuntimeExecutionState
    error: Optional[Exception] = None


class RuntimeExecutionEngine:
    def __init__(self, scheduler: RuntimeScheduler) -> None:
        self._scheduler = scheduler
        self._state = RuntimeExecutionState.IDLE
        self._last_result: Optional[RuntimeExecutionResult] = None

    @property
    def state(self) -> RuntimeExecutionState:
        return self._state

    @property
    def last_result(self) -> Optional[RuntimeExecutionResult]:
        return self._last_result

    def execute(self) -> RuntimeExecutionResult:
        self._state = RuntimeExecutionState.RUNNING

        try:
            self._scheduler.run_all()
        except Exception as error:
            self._state = RuntimeExecutionState.FAILED
            self._last_result = RuntimeExecutionResult(
                state=self._state,
                error=error,
            )
            return self._last_result

        self._state = RuntimeExecutionState.COMPLETED
        self._last_result = RuntimeExecutionResult(state=self._state)
        return self._last_result

    def reset(self) -> None:
        self._scheduler.reset()
        self._state = RuntimeExecutionState.IDLE
        self._last_result = None