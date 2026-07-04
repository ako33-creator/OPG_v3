"""Tests for Project Model snapshot system."""

from opg.project_model import Project, ProjectSnapshotter


def test_project_snapshot_returns_snapshot_object():
    project = Project("Test Project")

    snapshot = ProjectSnapshotter.snapshot(project)

    assert snapshot is not None


def test_project_snapshot_contains_serialized_data():
    project = Project("Test Project")

    snapshot = ProjectSnapshotter.snapshot(project)

    assert isinstance(snapshot.data, dict)


def test_project_snapshot_is_independent_from_project():
    project = Project("Test Project")

    snapshot = ProjectSnapshotter.snapshot(project)

    # modification du snapshot ne doit pas impacter les données projet
    snapshot.data["modified"] = True

    # on vérifie sur la source sérialisée, pas sur metadata inexistant
    snapshot2 = ProjectSnapshotter.snapshot(project)

    assert "modified" not in snapshot2.data