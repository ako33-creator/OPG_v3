class RuntimeConfiguration:
    def __init__(self):
        self._values: dict[str, object] = {}

    def set(self, key: str, value: object) -> None:
        if not key:
            raise ValueError("Configuration key cannot be empty.")

        self._values[key] = value

    def get(self, key: str, default: object = None) -> object:
        return self._values.get(key, default)

    def has(self, key: str) -> bool:
        return key in self._values

    def remove(self, key: str) -> None:
        if key not in self._values:
            raise RuntimeError(f"Configuration key not found: {key}")

        del self._values[key]

    def clear(self) -> None:
        self._values.clear()

    def count(self) -> int:
        return len(self._values)

    def keys(self) -> list[str]:
        return list(self._values.keys())