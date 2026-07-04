"""Tests for runtime project binding status."""

from opg.runtime.project_binding_state import RuntimeProjectBindingState
from opg.runtime.project_binding_status import RuntimeProjectBindingStatus


def test_binding_status_reports_bound_state():
    status = RuntimeProjectBindingStatus(
        state=RuntimeProjectBindingState.BOUND
    )

    assert status.is_bound() is True


def test_binding_status_reports_unbound_state():
    status = RuntimeProjectBindingStatus(
        state=RuntimeProjectBindingState.UNBOUND
    )

    assert status.is_bound() is False


def test_binding_status_preserves_state():
    status = RuntimeProjectBindingStatus(
        state=RuntimeProjectBindingState.BOUND
    )

    assert status.state == RuntimeProjectBindingState.BOUND


def test_binding_status_is_immutable():
    status = RuntimeProjectBindingStatus(
        state=RuntimeProjectBindingState.UNBOUND
    )

    try:
        status.state = RuntimeProjectBindingState.BOUND
    except Exception:
        pass

    assert status.state == RuntimeProjectBindingState.UNBOUND