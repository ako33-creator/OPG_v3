from opg.project_model.object import Object


def test_object_has_name():
    obj = Object(name="Cube")

    assert obj.name == "Cube"


def test_object_generates_uuid():
    obj = Object(name="Cube")

    assert isinstance(obj.uuid, str)
    assert len(obj.uuid) > 0


def test_objects_have_unique_uuid():
    a = Object(name="A")
    b = Object(name="B")

    assert a.uuid != b.uuid


def test_object_metadata_default():
    obj = Object(name="Cube")

    assert obj.metadata == {}


def test_object_has_metadata():
    obj = Object(
        name="Cube",
        metadata={"type": "mesh"},
    )

    assert obj.has_metadata


def test_object_has_name():
    obj = Object(name="Cube")

    assert obj.has_name()


def test_object_without_name():
    obj = Object(name="   ")

    assert not obj.has_name()