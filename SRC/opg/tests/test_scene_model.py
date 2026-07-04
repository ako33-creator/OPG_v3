from opg.project_model.scene import Scene


def test_scene_has_name():
    scene = Scene(name="Main Scene")

    assert scene.name == "Main Scene"


def test_scene_generates_uuid():
    scene = Scene(name="Main Scene")

    assert isinstance(scene.uuid, str)
    assert len(scene.uuid) > 0


def test_scenes_have_unique_uuid():
    scene_a = Scene(name="Scene A")
    scene_b = Scene(name="Scene B")

    assert scene_a.uuid != scene_b.uuid


def test_scene_metadata_default():
    scene = Scene(name="Main Scene")

    assert scene.metadata == {}


def test_scene_has_metadata():
    scene = Scene(
        name="Main Scene",
        metadata={"environment": "studio"},
    )

    assert scene.has_metadata


def test_scene_has_valid_name():
    scene = Scene(name="Main Scene")

    assert scene.has_name()


def test_scene_without_name():
    scene = Scene(name="   ")

    assert not scene.has_name()