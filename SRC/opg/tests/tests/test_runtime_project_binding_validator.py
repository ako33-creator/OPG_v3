"""Tests for runtime project binding validator."""

from opg.runtime.project_binding_snapshot import RuntimeProjectBindingSnapshot
from opg.runtime.project_binding_state import RuntimeProjectBindingState
from opg.runtime.project_binding_validator import RuntimeProjectBindingValidator


class DummyProject:
    """Minimal project-like object used for validator tests."""


def test_validator_accepts_bound_snapshot_with_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.BOUND,
        project=DummyProject(),
    )
    validator = RuntimeProjectBindingValidator()

    assert validator.validate(snapshot) is True


def test_validator_rejects_bound_snapshot_without_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.BOUND,
        project=None,
    )
    validator = RuntimeProjectBindingValidator()

    assert validator.validate(snapshot) is False


def test_validator_accepts_unbound_snapshot_without_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.UNBOUND,
        project=None,
    )
    validator = RuntimeProjectBindingValidator()

    assert validator.validate(snapshot) is True


def test_validator_rejects_unbound_snapshot_with_project():
    snapshot = RuntimeProjectBindingSnapshot(
        state=RuntimeProjectBindingState.UNBOUND,
        project=DummyProject(),
    )
    validator = RuntimeProjectBindingValidator()

    assert validator.validate(snapshot) is False