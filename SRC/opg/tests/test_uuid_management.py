from opg.project_model.uuid_manager import UUIDManager


def test_uuid_manager_generates_string():
    value = UUIDManager.generate()

    assert isinstance(value, str)


def test_uuid_manager_generates_valid_uuid():
    value = UUIDManager.generate()

    assert UUIDManager.is_valid(value)


def test_uuid_manager_generates_unique_values():
    value_a = UUIDManager.generate()
    value_b = UUIDManager.generate()

    assert value_a != value_b


def test_uuid_manager_accepts_valid_uuid():
    value = "123e4567-e89b-12d3-a456-426614174000"

    assert UUIDManager.is_valid(value)


def test_uuid_manager_rejects_invalid_uuid():
    assert not UUIDManager.is_valid("invalid-uuid")


def test_uuid_manager_rejects_empty_string():
    assert not UUIDManager.is_valid("")


def test_uuid_manager_rejects_non_string():
    assert not UUIDManager.is_valid(None)