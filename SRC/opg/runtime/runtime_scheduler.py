from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional


class RuntimeTaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class RuntimeTask:
    name: str
    action: Callable[[], None]
    dependencies: List[str] = field(default_factory=list)
    status: RuntimeTaskStatus = RuntimeTaskStatus.PENDING


class RuntimeScheduler:
    def __init__(self) -> None:
        self._tasks: Dict[str, RuntimeTask] = {}

    def register_task(
        self,
        name: str,
        action: Callable[[], None],
        dependencies: Optional[List[str]] = None,
    ) -> None:
        if name in self._tasks:
            raise ValueError(f"Runtime task already registered: {name}")

        self._tasks[name] = RuntimeTask(
            name=name,
            action=action,
            dependencies=dependencies or [],
        )

    def has_task(self, name: str) -> bool:
        return name in self._tasks

    def get_task(self, name: str) -> RuntimeTask:
        if name not in self._tasks:
            raise KeyError(f"Runtime task not found: {name}")
        return self._tasks[name]

    def list_tasks(self) -> List[str]:
        return list(self._tasks.keys())

    def run_task(self, name: str) -> None:
        task = self.get_task(name)

        if task.status == RuntimeTaskStatus.COMPLETED:
            return

        for dependency_name in task.dependencies:
            dependency = self.get_task(dependency_name)
            if dependency.status != RuntimeTaskStatus.COMPLETED:
                self.run_task(dependency_name)

        task.status = RuntimeTaskStatus.RUNNING

        try:
            task.action()
        except Exception:
            task.status = RuntimeTaskStatus.FAILED
            raise

        task.status = RuntimeTaskStatus.COMPLETED

    def run_all(self) -> None:
        for task_name in self.list_tasks():
            self.run_task(task_name)

    def reset(self) -> None:
        for task in self._tasks.values():
            task.status = RuntimeTaskStatus.PENDING