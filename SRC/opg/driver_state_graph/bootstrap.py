"""Bootstrap helper for state graph system."""

from __future__ import annotations

from .builder import StateGraphBuilder
from .resolver import StateGraphResolver
from .execution_engine import StateGraphExecutionEngine
from .listener import StateGraphEventListener
from .diff_propagator import StateGraphDiffPropagator


class StateGraphBootstrap:
    """
    Initializes the full State Graph system.
    """

    def __init__(self) -> None:
        self.builder = StateGraphBuilder()
        self.resolver = StateGraphResolver()
        self.listener = StateGraphEventListener()
        self.propagator = StateGraphDiffPropagator()

        self.engine = StateGraphExecutionEngine(
            resolver=self.resolver,
            listener=self.listener,
            propagator=self.propagator,
        )

    def get_engine(self) -> StateGraphExecutionEngine:
        """Return execution engine."""
        return self.engine