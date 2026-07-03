from opg.project_model import (
    DEFAULT_PROJECT_VERSION,
    PROJECT_MODEL_SCHEMA_VERSION,
    Project,
)


def test_project_can_be_created():
    project = Project(name="Test Project")

    assert project.name == "Test Project"


def test_project_has_schema_version():
    project = Project(name="Test Project")

    assert project.schema_version == PROJECT_MODEL_SCHEMA_VERSION


def test_project_has_default_project_version():
    project = Project(name="Test Project")

    assert project.project_version == DEFAULT_PROJECT_VERSION


def test_project_skeleton_is_valid_with_name():
    project = Project(name="Valid Project")

    assert project.is_valid_skeleton() is True


def test_project_skeleton_is_invalid_without_name():
    project = Project(name="   ")

    assert project.is_valid_skeleton() is False