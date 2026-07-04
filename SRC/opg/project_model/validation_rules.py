"""
Project Validation Rules Expansion.

Defines reusable validation rules for Project Model integrity checks.
These rules are designed to be used by the validation engine.
"""

from __future__ import annotations

from typing import Any, Callable, List


class ValidationRule:
    """Represents a single validation rule."""

    def __init__(self, name: str, check: Callable[[Any], bool], message: str) -> None:
        self.name = name
        self.check = check
        self.message = message

    def validate(self, project: Any) -> bool:
        """Execute rule check."""
        return self.check(project)


class ValidationRuleSet:
    """Container for multiple validation rules."""

    def __init__(self) -> None:
        self._rules: List[ValidationRule] = []

    def add(self, rule: ValidationRule) -> None:
        """Add a validation rule."""
        self._rules.append(rule)

    def validate(self, project: Any) -> List[str]:
        """
        Run all rules and return list of error messages.
        """
        errors: List[str] = []

        for rule in self._rules:
            try:
                if not rule.validate(project):
                    errors.append(rule.message)
            except Exception as e:
                errors.append(f"{rule.name}: exception {str(e)}")

        return errors