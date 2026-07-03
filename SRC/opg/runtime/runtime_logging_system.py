from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class RuntimeLogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


@dataclass(frozen=True)
class RuntimeLogRecord:
    level: RuntimeLogLevel
    message: str


class RuntimeLoggingSystem:
    def __init__(self) -> None:
        self._records: List[RuntimeLogRecord] = []

    def log(self, level: RuntimeLogLevel, message: str) -> RuntimeLogRecord:
        record = RuntimeLogRecord(level=level, message=message)
        self._records.append(record)
        return record

    def debug(self, message: str) -> RuntimeLogRecord:
        return self.log(RuntimeLogLevel.DEBUG, message)

    def info(self, message: str) -> RuntimeLogRecord:
        return self.log(RuntimeLogLevel.INFO, message)

    def warning(self, message: str) -> RuntimeLogRecord:
        return self.log(RuntimeLogLevel.WARNING, message)

    def error(self, message: str) -> RuntimeLogRecord:
        return self.log(RuntimeLogLevel.ERROR, message)

    def records(self) -> List[RuntimeLogRecord]:
        return list(self._records)

    def clear(self) -> None:
        self._records.clear()