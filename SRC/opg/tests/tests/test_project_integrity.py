"""Tests for Project Integrity Final Guard."""

from opg.project_model.integrity import ProjectIntegrityGuard, ProjectIntegrityError
from opg.project_model import Project


class DummyProject:
    def __init__(self, lifecycle_state=None):
        self.lifecycle_state = lifecycle_state
        self.project_id = "123"


def test_integrity_passes_for_valid_project():
    project = DummyProject(lifecycle_state="ACTIVE")

    assert ProjectIntegrityGuard.validate(project) is True


def test_integrity_fails_without_lifecycle():
    project = DummyProject()
    del project.lifecycle_state

    try:
        ProjectIntegrityGuard.validate(project)
        assert False
    except ProjectIntegrityError:
        assert True


def test_integrity_fails_when_destroyed():
    project = DummyProject(lifecycle_state="DESTROYED")

    try:
        ProjectIntegrityGuard.validate(project)
        assert False
    except ProjectIntegrityError:
        assert True


def test_integrity_fails_without_id():
    class BadProject:
        lifecycle_state = "ACTIVE"

    project = BadProject()

    try:
        ProjectIntegrityGuard.validate(project)
        assert False
    except ProjectIntegrityError:
        assert True