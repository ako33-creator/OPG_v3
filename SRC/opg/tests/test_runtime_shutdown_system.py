import pytest

from opg.runtime.runtime_bootstrap_system import RuntimeBootstrapSystem
from opg.runtime.runtime_execution_engine import RuntimeExecutionEngine
from opg.runtime.runtime_scheduler import RuntimeScheduler
from opg.runtime.runtime_shutdown_system import (
    RuntimeShutdownState,
    RuntimeShutdownSystem,
)


def create_shutdown_system():
    scheduler = RuntimeScheduler()
    scheduler.register_task("boot", lambda: None)

    engine = RuntimeExecutionEngine(scheduler)
    bootstrap = RuntimeBootstrapSystem(engine)

    bootstrap.bootstrap()

    return RuntimeShutdownSystem(bootstrap)


def test_shutdown_initial_state():
    shutdown = create_shutdown_system()

    assert shutdown.state == RuntimeShutdownState.NOT_SHUTDOWN
    assert shutdown.is_shutdown is False


def test_shutdown_runtime():
    shutdown = create_shutdown_system()

    shutdown.shutdown()

    assert shutdown.state == RuntimeShutdownState.SHUTDOWN
    assert shutdown.is_shutdown is True


def test_shutdown_is_idempotent():
    shutdown = create_shutdown_system()

    shutdown.shutdown()
    shutdown.shutdown()

    assert shutdown.state == RuntimeShutdownState.SHUTDOWN


def test_shutdown_reset():
    shutdown = create_shutdown_system()

    shutdown.shutdown()
    shutdown.reset()

    assert shutdown.state == RuntimeShutdownState.NOT_SHUTDOWN
    assert shutdown.is_shutdown is False


def test_shutdown_failure():
    class BrokenBootstrap:
        def reset(self):
            raise RuntimeError("shutdown failed")

    shutdown = RuntimeShutdownSystem(BrokenBootstrap())

    with pytest.raises(RuntimeError):
        shutdown.shutdown()

    assert shutdown.state == RuntimeShutdownState.FAILED