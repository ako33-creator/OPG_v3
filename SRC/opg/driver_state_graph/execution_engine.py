"""Execution engine for state graph runtime system."""

from __future__ import annotations

from typing import Any

from .contract import StateGraphContract
from .resolver import StateGraphResolver
from .listener import StateGraphEventListener
from .diff_propagator import StateGraphDiffPropagator


class StateGraphExecutionEngine:
    """
    Executes the state graph lifecycle:
    - resolve graph
    - listen events
    - propagate diffs
    """

    def __init__(
        self,
        resolver: StateGraphResolver | None = None,
        listener: StateGraphEventListener | None = None,
        propagator: StateGraphDiffPropagator | None = None,
    ) -> None:
        self.resolver = resolver or StateGraphResolver()
        self.listener = listener or StateGraphEventListener()
        self.propagator = propagator or StateGraphDiffPropagator()

    def run(self, graph: StateGraphContract, diff: Any | None = None) -> dict[str, Any]:
        """Run full execution cycle."""

        resolved = self.resolver.resolve(graph)

        if diff is not None:
            self.propagator.propagate(graph, diff)

        self.listener.notify(graph, {"event": "execution_run"})

        return {
            "resolved": resolved,
            "status": "executed",
        }