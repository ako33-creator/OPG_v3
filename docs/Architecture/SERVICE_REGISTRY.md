# Service Registry

Version: 3.0  
Status: Draft  
Ticket: M-003-003

---

## Purpose

The Service Registry is the central registry of runtime services in OPG.

It allows the Runtime to register, retrieve, validate, and manage services.

No service may be accessed directly without going through the Service Registry.

---

## Responsibilities

The Service Registry shall:

- register runtime services
- expose services by name
- prevent duplicate service registration
- validate service availability
- provide controlled access to services
- support runtime initialization order

---

## Design Rules

The Service Registry:

- does not create business logic
- does not own module logic
- does not depend on Blender
- does not import plugin-specific code
- belongs to the Core Architecture

---

## Service Lifecycle

1. Service declared
2. Service registered
3. Service validated
4. Service available
5. Service used by Runtime or modules
6. Service released during shutdown

---

## Required Core Services

The initial Service Registry shall support:

- Configuration Service
- Logging Service
- Plugin Manager
- Runtime Graph
- Event Bus
- Command Bus

---

## Access Rule

All services must be requested through the registry.

Direct global access is forbidden.

---

## Failure Rules

The Service Registry must fail when:

- a required service is missing
- a service is registered twice
- a service name is invalid
- a service is requested before registration

---

## Future Implementation

The future Python implementation will be located under:

```text
SRC/opg/core/services/