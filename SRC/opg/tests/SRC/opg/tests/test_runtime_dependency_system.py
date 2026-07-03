import pytest

from opg.runtime import RuntimeDependencySystem


def test_runtime_dependency_system_adds_service():
    system = RuntimeDependencySystem()

    system.add_service("service_a")

    assert system.has_service("service_a") is True
    assert system.count() == 1


def test_runtime_dependency_system_adds_dependency():
    system = RuntimeDependencySystem()

    system.add_dependency("service_a", "service_b")

    assert system.has_service("service_a") is True
    assert system.has_service("service_b") is True
    assert system.get_dependencies("service_a") == {"service_b"}


def test_runtime_dependency_system_rejects_empty_service_name():
    system = RuntimeDependencySystem()

    with pytest.raises(ValueError):
        system.add_service("")


def test_runtime_dependency_system_rejects_empty_dependency_name():
    system = RuntimeDependencySystem()

    with pytest.raises(ValueError):
        system.add_dependency("service_a", "")


def test_runtime_dependency_system_removes_service_and_relations():
    system = RuntimeDependencySystem()

    system.add_dependency("service_a", "service_b")
    system.remove_service("service_b")

    assert system.has_service("service_b") is False
    assert system.get_dependencies("service_a") == set()


def test_runtime_dependency_system_clears_all_services():
    system = RuntimeDependencySystem()

    system.add_dependency("service_a", "service_b")
    system.clear()

    assert system.count() == 0
    assert system.names() == []