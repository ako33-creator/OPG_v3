"""Tests for runtime project binding contract."""

from opg.runtime.project_binding import RuntimeProjectBinding


class DummyProject:
    """Minimal project-like object used for binding tests."""


def test_runtime_project_binding_stores_project():
    project = DummyProject()

    binding = RuntimeProjectBinding(project=project)

    assert binding.project is project


def test_runtime_project_binding_returns_project():
    project = DummyProject()

    binding = RuntimeProjectBinding(project=project)

    assert binding.get_project() is project


def test_runtime_project_binding_is_immutable():
    project = DummyProject()
    other_project = DummyProject()

    binding = RuntimeProjectBinding(project=project)

    try:
        binding.project = other_project
    except Exception:
        pass

    assert binding.project is project