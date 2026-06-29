"""OPG Core package."""

from .application import OPGApplication
from .config import OPGConfig
from .constants import APP_NAME, APP_SHORT_NAME, VERSION
from .exceptions import OPGException
from .logger import get_logger
from .service_registry import ServiceRegistry
from .module_manager import ModuleManager
from .plugin_loader import PluginLoader

__all__ = [
    "OPGApplication",
    "OPGConfig",
    "APP_NAME",
    "APP_SHORT_NAME",
    "VERSION",
    "OPGException",
    "get_logger",
    "ServiceRegistry",
    "ModuleManager",
    "PluginLoader",
]
