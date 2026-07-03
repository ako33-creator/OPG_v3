class RuntimeGraph:
    def __init__(self):
        self._nodes: set[str] = set()
        self._edges: dict[str, set[str]] = {}

    def add_node(self, name: str) -> None:
        if not name:
            raise ValueError("Node name cannot be empty.")

        self._nodes.add(name)
        self._edges.setdefault(name, set())

    def remove_node(self, name: str) -> None:
        if name not in self._nodes:
            raise RuntimeError(f"Node not found: {name}")

        self._nodes.remove(name)
        self._edges.pop(name, None)

        for neighbors in self._edges.values():
            neighbors.discard(name)

    def add_edge(self, source: str, target: str) -> None:
        if not source:
            raise ValueError("Source node cannot be empty.")
        if not target:
            raise ValueError("Target node cannot be empty.")

        self.add_node(source)
        self.add_node(target)
        self._edges[source].add(target)

    def remove_edge(self, source: str, target: str) -> None:
        if source not in self._nodes:
            raise RuntimeError(f"Source node not found: {source}")
        if target not in self._nodes:
            raise RuntimeError(f"Target node not found: {target}")

        self._edges[source].discard(target)

    def neighbors(self, name: str) -> set[str]:
        if name not in self._nodes:
            raise RuntimeError(f"Node not found: {name}")

        return set(self._edges[name])

    def has_node(self, name: str) -> bool:
        return name in self._nodes

    def has_edge(self, source: str, target: str) -> bool:
        return source in self._edges and target in self._edges[source]

    def count(self) -> int:
        return len(self._nodes)

    def nodes(self) -> list[str]:
        return list(self._nodes)

    def clear(self) -> None:
        self._nodes.clear()
        self._edges.clear()