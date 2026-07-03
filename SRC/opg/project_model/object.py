from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Object:
    """
    Base Project Model object.

    Every persistent Project object derives from this type.
    """

    name: str

    uuid: str = field(default_factory=lambda: str(uuid4()))

    metadata: dict = field(default_factory=dict)

    @property
    def has_metadata(self) -> bool:
        return bool(self.metadata)

    def has_name(self) -> bool:
        return bool(self.name.strip())