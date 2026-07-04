"""Public API for the OPG Project Model package."""

from .asset_reference import AssetReference
from .cloning import ProjectCloner
from .collection import Collection
from .comparison import ProjectComparator, ProjectComparison
from .component import Component
from .constants import DEFAULT_PROJECT_VERSION, PROJECT_MODEL_SCHEMA_VERSION
from .deserialization import ProjectDeserializer
from .diff import ProjectDiff, ProjectDiffer
from .query import ProjectQuery, ProjectQueryEngine
from .snapshot import ProjectSnapshot, ProjectSnapshotter
from .event import ProjectEvent, ProjectEventBus
from .registry import ProjectRegistry
from .errors import ProjectModelError
from .metadata import Metadata
from .migration import ProjectMigration
from .object import Object
from .project import Project
from .scene import Scene
from .serialization import ProjectSerializer
from .uuid_manager import UUIDManager
from .validation import ValidationError, ValidationResult
from .versioning import ProjectVersion

__all__ = [
    "AssetReference",
    "Collection",
    "Component",
    "DEFAULT_PROJECT_VERSION",
    "Metadata",
    "Object",
    "PROJECT_MODEL_SCHEMA_VERSION",
    "Project",
    "ProjectCloner",
    "ProjectComparator",
    "ProjectComparison",
    "ProjectDeserializer",
    "ProjectDiff",
    "ProjectDiffer",
    "ProjectQuery",
    "ProjectQueryEngine",
    "ProjectSnapshot",
    "ProjectSnapshotter",
    "ProjectEvent",
    "ProjectEventBus",
    "ProjectRegistry",
    "ProjectMigration",
    "ProjectModelError",
    "ProjectSerializer",
    "ProjectVersion",
    "Scene",
    "UUIDManager",
    "ValidationError",
    "ValidationResult",
]