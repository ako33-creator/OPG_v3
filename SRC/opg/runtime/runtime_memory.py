from typing import Any


class RuntimeMemory:
    def __init__(self):
        self._memory: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        if not key:
            raise ValueError("Memory key cannot be empty.")

        self._memory[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._memory.get(key, default)

    def has(self, key: str) -> bool:
        return key in self._memory

    def remove(self, key: str) -> None:
        if key not in self._memory:
            raise RuntimeError(f"Memory key not found: {key}")

        del self._memory[key]

    def clear(self) -> None:
        self._memory.clear()

    def count(self) -> int:
        return len(self._memory)

    def keys(self) -> list[str]:
        return list(self._memory.keys())