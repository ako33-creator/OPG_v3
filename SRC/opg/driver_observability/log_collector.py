"""Log collector for runtime observability system."""

from __future__ import annotations

from typing import Any

from .log_model import LogEntry


class LogCollector:
    """Collects structured logs from runtime system."""

    def __init__(self) -> None:
        self.logs: list[LogEntry] = []

    def collect(self, entry: LogEntry) -> None:
        """Store a log entry."""
        self.logs.append(entry)

    def query(self, level: str | None = None) -> list[dict[str, Any]]:
        """Return logs optionally filtered by level."""
        if level is None:
            return [log.to_dict() for log in self.logs]

        return [log.to_dict() for log in self.logs if log.level == level]