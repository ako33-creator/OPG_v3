"""Blender availability detection for OPG."""

from __future__ import annotations

import importlib.util


def is_blender_available() -> bool:
    """Return whether the Blender Python API module is available."""
    return importlib.util.find_spec("bpy") is not None