"""Tests for runtime project binding errors."""

from opg.runtime.project_binding_error import RuntimeProjectBindingError


def test_runtime_project_binding_error_is_runtime_error():
    error = RuntimeProjectBindingError()

    assert isinstance(error, RuntimeError)


def test_runtime_project_binding_error_preserves_message():
    message = "Active project binding required"

    error = RuntimeProjectBindingError(message)

    assert str(error) == message


def test_runtime_project_binding_error_can_be_raised():
    try:
        raise RuntimeProjectBindingError("Project binding unavailable")
    except RuntimeProjectBindingError as error:
        assert str(error) == "Project binding unavailable"