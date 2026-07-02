from .execution_engine import RuntimeExecutionEngine, ExecutionState


class RuntimeManager:
    def __init__(self):
        self.execution_engine = RuntimeExecutionEngine()
        self.runtime_context = None
        self.initialized = False

    def initialize(self, context):
        if self.initialized:
            raise RuntimeError("Runtime Manager is already initialized.")

        self.runtime_context = context
        self.initialized = True
        return True

    def start_runtime(self):
        self._ensure_initialized()
        return self.execution_engine.start(self.runtime_context)

    def pause_runtime(self):
        self._ensure_initialized()
        return self.execution_engine.pause()

    def resume_runtime(self):
        self._ensure_initialized()
        return self.execution_engine.resume()

    def stop_runtime(self):
        self._ensure_initialized()
        return self.execution_engine.stop()

    def shutdown(self):
        if self.execution_engine.state == ExecutionState.RUNNING:
            self.execution_engine.stop()

        self.runtime_context = None
        self.initialized = False
        return True

    def get_state(self):
        return self.execution_engine.state

    def _ensure_initialized(self):
        if not self.initialized:
            raise RuntimeError("Runtime Manager is not initialized.")