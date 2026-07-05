"""Runtime lifecycle transition history."""

from __future__ import annotations

from .lifecycle_transition import RuntimeLifecycleTransition


class RuntimeLifecycleHistory:
    """Stores runtime lifecycle transitions in insertion order."""

    def __init__(self) -> None:
        self._transitions: list[RuntimeLifecycleTransition] = []

    def record(self, transition: RuntimeLifecycleTransition) -> None:
        """Record a runtime lifecycle transition."""
        self._transitions.append(transition)

    def get_transitions(self) -> tuple[RuntimeLifecycleTransition, ...]:
        """Return all recorded transitions."""
        return tuple(self._transitions)

    def get_last_transition(self) -> RuntimeLifecycleTransition | None:
        """Return the most recently recorded transition, if any."""
        if not self._transitions:
            return None

        return self._transitions[-1]

    def clear(self) -> None:
        """Remove all recorded transitions."""
        self._transitions.clear()

    def __len__(self) -> int:
        """Return the number of recorded transitions."""
        return len(self._transitions)