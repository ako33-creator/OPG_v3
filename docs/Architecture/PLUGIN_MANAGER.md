# Plugin Manager

Version: 3.0  
Status: Draft  
Ticket: M-003-004

---

## Purpose

The Plugin Manager is responsible for discovering, validating, loading, and managing OPG plugins.

Plugins extend OPG capabilities without modifying the core runtime.

The Plugin Manager is controlled by the Runtime and uses the Service Registry to access required services.

---

## Responsibilities

The Plugin Manager shall:

- discover available plugins
- validate plugin metadata
- verify plugin compatibility
- register plugin services
- initialize plugins in dependency order
- expose plugin status to the Runtime
- prevent invalid plugins from loading
- support clean plugin shutdown

---

## Design Rules

The Plugin Manager:

- does not contain business logic
- does not bypass the Runtime
- does not access Blender directly
- does not create services directly outside the Service Registry
- does not load unvalidated plugins

---

## Plugin Lifecycle

1. Plugin discovered
2. Plugin metadata loaded
3. Plugin compatibility checked
4. Plugin dependencies resolved
5. Plugin registered
6. Plugin initialized
7. Plugin active
8. Plugin shutdown

---

## Plugin Metadata

Each plugin shall declare:

- plugin id
- plugin name
- version
- author
- description
- required OPG version
- dependencies
- provided services
- entry point

---

## Failure Rules

The Plugin Manager must fail when:

- plugin metadata is missing
- plugin version is incompatible
- dependency resolution fails
- plugin id is duplicated
- plugin entry point is invalid
- plugin initialization fails

---

## Runtime Integration

The Runtime owns the Plugin Manager lifecycle.

The Plugin Manager depends on:

- Configuration Service
- Logging Service
- Service Registry
- Runtime Graph

---

## Future Implementation

The future Python implementation will be located under:

```text
SRC/opg/core/plugins/