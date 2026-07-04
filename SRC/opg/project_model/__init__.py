"""Public API for the OPG Project Model package."""

from .asset_reference import AssetReference
from .collection import Collection
from .component import Component
from .constants import DEFAULT_PROJECT_VERSION, PROJECT_MODEL_SCHEMA_VERSION
from .errors import ProjectModelError
from .metadata import Metadata
from .object import Object
from .project import Project
from .scene import Scene
from .uuid_manager import UUIDManager
from .validation import ValidationError, ValidationResult

__all__ = [
    "AssetReference",
    "Collection",
    "Component",
    "DEFAULT_PROJECT_VERSION",
    "Metadata",
    "Object",
    "PROJECT_MODEL_SCHEMA_VERSION",
    "Project",
    "ProjectModelError",
    "Scene",
    "UUIDManager",
    "ValidationError",
    "ValidationResult",
]