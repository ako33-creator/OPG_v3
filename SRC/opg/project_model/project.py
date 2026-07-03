from dataclasses import dataclass, field

from .constants import (
    DEFAULT_PROJECT_VERSION,
    PROJECT_MODEL_SCHEMA_VERSION,
)


@dataclass(frozen=True)
class Project:
    """
    Root entity of the OPG Project Model.

    The Project is the persistent aggregate root.

    Runtime data must never be stored here.
    """

    name: str

    schema_version: int = PROJECT_MODEL_SCHEMA_VERSION

    project_version: str = DEFAULT_PROJECT_VERSION

    objects: list = field(default_factory=list)

    @property
    def object_count(self) -> int:
        return len(self.objects)

    def is_valid_skeleton(self) -> bool:
        return (
            bool(self.name.strip())
            and self.schema_version > 0
        )