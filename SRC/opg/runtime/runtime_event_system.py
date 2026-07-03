from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass(frozen=True)
class RuntimeEvent:
    name: str
    payload: Dict[str, Any]


RuntimeEventHandler = Callable[[RuntimeEvent], None]


class RuntimeEventSystem:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[RuntimeEventHandler]] = {}

    def subscribe(self, event_name: str, handler: RuntimeEventHandler) -> None:
        if event_name not in self._handlers:
            self._handlers[event_name] = []

        self._handlers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: RuntimeEventHandler) -> None:
        if event_name not in self._handlers:
            return

        if handler in self._handlers[event_name]:
            self._handlers[event_name].remove(handler)

        if not self._handlers[event_name]:
            del self._handlers[event_name]

    def publish(self, event_name: str, payload: Dict[str, Any] | None = None) -> RuntimeEvent:
        event = RuntimeEvent(name=event_name, payload=payload or {})

        for handler in list(self._handlers.get(event_name, [])):
            handler(event)

        return event

    def has_subscribers(self, event_name: str) -> bool:
        return event_name in self._handlers and bool(self._handlers[event_name])

    def clear(self) -> None:
        self._handlers.clear()