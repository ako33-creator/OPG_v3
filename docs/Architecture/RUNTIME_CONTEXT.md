# Runtime Context

## Purpose

## Responsibilities
The Runtime Context is responsible for:

- Holding the runtime-scoped state.
- Providing access to runtime services.
- Coordinating runtime execution.
- Managing temporary runtime resources.
- Exposing execution metadata.
- Providing a shared context for systems operating during a runtime session.

The Runtime Context never contains persistent business data.
Persistent information belongs to the Project Model.

## Architecture
The Runtime Context is a central runtime object shared across the execution environment.

It acts as the composition root for runtime-only resources and provides controlled access to services required during execution.

Typical content includes:

- Service Registry
- Runtime Graph
- Runtime Configuration
- Runtime Metadata
- Runtime Cache
- Execution State
- Event Dispatcher

The Runtime Context is created during runtime initialization and destroyed when the runtime terminates.

## Lifecycle
The Runtime Context follows the lifecycle of the runtime.

Initialization:

- Runtime starts.
- Runtime Context is created.
- Services are registered.
- Runtime Graph is built.
- Systems receive the Runtime Context.

Execution:

- Systems use the Runtime Context during execution.
- Runtime resources remain available until shutdown.

Shutdown:

- Systems are stopped.
- Runtime resources are released.
- Runtime Context is destroyed.

## Runtime Scope
The Runtime Context defines the execution scope shared by all runtime systems.

Objects stored inside the Runtime Context exist only during the current runtime session.

Examples include:

- Runtime services
- Temporary caches
- Active commands
- Execution metadata
- Runtime graph
- Synchronization objects

No object stored inside the Runtime Context survives application shutdown.

## Context Ownership
The Runtime Context is owned by the Runtime.

No individual system owns the Runtime Context.

Systems receive a reference to the Runtime Context during initialization and use it without modifying its ownership.

Creation and destruction of the Runtime Context are exclusively managed by the Runtime bootstrap process.

## Context Services
The Runtime Context provides controlled access to runtime services.

Services are not created by the Runtime Context itself.
They are resolved through the Service Registry and exposed to runtime systems when required.

Typical services include:

- Configuration Service
- Logging Service
- Plugin Manager
- Event Dispatcher
- Runtime Graph

The Runtime Context serves as the common access point for these services during runtime execution.

## Context Isolation
The Runtime Context is isolated from persistent application data.

It must never contain domain models intended for long-term storage.

All data stored inside the Runtime Context is considered temporary and disposable.

This isolation guarantees that runtime execution remains independent from project persistence mechanisms.

## Thread Safety
The Runtime Context is designed to support concurrent runtime execution.

It does not guarantee thread safety by itself.

Thread synchronization is the responsibility of the services and systems manipulating shared resources.

The Runtime Context provides a common execution environment while allowing internal implementations to adopt the synchronization strategy best suited to their responsibilities.

## Relationship with Runtime Graph
The Runtime Context and the Runtime Graph have complementary responsibilities.

The Runtime Context stores runtime-wide execution resources, while the Runtime Graph represents dependencies between runtime objects.

The Runtime Graph may be accessed through the Runtime Context, but it remains an independent architectural component.

This separation preserves a clear distinction between runtime state management and dependency modeling.

## Relationship with Service Registry
The Runtime Context does not manage service lifecycles.

Its responsibility is to provide access to the Service Registry, which owns the registration and resolution of runtime services.

This separation ensures that service management remains independent from the execution context while allowing runtime systems to retrieve the services they require.

The Runtime Context therefore acts as the gateway to the Service Registry without becoming a service container itself.

## Best Practices
- Keep the Runtime Context lightweight.
- Store only runtime-scoped objects.
- Never place persistent business data inside the Runtime Context.
- Expose services through well-defined interfaces.
- Avoid unnecessary coupling between runtime systems.
- Keep ownership rules explicit.
- Destroy the Runtime Context completely when the runtime terminates.

## Future Extensions
The Runtime Context is designed to evolve without breaking existing runtime systems.

Future versions may introduce:

- Multiple runtime contexts.
- Nested runtime contexts.
- Context inheritance.
- Runtime session management.
- Distributed runtime execution.
- Context diagnostics and profiling.
- Runtime sandboxing.

These extensions must preserve backward compatibility and maintain the separation between runtime execution and persistent application data.