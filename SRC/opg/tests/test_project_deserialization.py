"""Tests for the OPG Project Model deserialization support."""

from opg.project_model import Project, ProjectDeserializer


def test_project_deserializer_deserializes_project():
    deserializer = ProjectDeserializer()

    project = deserializer.deserialize(
        {
            "name": "OPG Project",
        }
    )

    assert isinstance(project, Project)
    assert project.name == "OPG Project"


def test_project_deserializer_returns_project_instance():
    deserializer = ProjectDeserializer()

    project = deserializer.deserialize(
        {
            "name": "OPG Project",
        }
    )

    assert isinstance(project, Project)


def test_project_deserializer_preserves_project_name():
    deserializer = ProjectDeserializer()

    project = deserializer.deserialize(
        {
            "name": "OPG Project",
        }
    )

    assert project.name == "OPG Project"