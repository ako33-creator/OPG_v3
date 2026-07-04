"""Validation support for the OPG Project Model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationError:
    """Represents a Project Model validation error."""

    code: str
    message: str
    path: str = ""


class ValidationResult:
    """Stores the result of a Project Model validation operation."""

    def __init__(self) -> None:
        self._errors: list[ValidationError] = []

    @property
    def is_valid(self) -> bool:
        """Return whether validation completed without errors."""
        return not self._errors

    @property
    def errors(self) -> tuple[ValidationError, ...]:
        """Return validation errors as an immutable sequence."""
        return tuple(self._errors)

    def add_error(
        self,
        code: str,
        message: str,
        path: str = "",
    ) -> None:
        """Add a validation error."""
        self._errors.append(
            ValidationError(
                code=code,
                message=message,
                path=path,
            )
        )