import pytest

from opg.runtime.runtime_scheduler import RuntimeScheduler, RuntimeTaskStatus


def test_runtime_scheduler_registers_task():
    scheduler = RuntimeScheduler()

    scheduler.register_task("boot", lambda: None)

    assert scheduler.has_task("boot") is True
    assert scheduler.get_task("boot").status == RuntimeTaskStatus.PENDING


def test_runtime_scheduler_rejects_duplicate_task():
    scheduler = RuntimeScheduler()

    scheduler.register_task("boot", lambda: None)

    with pytest.raises(ValueError):
        scheduler.register_task("boot", lambda: None)


def test_runtime_scheduler_runs_task():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("boot", lambda: executed.append("boot"))
    scheduler.run_task("boot")

    assert executed == ["boot"]
    assert scheduler.get_task("boot").status == RuntimeTaskStatus.COMPLETED


def test_runtime_scheduler_runs_dependencies_first():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("config", lambda: executed.append("config"))
    scheduler.register_task(
        "runtime",
        lambda: executed.append("runtime"),
        dependencies=["config"],
    )

    scheduler.run_task("runtime")

    assert executed == ["config", "runtime"]
    assert scheduler.get_task("config").status == RuntimeTaskStatus.COMPLETED
    assert scheduler.get_task("runtime").status == RuntimeTaskStatus.COMPLETED


def test_runtime_scheduler_run_all_runs_every_task():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("a", lambda: executed.append("a"))
    scheduler.register_task("b", lambda: executed.append("b"))

    scheduler.run_all()

    assert executed == ["a", "b"]


def test_runtime_scheduler_does_not_rerun_completed_task():
    scheduler = RuntimeScheduler()
    executed = []

    scheduler.register_task("boot", lambda: executed.append("boot"))

    scheduler.run_task("boot")
    scheduler.run_task("boot")

    assert executed == ["boot"]


def test_runtime_scheduler_marks_failed_task():
    scheduler = RuntimeScheduler()

    def failing_task():
        raise RuntimeError("boom")

    scheduler.register_task("broken", failing_task)

    with pytest.raises(RuntimeError):
        scheduler.run_task("broken")

    assert scheduler.get_task("broken").status == RuntimeTaskStatus.FAILED


def test_runtime_scheduler_reset_sets_tasks_to_pending():
    scheduler = RuntimeScheduler()

    scheduler.register_task("boot", lambda: None)
    scheduler.run_task("boot")

    scheduler.reset()

    assert scheduler.get_task("boot").status == RuntimeTaskStatus.PENDING