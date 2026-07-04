"""Tests for Project Validation Rules Expansion."""

from opg.project_model.validation_rules import ValidationRule, ValidationRuleSet


class DummyProject:
    def __init__(self, valid: bool = True):
        self.valid = valid


def test_validation_rule_passes_when_true():
    project = DummyProject(valid=True)

    rule = ValidationRule(
        name="always_true",
        check=lambda p: True,
        message="Should never fail",
    )

    assert rule.validate(project) is True


def test_validation_rule_fails_when_false():
    project = DummyProject(valid=False)

    rule = ValidationRule(
        name="always_false",
        check=lambda p: False,
        message="Failure expected",
    )

    assert rule.validate(project) is False


def test_validation_rule_set_collects_errors():
    project = DummyProject(valid=False)

    rules = ValidationRuleSet()

    rules.add(
        ValidationRule(
            name="rule_1",
            check=lambda p: False,
            message="Error 1",
        )
    )

    rules.add(
        ValidationRule(
            name="rule_2",
            check=lambda p: False,
            message="Error 2",
        )
    )

    errors = rules.validate(project)

    assert "Error 1" in errors
    assert "Error 2" in errors


def test_validation_rule_set_handles_exceptions():
    project = DummyProject()

    rules = ValidationRuleSet()

    rules.add(
        ValidationRule(
            name="broken_rule",
            check=lambda p: 1 / 0,
            message="Should not crash",
        )
    )

    errors = rules.validate(project)

    assert any("broken_rule" in e for e in errors)