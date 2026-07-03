import pytest

from opg.runtime import RuntimeServiceRegistry


def test_runtime_service_registry_registers_service():
    registry = RuntimeServiceRegistry()
    service = object()

    registry.register("test_service", service)

    assert registry.has("test_service") is True
    assert registry.get("test_service") is service
    assert registry.count() == 1


def test_runtime_service_registry_rejects_duplicate_service():
    registry = RuntimeServiceRegistry()
    service = object()

    registry.register("test_service", service)

    with pytest.raises(RuntimeError):
        registry.register("test_service", service)


def test_runtime_service_registry_rejects_empty_name():
    registry = RuntimeServiceRegistry()

    with pytest.raises(ValueError):
        registry.register("", object())


def test_runtime_service_registry_unregisters_service():
    registry = RuntimeServiceRegistry()
    service = object()

    registry.register("test_service", service)
    registry.unregister("test_service")

    assert registry.has("test_service") is False
    assert registry.count() == 0


def test_runtime_service_registry_clear_services():
    registry = RuntimeServiceRegistry()

    registry.register("a", object())
    registry.register("b", object())

    registry.clear()

    assert registry.count() == 0
    assert registry.names() == []