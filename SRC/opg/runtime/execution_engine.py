from enum import Enum


class ExecutionState(Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    FAILED = "failed"


class RuntimeExecutionEngine:
    def __init__(self):
        self.state = ExecutionState.IDLE
        self.current_context = None

    def start(self, context):
        if self.state == ExecutionState.RUNNING:
            raise RuntimeError("Execution Engine is already running.")

        self.current_context = context
        self.state = ExecutionState.RUNNING
        return True

    def pause(self):
        if self.state != ExecutionState.RUNNING:
            raise RuntimeError("Execution Engine can only pause while running.")

        self.state = ExecutionState.PAUSED
        return True

    def resume(self):
        if self.state != ExecutionState.PAUSED:
            raise RuntimeError("Execution Engine can only resume from paused state.")

        self.state = ExecutionState.RUNNING
        return True

    def stop(self):
        if self.state in (ExecutionState.IDLE, ExecutionState.STOPPED):
            return True

        self.state = ExecutionState.STOPPED
        self.current_context = None
        return True

    def fail(self):
        self.state = ExecutionState.FAILED
        return True

    def is_running(self):
        return self.state == ExecutionState.RUNNING