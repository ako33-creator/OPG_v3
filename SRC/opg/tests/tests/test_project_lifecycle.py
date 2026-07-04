"""Tests for Project Lifecycle Manager."""

from opg.project_model.lifecycle import ProjectLifecycleManager, ProjectLifecycleState
from opg.project_model import Project


def test_project_lifecycle_create_sets_state():
    project = Project("Test Project")

    ProjectLifecycleManager.create(project)

    assert project.lifecycle_state == ProjectLifecycleState.CREATED


def test_project_lifecycle_activate_sets_state():
    project = Project("Test Project")

    ProjectLifecycleManager.activate(project)

    assert project.lifecycle_state == ProjectLifecycleState.ACTIVE


def test_project_lifecycle_deactivate_sets_state():
    project = Project("Test Project")

    ProjectLifecycleManager.deactivate(project)

    assert project.lifecycle_state == ProjectLifecycleState.INACTIVE


def test_project_lifecycle_destroy_sets_state():
    project = Project("Test Project")

    ProjectLifecycleManager.destroy(project)

    assert project.lifecycle_state == ProjectLifecycleState.DESTROYED