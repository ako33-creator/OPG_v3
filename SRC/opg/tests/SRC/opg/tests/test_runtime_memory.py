import pytest

from opg.runtime import RuntimeMemory


def test_runtime_memory_set_get():
    memory = RuntimeMemory()

    memory.set("current_scene", "Scene_A")

    assert memory.get("current_scene") == "Scene_A"


def test_runtime_memory_default_value():
    memory = RuntimeMemory()

    assert memory.get("missing", "default") == "default"


def test_runtime_memory_has_key():
    memory = RuntimeMemory()

    memory.set("booted", True)

    assert memory.has("booted") is True


def test_runtime_memory_remove_key():
    memory = RuntimeMemory()

    memory.set("temp", 123)
    memory.remove("temp")

    assert memory.has("temp") is False


def test_runtime_memory_rejects_missing_remove():
    memory = RuntimeMemory()

    with pytest.raises(RuntimeError):
        memory.remove("missing")


def test_runtime_memory_rejects_empty_key():
    memory = RuntimeMemory()

    with pytest.raises(ValueError):
        memory.set("", "value")


def test_runtime_memory_clear():
    memory = RuntimeMemory()

    memory.set("a", 1)
    memory.set("b", 2)

    memory.clear()

    assert memory.count() == 0
    assert memory.keys() == []