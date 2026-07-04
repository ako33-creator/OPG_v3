"""Driver project binding adapter for OPG external runtime drivers."""

from __future__ import annotations

from typing import Any

from .interface import DriverInterface


class DriverProjectBindingAdapter:
    """Adapts an OPG driver to project binding operations."""

    def __init__(self, driver: DriverInterface) -> None:
        """Initialize the adapter with a driver."""
        self.driver = driver

    def bind_project(self, project: Any) -> None:
        """Bind a project to the adapted driver."""
        self.driver.initialize(project)

    def unbind_project(self) -> None:
        """Unbind a project from the adapted driver."""
        self.driver.shutdown()