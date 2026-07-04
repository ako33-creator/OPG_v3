"""Migration support for the OPG Project Model."""

from __future__ import annotations

from typing import Any, Callable


MigrationFunction = Callable[[dict[str, Any]], dict[str, Any]]


class ProjectMigration:
    """Represents a migration between two Project Model versions."""

    def __init__(
        self,
        source_version: str,
        target_version: str,
        migration_function: MigrationFunction,
    ) -> None:
        self.source_version = source_version
        self.target_version = target_version
        self._migration_function = migration_function

    def migrate(self, data: dict[str, Any]) -> dict[str, Any]:
        """Apply the migration to project data."""
        return self._migration_function(data)