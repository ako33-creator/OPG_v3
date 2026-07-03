from opg.runtime import RuntimeBuilder, RuntimeManager, RuntimeContext


def test_runtime_builder_creates_context():
    builder = RuntimeBuilder()

    context = builder.build_context()

    assert isinstance(context, RuntimeContext)
    assert context.project_name == "OPG V3"
    assert context.version == "3.0.0"


def test_runtime_builder_custom_project_name():
    builder = RuntimeBuilder().with_project_name("Custom Project")

    context = builder.build_context()

    assert context.project_name == "Custom Project"


def test_runtime_builder_custom_version():
    builder = RuntimeBuilder().with_version("3.1.0")

    context = builder.build_context()

    assert context.version == "3.1.0"


def test_runtime_builder_creates_initialized_manager():
    builder = RuntimeBuilder()

    manager = builder.build_manager()

    assert isinstance(manager, RuntimeManager)
    assert manager.initialized is True