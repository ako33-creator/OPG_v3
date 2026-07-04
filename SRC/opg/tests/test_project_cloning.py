"""Tests for Project Model cloning."""

from opg.project_model import Project, ProjectCloner


def test_project_cloner_returns_new_project_instance():
    project = Project("Test Project")

    cloned_project = ProjectCloner.clone(project)

    assert cloned_project is not project


def test_project_cloner_preserves_project_name():
    project = Project("Original Project")

    cloned_project = ProjectCloner.clone(project)

    assert cloned_project.name == project.name


def test_project_cloner_creates_equal_but_distinct_project():
    project = Project("Original Project")

    cloned_project = ProjectCloner.clone(project)

    assert cloned_project == project
    assert cloned_project is not project