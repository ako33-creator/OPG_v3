import pytest

from opg.runtime.runtime_bootstrap_system import (
    RuntimeBootstrapState,
    RuntimeBootstrapSystem,
)
from opg.runtime.runtime_execution_engine import RuntimeExecutionEngine
from opg.runtime.runtime_scheduler import RuntimeScheduler


def test_bootstrap_initial_state():
    scheduler = RuntimeScheduler()
    engine = RuntimeExecutionEngine(scheduler)

    bootstrap = RuntimeBootstrapSystem(engine)

    assert bootstrap.state == RuntimeBootstrapState.NOT_BOOTSTRAPPED
    assert bootstrap.is_bootstrapped is False


def test_bootstrap_executes_runtime():
    scheduler = RuntimeScheduler()

    executed = []

    scheduler.register_task(
        "boot",
        lambda: executed.append("boot"),
    )

    engine = RuntimeExecutionEngine(scheduler)
    bootstrap = RuntimeBootstrapSystem(engine)

    bootstrap.bootstrap()

    assert executed == ["boot"]
    assert bootstrap.state == RuntimeBootstrapState.BOOTSTRAPPED
    assert bootstrap.is_bootstrapped is True


def test_bootstrap_is_idempotent():
    scheduler = RuntimeScheduler()

    executed = []

    scheduler.register_task(
        "boot",
        lambda: executed.append("boot"),
    )

    engine = RuntimeExecutionEngine(scheduler)
    bootstrap = RuntimeBootstrapSystem(engine)

    bootstrap.bootstrap()
    bootstrap.bootstrap()

    assert executed == ["boot"]


def test_bootstrap_failure():
    scheduler = RuntimeScheduler()

    def failing():
        raise RuntimeError("failure")

    scheduler.register_task("boot", failing)

    engine = RuntimeExecutionEngine(scheduler)
    bootstrap = RuntimeBootstrapSystem(engine)

    with pytest.raises(RuntimeError):
        bootstrap.bootstrap()

    assert bootstrap.state == RuntimeBootstrapState.FAILED


def test_bootstrap_reset():
    scheduler = RuntimeScheduler()

    scheduler.register_task("boot", lambda: None)

    engine = RuntimeExecutionEngine(scheduler)
    bootstrap = RuntimeBootstrapSystem(engine)

    bootstrap.bootstrap()
    bootstrap.reset()

    assert bootstrap.state == RuntimeBootstrapState.NOT_BOOTSTRAPPED
    assert bootstrap.is_bootstrapped is False