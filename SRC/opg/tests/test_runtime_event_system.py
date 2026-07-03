from opg.runtime.runtime_event_system import RuntimeEventSystem


def test_event_system_starts_without_subscribers():
    events = RuntimeEventSystem()

    assert events.has_subscribers("runtime.started") is False


def test_event_system_subscribes_handler():
    events = RuntimeEventSystem()

    def handler(event):
        pass

    events.subscribe("runtime.started", handler)

    assert events.has_subscribers("runtime.started") is True


def test_event_system_publishes_event_to_handler():
    events = RuntimeEventSystem()
    received = []

    def handler(event):
        received.append(event)

    events.subscribe("runtime.started", handler)

    event = events.publish("runtime.started", {"status": "ok"})

    assert len(received) == 1
    assert received[0].name == "runtime.started"
    assert received[0].payload == {"status": "ok"}
    assert event == received[0]


def test_event_system_publish_without_payload_uses_empty_payload():
    events = RuntimeEventSystem()
    received = []

    events.subscribe("runtime.started", lambda event: received.append(event))

    events.publish("runtime.started")

    assert received[0].payload == {}


def test_event_system_unsubscribes_handler():
    events = RuntimeEventSystem()
    received = []

    def handler(event):
        received.append(event)

    events.subscribe("runtime.started", handler)
    events.unsubscribe("runtime.started", handler)

    events.publish("runtime.started")

    assert received == []
    assert events.has_subscribers("runtime.started") is False


def test_event_system_clear_removes_all_handlers():
    events = RuntimeEventSystem()

    events.subscribe("runtime.started", lambda event: None)
    events.subscribe("runtime.stopped", lambda event: None)

    events.clear()

    assert events.has_subscribers("runtime.started") is False
    assert events.has_subscribers("runtime.stopped") is False