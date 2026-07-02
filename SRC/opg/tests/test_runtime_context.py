from opg.runtime import RuntimeContext


def test_runtime_context_creation():
    context = RuntimeContext(project_name="OPG V3")

    assert context.project_name == "OPG V3"
    assert context.version == "0.1.0"
    assert context.metadata == {}
    assert context.services == {}
    assert context.state == {}


def test_runtime_context_metadata():
    context = RuntimeContext(project_name="OPG V3")

    context.set_metadata("author", "OXAHO")

    assert context.get_metadata("author") == "OXAHO"
    assert context.get_metadata("missing", "default") == "default"


def test_runtime_context_services():
    context = RuntimeContext(project_name="OPG V3")
    service = object()

    context.register_service("test_service", service)

    assert context.get_service("test_service") is service


def test_runtime_context_state():
    context = RuntimeContext(project_name="OPG V3")

    context.set_state("booted", True)

    assert context.get_state("booted") is True
    assert context.get_state("missing", False) is False