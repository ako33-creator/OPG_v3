"""Tests for Cross-System Consistency Validator."""

from opg.project_model.consistency import ProjectConsistencyValidator, ProjectConsistencyError


class DummyProject:
    def __init__(self, lifecycle_state="ACTIVE", project_id="123"):
        self.lifecycle_state = lifecycle_state
        self.project_id = project_id


def test_consistency_validator_passes_valid_project():
    project = DummyProject()

    assert ProjectConsistencyValidator.validate(project) is True


def test_consistency_validator_rejects_invalid_lifecycle():
    project = DummyProject(lifecycle_state="UNKNOWN")

    try:
        ProjectConsistencyValidator.validate(project)
        assert False
    except ProjectConsistencyError:
        assert True


def test_consistency_validator_rejects_missing_id():
    project = DummyProject()
    project.project_id = None

    try:
        ProjectConsistencyValidator.validate(project)
        assert False
    except ProjectConsistencyError:
        assert True


def test_consistency_validator_rejects_snapshot_locked_invalid_state():
    project = DummyProject(lifecycle_state="INACTIVE")
    project._snapshot_locked = True

    try:
        ProjectConsistencyValidator.validate(project)
        assert False
    except ProjectConsistencyError:
        assert True