"""
OPG Core Exceptions.

This module defines the official exception hierarchy for the OPG core layer.

Rules:
- No Blender dependency.
- No external dependency.
- All OPG-specific errors must inherit from OPGError.
"""


class OPGError(Exception):
    """
    Base exception for all OPG-specific errors.

    Every custom exception raised by OPG must inherit from this class.
    """

    pass


class OPGConfigurationError(OPGError):
    """
    Raised when the application configuration is invalid or unavailable.
    """

    pass


class OPGApplicationError(OPGError):
    """
    Raised when the core application enters an invalid state.
    """

    pass


class OPGServiceError(OPGError):
    """
    Raised when a service registration, lookup, or lifecycle operation fails.
    """

    pass


class OPGModuleError(OPGError):
    """
    Raised when a module declaration, registration, loading, or state transition fails.
    """

    pass


class OPGPluginError(OPGError):
    """
    Raised when plugin discovery, loading, validation, or execution fails.
    """

    pass


class OPGLifecycleError(OPGError):
    """
    Raised when an invalid lifecycle operation is requested.
    """

    pass