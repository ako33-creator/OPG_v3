from opg.runtime.runtime_logging_system import (
    RuntimeLoggingSystem,
    RuntimeLogLevel,
)


def test_logging_system_starts_empty():
    logs = RuntimeLoggingSystem()

    assert logs.records() == []


def test_logging_system_records_debug_log():
    logs = RuntimeLoggingSystem()

    record = logs.debug("debug message")

    assert record.level == RuntimeLogLevel.DEBUG
    assert record.message == "debug message"
    assert logs.records() == [record]


def test_logging_system_records_info_log():
    logs = RuntimeLoggingSystem()

    record = logs.info("info message")

    assert record.level == RuntimeLogLevel.INFO
    assert record.message == "info message"


def test_logging_system_records_warning_log():
    logs = RuntimeLoggingSystem()

    record = logs.warning("warning message")

    assert record.level == RuntimeLogLevel.WARNING
    assert record.message == "warning message"


def test_logging_system_records_error_log():
    logs = RuntimeLoggingSystem()

    record = logs.error("error message")

    assert record.level == RuntimeLogLevel.ERROR
    assert record.message == "error message"


def test_logging_system_returns_copy_of_records():
    logs = RuntimeLoggingSystem()

    logs.info("hello")

    records = logs.records()
    records.clear()

    assert len(logs.records()) == 1


def test_logging_system_clear_removes_records():
    logs = RuntimeLoggingSystem()

    logs.info("hello")
    logs.error("boom")

    logs.clear()

    assert logs.records() == []