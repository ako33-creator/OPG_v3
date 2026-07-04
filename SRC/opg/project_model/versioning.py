"""Versioning support for the OPG Project Model."""

from __future__ import annotations


class ProjectVersion:
    """Represents and compares Project Model versions."""

    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def to_tuple(self) -> tuple[int, int, int]:
        """Return the version as a tuple."""
        return self.major, self.minor, self.patch

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProjectVersion):
            return NotImplemented
        return self.to_tuple() == other.to_tuple()

    def __lt__(self, other: ProjectVersion) -> bool:
        return self.to_tuple() < other.to_tuple()

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"