from .runtime_context import RuntimeContext
from .execution_engine import RuntimeExecutionEngine
from .runtime_manager import RuntimeManager


class RuntimeBuilder:
    def __init__(self):
        self.project_name = "OPG V3"
        self.version = "3.0.0"

    def with_project_name(self, project_name: str):
        self.project_name = project_name
        return self

    def with_version(self, version: str):
        self.version = version
        return self

    def build_context(self) -> RuntimeContext:
        return RuntimeContext(
            project_name=self.project_name,
            version=self.version,
        )

    def build_execution_engine(self) -> RuntimeExecutionEngine:
        return RuntimeExecutionEngine()

    def build_manager(self) -> RuntimeManager:
        context = self.build_context()
        manager = RuntimeManager()
        manager.initialize(context)
        return manager