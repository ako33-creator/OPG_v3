from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, Optional


class RuntimeRecoveryState(str, Enum):
    IDLE = "idle"
    RECOVERING = "recovering"
    RECOVERED = "recovered"
    FAILED = "failed"


@dataclass(frozen=True)
class RuntimeRecoveryResult:
    state: RuntimeRecoveryState
    message: str = ""
    error: Optional[Exception] = None


RuntimeRecoveryAction = Callable[[], None]


class RuntimeRecoverySystem:
    def __init__(self) -> None:
        self._actions: Dict[str, RuntimeRecoveryAction] = {}
        self._state = RuntimeRecoveryState.IDLE
        self._last_result: Optional[RuntimeRecoveryResult] = None

    @property
    def state(self) -> RuntimeRecoveryState:
        return self._state

    @property
    def last_result(self) -> Optional[RuntimeRecoveryResult]:
        return self._last_result

    def register_action(self, name: str, action: RuntimeRecoveryAction) -> None:
        if name in self._actions:
            raise ValueError(f"Runtime recovery action already registered: {name}")

        self._actions[name] = action

    def has_action(self, name: str) -> bool:
        return name in self._actions

    def recover(self, name: str) -> RuntimeRecoveryResult:
        if name not in self._actions:
            raise KeyError(f"Runtime recovery action not found: {name}")

        self._state = RuntimeRecoveryState.RECOVERING

        try:
            self._actions[name]()
        except Exception as error:
            self._state = RuntimeRecoveryState.FAILED
            self._last_result = RuntimeRecoveryResult(
                state=self._state,
                message=f"Recovery failed: {name}",
                error=error,
            )
            return self._last_result

        self._state = RuntimeRecoveryState.RECOVERED
        self._last_result = RuntimeRecoveryResult(
            state=self._state,
            message=f"Recovery completed: {name}",
        )
        return self._last_result

    def reset(self) -> None:
        self._state = RuntimeRecoveryState.IDLE
        self._last_result = None

    def clear(self) -> None:
        self._actions.clear()
        self.reset()