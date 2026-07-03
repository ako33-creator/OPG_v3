import pytest

from opg.runtime import RuntimeGraph


def test_runtime_graph_add_node():
    graph = RuntimeGraph()

    graph.add_node("runtime")

    assert graph.has_node("runtime") is True
    assert graph.count() == 1


def test_runtime_graph_rejects_empty_node():
    graph = RuntimeGraph()

    with pytest.raises(ValueError):
        graph.add_node("")


def test_runtime_graph_add_edge():
    graph = RuntimeGraph()

    graph.add_edge("manager", "engine")

    assert graph.has_node("manager") is True
    assert graph.has_node("engine") is True
    assert graph.has_edge("manager", "engine") is True
    assert graph.neighbors("manager") == {"engine"}


def test_runtime_graph_remove_edge():
    graph = RuntimeGraph()

    graph.add_edge("manager", "engine")
    graph.remove_edge("manager", "engine")

    assert graph.has_edge("manager", "engine") is False


def test_runtime_graph_remove_node():
    graph = RuntimeGraph()

    graph.add_edge("manager", "engine")
    graph.remove_node("engine")

    assert graph.has_node("engine") is False
    assert graph.has_edge("manager", "engine") is False


def test_runtime_graph_neighbors_unknown_node():
    graph = RuntimeGraph()

    with pytest.raises(RuntimeError):
        graph.neighbors("missing")


def test_runtime_graph_clear():
    graph = RuntimeGraph()

    graph.add_edge("manager", "engine")
    graph.clear()

    assert graph.count() == 0
    assert graph.nodes() == []