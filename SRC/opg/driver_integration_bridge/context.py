"""Context model for Driver Integration Bridge."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DriverIntegrationContext:
    """
    Immutable context passed through the integration pipeline.

    This context carries runtime state needed to:
    - synchronize drivers
    - emit events
    - compute diffs
    - execute bridge logic
    """

    runtime_state: Any
    project_model: Any
    driver_state: Any
    metadata: dict[str, Any] = None