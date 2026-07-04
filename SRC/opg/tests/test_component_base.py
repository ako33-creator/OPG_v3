from opg.project_model.component import Component


def test_component_has_name():
    component = Component(name="Transform")

    assert component.name == "Transform"


def test_component_generates_uuid():
    component = Component(name="Transform")

    assert isinstance(component.uuid, str)
    assert len(component.uuid) > 0


def test_components_have_unique_uuid():
    component_a = Component(name="A")
    component_b = Component(name="B")

    assert component_a.uuid != component_b.uuid


def test_component_metadata_default():
    component = Component(name="Transform")

    assert component.metadata == {}


def test_component_has_metadata():
    component = Component(
        name="Transform",
        metadata={"enabled": True},
    )

    assert component.has_metadata


def test_component_has_valid_name():
    component = Component(name="Transform")

    assert component.has_name()


def test_component_without_name():
    component = Component(name="   ")

    assert not component.has_name()