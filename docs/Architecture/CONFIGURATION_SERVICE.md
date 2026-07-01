# Configuration Service

Version: 3.0  
Status: Draft  
Ticket: M-003-005

---

## Purpose

The Configuration Service is responsible for loading, validating, and exposing OPG configuration data.

Configuration must be centralized, validated, and accessible only through the Configuration Service.

No component may read configuration files directly.

---

## Responsibilities

The Configuration Service shall:

- load configuration files
- validate configuration structure
- expose configuration values
- provide default values
- reject invalid configuration
- support environment-specific configuration
- support runtime configuration access
- report configuration errors clearly

---

## Design Rules

The Configuration Service:

- does not contain business logic
- does not access Blender directly
- does not create services
- does not manage plugins
- does not bypass the Runtime
- is registered in the Service Registry

---

## Configuration Lifecycle

1. Configuration source discovered
2. Configuration file loaded
3. Configuration structure validated
4. Default values applied
5. Configuration registered as service
6. Runtime consumes configuration
7. Modules request configuration through the service

---

## Configuration Sources

The initial Configuration Service shall support:

- project configuration
- user configuration
- runtime configuration
- plugin configuration

---

## Required Configuration Domains

OPG shall define configuration domains for:

- runtime
- logging
- plugins
- assets
- catalog
- export
- UI

---

## Access Rule

All configuration access must go through the Configuration Service.

Direct file access is forbidden outside the Configuration Service.

---

## Failure Rules

The Configuration Service must fail when:

- configuration file is missing
- configuration syntax is invalid
- required keys are missing
- configuration value type is invalid
- environment configuration conflicts with project configuration

---

## Runtime Integration

The Runtime owns the Configuration Service lifecycle.

The Configuration Service is initialized before:

- Logging Service
- Service Registry
- Plugin Manager
- Runtime Graph
- Modules

---

## Future Implementation

The future Python implementation will be located under:

```text
SRC/opg/core/configuration/