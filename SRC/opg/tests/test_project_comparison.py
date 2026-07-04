"""Tests for Project Model comparison."""

from opg.project_model import Project, ProjectComparator


def test_project_comparator_returns_comparison_result():
    project = Project("Test Project")

    comparison = ProjectComparator.compare(project, project)

    assert comparison is not None


def test_project_comparator_reports_equal_projects():
    left_project = Project("Test Project")
    right_project = left_project

    comparison = ProjectComparator.compare(left_project, right_project)

    assert comparison.are_equal is True


def test_project_comparator_reports_different_projects():
    left_project = Project("Left Project")
    right_project = Project("Right Project")

    comparison = ProjectComparator.compare(left_project, right_project)

    assert comparison.are_equal is False


def test_project_comparator_preserves_left_serialized_data():
    project = Project("Test Project")

    comparison = ProjectComparator.compare(project, project)

    assert comparison.left_data == comparison.right_data


def test_project_comparator_returns_distinct_serialized_data_objects():
    project = Project("Test Project")

    comparison = ProjectComparator.compare(project, project)

    assert comparison.left_data is not comparison.right_data