"""Tests for Project Model diff."""

from opg.project_model import Project, ProjectDiffer


def test_project_diff_returns_diff_object():
    left = Project("Test Project")
    right = Project("Test Project")

    diff = ProjectDiffer.diff(left, right)

    assert diff is not None


def test_project_diff_detects_no_changes_for_identical_projects():
    project = Project("Test Project")

    diff = ProjectDiffer.diff(project, project)

    assert diff.has_changes is False


def test_project_diff_detects_name_change():
    left = Project("Left Project")
    right = Project("Right Project")

    diff = ProjectDiffer.diff(left, right)

    assert diff.has_changes is True


def test_project_diff_contains_added_removed_or_changed_fields():
    left = Project("A")
    right = Project("B")

    diff = ProjectDiffer.diff(left, right)

    assert isinstance(diff.added, dict)
    assert isinstance(diff.removed, dict)
    assert isinstance(diff.changed, dict)