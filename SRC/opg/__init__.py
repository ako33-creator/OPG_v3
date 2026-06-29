"""OXAHO Product Generator v3 package bootstrap."""

from .version import VERSION

bl_info = {
    "name": "OXAHO Product Generator",
    "author": "OXAHO",
    "version": (3, 0, 0),
    "blender": (5, 1, 0),
    "location": "View3D > Sidebar > OXAHO",
    "description": "Industrial product generation platform for OXAHO products.",
    "category": "3D View",
}


def register():
    # Blender integration is intentionally deferred after Core Bootstrap.
    print("OPG v3 Core Bootstrap registered")


def unregister():
    print("OPG v3 Core Bootstrap unregistered")
