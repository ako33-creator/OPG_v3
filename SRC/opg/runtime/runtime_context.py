from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeContext:
    project_name: str
    version: str = "0.1.0"
    metadata: dict[str, Any] = field(default_factory=dict)
    services: dict[str, Any] = field(default_factory=dict)
    state: dict[str, Any] = field(default_factory=dict)

    def set_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    def get_metadata(self, key: str, default: Any = None) -> Any:
        return self.metadata.get(key, default)

    def register_service(self, name: str, service: Any) -> None:
        if name in self.services:
            raise RuntimeError(f"Service already registered: {name}")

        self.services[name] = service

    def get_service(self, name: str) -> Any:
        if name not in self.services:
            raise RuntimeError(f"Service not found: {name}")

        return self.services[name]

    def set_state(self, key: str, value: Any) -> None:
        self.state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)