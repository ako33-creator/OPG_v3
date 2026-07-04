"""Tests for runtime project binding state definitions."""

from opg.runtime.project_binding_state import RuntimeProjectBindingState


def test_runtime_project_binding_state_unbound_value():
    assert RuntimeProjectBindingState.UNBOUND.value == "unbound"


def test_runtime_project_binding_state_bound_value():
    assert RuntimeProjectBindingState.BOUND.value == "bound"


def test_runtime_project_binding_state_is_string_enum():
    assert isinstance(RuntimeProjectBindingState.UNBOUND, str)
    assert isinstance(RuntimeProjectBindingState.BOUND, str)