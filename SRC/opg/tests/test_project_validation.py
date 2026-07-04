"""Tests for the OPG Project Model validation support."""

from opg.project_model import ValidationError, ValidationResult


def test_validation_error_stores_required_data():
    error = ValidationError(
        code="missing_name",
        message="Project name is required.",
    )

    assert error.code == "missing_name"
    assert error.message == "Project name is required."
    assert error.path == ""


def test_validation_error_stores_path():
    error = ValidationError(
        code="missing_name",
        message="Scene name is required.",
        path="scenes[0].name",
    )

    assert error.path == "scenes[0].name"


def test_validation_result_starts_valid():
    result = ValidationResult()

    assert result.is_valid is True
    assert result.errors == ()


def test_validation_result_can_add_error():
    result = ValidationResult()

    result.add_error(
        code="missing_name",
        message="Project name is required.",
    )

    assert result.is_valid is False
    assert len(result.errors) == 1


def test_validation_result_preserves_error_data():
    result = ValidationResult()

    result.add_error(
        code="invalid_scene",
        message="Scene is invalid.",
        path="scenes[0]",
    )

    error = result.errors[0]

    assert error.code == "invalid_scene"
    assert error.message == "Scene is invalid."
    assert error.path == "scenes[0]"


def test_validation_result_errors_are_immutable():
    result = ValidationResult()

    result.add_error(
        code="invalid_project",
        message="Project is invalid.",
    )

    assert isinstance(result.errors, tuple)