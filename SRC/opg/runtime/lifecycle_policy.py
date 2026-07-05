"""Runtime lifecycle policy system."""

from __future__ import annotations

from abc import ABC, abstractmethod

from .control_plane import RuntimeControlState


class RuntimeLifecyclePolicy(ABC):
    """Contract for runtime lifecycle transition policies."""

    @abstractmethod
    def can_start(self, state: RuntimeControlState) -> bool:
        """Return whether the runtime can start from the current state."""

    @abstractmethod
    def can_stop(self, state: RuntimeControlState) -> bool:
        """Return whether the runtime can stop from the current state."""

    @abstractmethod
    def can_restart(self, state: RuntimeControlState) -> bool:
        """Return whether the runtime can restart from the current state."""

    @abstractmethod
    def can_fail(self, state: RuntimeControlState) -> bool:
        """Return whether the runtime can transition to the failed state."""


class DefaultRuntimeLifecyclePolicy(RuntimeLifecyclePolicy):
    """Default runtime lifecycle transition policy."""

    def can_start(self, state: RuntimeControlState) -> bool:
        """Allow start from created, stopped, or failed states."""
        return state in {
            RuntimeControlState.CREATED,
            RuntimeControlState.STOPPED,
            RuntimeControlState.FAILED,
        }

    def can_stop(self, state: RuntimeControlState) -> bool:
        """Allow stop only from the running state."""
        return state is RuntimeControlState.RUNNING

    def can_restart(self, state: RuntimeControlState) -> bool:
        """Allow restart from running or failed states."""
        return state in {
            RuntimeControlState.RUNNING,
            RuntimeControlState.FAILED,
        }

    def can_fail(self, state: RuntimeControlState) -> bool:
        """Allow failure transition from any non-failed state."""
        return state is not RuntimeControlState.FAILED