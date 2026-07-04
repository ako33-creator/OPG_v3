"""Runtime binding contract for OPG Project Model instances."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RuntimeProjectBinding:
    """Immutable contract binding a runtime session to a project model."""

    project: Any

    def get_project(self) -> Any:
        """Return the bound project model instance."""
        return self.project