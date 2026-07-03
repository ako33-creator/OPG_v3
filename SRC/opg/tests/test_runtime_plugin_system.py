import pytest

from opg.runtime import RuntimePluginSystem


def test_runtime_plugin_register():
    plugins = RuntimePluginSystem()

    plugin = object()
    plugins.register("plugin", plugin)

    assert plugins.has("plugin")
    assert plugins.get("plugin") is plugin


def test_runtime_plugin_duplicate():
    plugins = RuntimePluginSystem()

    plugins.register("plugin", object())

    with pytest.raises(RuntimeError):
        plugins.register("plugin", object())


def test_runtime_plugin_get_unknown():
    plugins = RuntimePluginSystem()

    with pytest.raises(RuntimeError):
        plugins.get("missing")


def test_runtime_plugin_unregister():
    plugins = RuntimePluginSystem()

    plugins.register("plugin", object())
    plugins.unregister("plugin")

    assert plugins.has("plugin") is False


def test_runtime_plugin_unregister_unknown():
    plugins = RuntimePluginSystem()

    with pytest.raises(RuntimeError):
        plugins.unregister("missing")


def test_runtime_plugin_count():
    plugins = RuntimePluginSystem()

    plugins.register("a", object())
    plugins.register("b", object())

    assert plugins.count() == 2


def test_runtime_plugin_names():
    plugins = RuntimePluginSystem()

    plugins.register("a", object())
    plugins.register("b", object())

    assert set(plugins.names()) == {"a", "b"}


def test_runtime_plugin_clear():
    plugins = RuntimePluginSystem()

    plugins.register("a", object())
    plugins.register("b", object())

    plugins.clear()

    assert plugins.count() == 0
    assert plugins.names() == []