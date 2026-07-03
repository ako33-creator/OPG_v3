import pytest

from opg.runtime import RuntimeConfiguration


def test_runtime_configuration_set_get():
    config = RuntimeConfiguration()

    config.set("version", "3.0")

    assert config.get("version") == "3.0"


def test_runtime_configuration_default():
    config = RuntimeConfiguration()

    assert config.get("missing", 42) == 42


def test_runtime_configuration_has():
    config = RuntimeConfiguration()

    config.set("debug", True)

    assert config.has("debug")


def test_runtime_configuration_remove():
    config = RuntimeConfiguration()

    config.set("debug", True)
    config.remove("debug")

    assert not config.has("debug")


def test_runtime_configuration_rejects_missing_key():
    config = RuntimeConfiguration()

    with pytest.raises(RuntimeError):
        config.remove("missing")


def test_runtime_configuration_rejects_empty_key():
    config = RuntimeConfiguration()

    with pytest.raises(ValueError):
        config.set("", 123)


def test_runtime_configuration_clear():
    config = RuntimeConfiguration()

    config.set("a", 1)
    config.set("b", 2)

    config.clear()

    assert config.count() == 0
    assert config.keys() == []