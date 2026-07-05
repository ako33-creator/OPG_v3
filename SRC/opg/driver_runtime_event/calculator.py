"""Diff calculator for driver runtime events."""

from __future__ import annotations

from typing import Any

from .diff import RuntimeDiff


class RuntimeDiffCalculator:
    """Compute differences between runtime states."""

    def calculate(self, old: dict[str, Any], new: dict[str, Any]) -> list[RuntimeDiff]:
        """Return list of differences between two states."""
        diffs: list[RuntimeDiff] = []

        for key in old.keys() | new.keys():
            old_value = old.get(key)
            new_value = new.get(key)

            if old_value != new_value:
                diffs.append(
                    RuntimeDiff(
                        path=key,
                        old_value=old_value,
                        new_value=new_value,
                    )
                )

        return diffs