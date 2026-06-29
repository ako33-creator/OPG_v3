"""
OPG Core Plugin Loader.

Generic Python plugin loader for OPG.

Rules:
- No Blender dependency.
- No external dependency.
- No plugin must be loaded twice silently.
"""

import importlib
from types import ModuleType
from typing import Dict, Iterator

from .exceptions import OPGPluginError


class PluginRecord:
    """
    Internal record describing a loaded plugin.
    """

    def __init__(self, name: str, module: ModuleType) -> None:
        if not isinstance(name, str) or not name.strip():
            raise OPGPluginError("Plugin name must be a non-empty string.")

        if not isinstance(module, ModuleType):
            raise OPGPluginError("Plugin module must be a Python module.")

        self.name = name
        self.module = module
        self.loaded = True


class PluginLoader:
    """
    Loads and tracks Python plugins by import path.
    """

    def __init__(self) -> None:
        self._plugins: Dict[str, PluginRecord] = {}

    def load(self, import_path: str, *, alias: str | None = None, reload: bool = False) -> ModuleType:
        """
        Load a plugin module.

        Args:
            import_path: Python import path, for example "opg.catalog".
            alias: Optional registry name. Defaults to import_path.
            reload: Reload the module if already loaded.

        Returns:
            Imported Python module.

        Raises:
            OPGPluginError: If import path is invalid or loading fails.
        """
        self._validate_name(import_path)

        name = alias or import_path
        self._validate_name(name)

        if name in self._plugins and not reload:
            raise OPGPluginError(f"Plugin already loaded: {name}")

        try:
            if name in self._plugins and reload:
                module = importlib.reload(self._plugins[name].module)
            else:
                module = importlib.import_module(import_path)
        except Exception as exc:
            raise OPGPluginError(f"Failed to load plugin: {import_path}") from exc

        record = PluginRecord(name, module)
        self._plugins[name] = record
        return module

    def get(self, name: str) -> ModuleType:
        """
        Return a loaded plugin module.
        """
        return self.get_record(name).module

    def get_record(self, name: str) -> PluginRecord:
        """
        Return the plugin record.
        """
        self._validate_name(name)

        if name not in self._plugins:
            raise OPGPluginError(f"Plugin not loaded: {name}")

        return self._plugins[name]

    def has(self, name: str) -> bool:
        """
        Check whether a plugin is loaded.
        """
        self._validate_name(name)
        return name in self._plugins

    def unload(self, name: str) -> None:
        """
        Logically unload a plugin from the loader registry.

        This does not remove the Python module from sys.modules.
        """
        self._validate_name(name)

        if name not in self._plugins:
            raise OPGPluginError(f"Cannot unload missing plugin: {name}")

        self._plugins[name].loaded = False
        del self._plugins[name]

    def clear(self) -> None:
        """
        Clear all loaded plugin records.
        """
        self._plugins.clear()

    def names(self) -> Iterator[str]:
        """
        Iterate over loaded plugin names.
        """
        return iter(self._plugins.keys())

    def plugins(self) -> Iterator[ModuleType]:
        """
        Iterate over loaded plugin modules.
        """
        for record in self._plugins.values():
            yield record.module

    def records(self) -> Iterator[PluginRecord]:
        """
        Iterate over plugin records.
        """
        return iter(self._plugins.values())

    def items(self) -> Iterator[tuple[str, ModuleType]]:
        """
        Iterate over plugin name / module pairs.
        """
        for name, record in self._plugins.items():
            yield name, record.module

    def count(self) -> int:
        """
        Return the number of loaded plugins.
        """
        return len(self._plugins)

    def _validate_name(self, name: str) -> None:
        """
        Validate a plugin name or import path.
        """
        if not isinstance(name, str):
            raise OPGPluginError("Plugin name must be a string.")

        if not name.strip():
            raise OPGPluginError("Plugin name cannot be empty.")