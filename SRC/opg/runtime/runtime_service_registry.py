from typing import Any


class RuntimeServiceRegistry:
    def __init__(self):
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        if not name:
            raise ValueError("Service name cannot be empty.")

        if name in self._services:
            raise RuntimeError(f"Service already registered: {name}")

        self._services[name] = service

    def get(self, name: str) -> Any:
        if name not in self._services:
            raise RuntimeError(f"Service not found: {name}")

        return self._services[name]

    def has(self, name: str) -> bool:
        return name in self._services

    def unregister(self, name: str) -> None:
        if name not in self._services:
            raise RuntimeError(f"Service not found: {name}")

        del self._services[name]

    def clear(self) -> None:
        self._services.clear()

    def count(self) -> int:
        return len(self._services)

    def names(self) -> list[str]:
        return list(self._services.keys())