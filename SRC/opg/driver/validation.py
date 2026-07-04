"""Driver validation layer for OPG external runtime drivers."""

from __future__ import annotations

from .interface import DriverInterface


class DriverValidator:
    """Validates technology-agnostic OPG driver instances."""

    def validate(self, driver: DriverInterface) -> bool:
        """Return whether a driver satisfies the minimal runtime contract."""
        return bool(driver.name) and bool(driver.version) and driver.is_available()