class RuntimePluginSystem:
    def __init__(self):
        self._plugins: dict[str, object] = {}

    def register(self, name: str, plugin: object) -> None:
        if not name:
            raise ValueError("Plugin name cannot be empty.")

        if name in self._plugins:
            raise RuntimeError(f"Plugin already registered: {name}")

        self._plugins[name] = plugin

    def unregister(self, name: str) -> None:
        if name not in self._plugins:
            raise RuntimeError(f"Plugin not found: {name}")

        del self._plugins[name]

    def get(self, name: str):
        if name not in self._plugins:
            raise RuntimeError(f"Plugin not found: {name}")

        return self._plugins[name]

    def has(self, name: str) -> bool:
        return name in self._plugins

    def count(self) -> int:
        return len(self._plugins)

    def names(self) -> list[str]:
        return list(self._plugins.keys())

    def clear(self) -> None:
        self._plugins.clear()