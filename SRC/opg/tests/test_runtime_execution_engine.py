from opg.runtime.runtime_execution_engine import (
    RuntimeExecutionEngine,
    RuntimeExecutionState,
)
from opg.runtime.runtime_scheduler import RuntimeScheduler


def test_runtime_execution_engine_starts_idle():
    scheduler = RuntimeScheduler()
    engine = RuntimeExecutionEngine(scheduler)

    assert engine.state == RuntimeExecutionState.IDLE
    assert engine.last_result is None


def test_runtime_execution_engine_executes_scheduler_tasks():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("boot", lambda: executed.append("boot"))

    engine = RuntimeExecutionEngine(scheduler)
    result = engine.execute()

    assert executed == ["boot"]
    assert result.state == RuntimeExecutionState.COMPLETED
    assert result.error is None
    assert engine.state == RuntimeExecutionState.COMPLETED
    assert engine.last_result == result


def test_runtime_execution_engine_runs_task_dependencies():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("config", lambda: executed.append("config"))
    scheduler.register_task(
        "runtime",
        lambda: executed.append("runtime"),
        dependencies=["config"],
    )

    engine = RuntimeExecutionEngine(scheduler)
    result = engine.execute()

    assert executed == ["config", "runtime"]
    assert result.state == RuntimeExecutionState.COMPLETED


def test_runtime_execution_engine_returns_failed_result_on_error():
    scheduler = RuntimeScheduler()

    def failing_task():
        raise RuntimeError("boom")

    scheduler.register_task("broken", failing_task)

    engine = RuntimeExecutionEngine(scheduler)
    result = engine.execute()

    assert result.state == RuntimeExecutionState.FAILED
    assert isinstance(result.error, RuntimeError)
    assert engine.state == RuntimeExecutionState.FAILED
    assert engine.last_result == result


def test_runtime_execution_engine_reset_returns_to_idle():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("boot", lambda: executed.append("boot"))

    engine = RuntimeExecutionEngine(scheduler)
    engine.execute()
    engine.reset()

    assert engine.state == RuntimeExecutionState.IDLE
    assert engine.last_result is None
    assert scheduler.get_task("boot").status.value == "pending"