class RuntimeDependencySystem:
    def __init__(self):
        self._dependencies: dict[str, set[str]] = {}

    def add_service(self, name: str) -> None:
        if not name:
            raise ValueError("Service name cannot be empty.")

        self._dependencies.setdefault(name, set())

    def add_dependency(self, service: str, depends_on: str) -> None:
        if not service:
            raise ValueError("Service name cannot be empty.")

        if not depends_on:
            raise ValueError("Dependency name cannot be empty.")

        self.add_service(service)
        self.add_service(depends_on)

        self._dependencies[service].add(depends_on)

    def get_dependencies(self, service: str) -> set[str]:
        if service not in self._dependencies:
            raise RuntimeError(f"Service not found: {service}")

        return set(self._dependencies[service])

    def has_service(self, service: str) -> bool:
        return service in self._dependencies

    def remove_service(self, service: str) -> None:
        if service not in self._dependencies:
            raise RuntimeError(f"Service not found: {service}")

        del self._dependencies[service]

        for dependencies in self._dependencies.values():
            dependencies.discard(service)

    def clear(self) -> None:
        self._dependencies.clear()

    def count(self) -> int:
        return len(self._dependencies)

    def names(self) -> list[str]:
        return list(self._dependencies.keys())