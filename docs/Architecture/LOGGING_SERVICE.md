# Logging Service

Version: 3.0

Status: Draft

Ticket: M-003-006

---

## Purpose

The Logging Service is responsible for collecting, formatting, routing and storing all runtime logs produced by OPG.

Every runtime event must be traceable.

---

## Responsibilities

The Logging Service shall:

- record runtime events
- record warnings
- record errors
- record fatal failures
- provide debug logging
- support multiple output targets
- support structured logging
- support runtime diagnostics

---

## Design Rules

The Logging Service:

- contains no business logic
- does not depend on Blender
- does not manage plugins
- does not create services
- does not modify runtime state
- is registered inside the Service Registry

---

## Log Levels

Supported log levels:

- Trace
- Debug
- Info
- Warning
- Error
- Fatal

---

## Log Categories

OPG shall support categories:

- Runtime
- Services
- Plugins
- Configuration
- Assets
- Catalog
- Export
- UI

---

## Log Destinations

Supported destinations:

- Console
- File
- Debug Window
- Future Remote Logger

---

## Failure Rules

The Logging Service must never crash the Runtime.

Logging failures shall be isolated.

---

## Runtime Integration

Initialization order:

1. Configuration Service

2. Logging Service

3. Service Registry

4. Plugin Manager

5. Runtime Graph

---

## Future Implementation

Future Python implementation:

```text
SRC/opg/core/logging/
```

Expected files:

```text
logging_service.py
logger.py
log_levels.py
log_targets.py
log_formatter.py
```

---

## Related Documents

- Runtime Architecture

- Configuration Service

- Service Registry

- Plugin Manager

- Runtime Graph