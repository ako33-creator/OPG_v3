"""Tests for the OPG Project Model migration support."""

from opg.project_model import ProjectMigration


def test_project_migration_stores_versions():
    migration = ProjectMigration(
        source_version="1.0.0",
        target_version="2.0.0",
        migration_function=lambda data: data,
    )

    assert migration.source_version == "1.0.0"
    assert migration.target_version == "2.0.0"


def test_project_migration_applies_migration_function():
    def add_version(data):
        migrated_data = dict(data)
        migrated_data["version"] = "2.0.0"
        return migrated_data

    migration = ProjectMigration(
        source_version="1.0.0",
        target_version="2.0.0",
        migration_function=add_version,
    )

    result = migration.migrate({"name": "OPG Project"})

    assert result == {
        "name": "OPG Project",
        "version": "2.0.0",
    }


def test_project_migration_returns_migration_result():
    expected = {"name": "Migrated Project"}

    migration = ProjectMigration(
        source_version="1.0.0",
        target_version="2.0.0",
        migration_function=lambda data: expected,
    )

    result = migration.migrate({"name": "OPG Project"})

    assert result is expected