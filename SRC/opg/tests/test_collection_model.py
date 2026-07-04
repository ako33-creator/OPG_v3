from opg.project_model.collection import Collection


def test_collection_has_name():
    collection = Collection(name="Main Collection")

    assert collection.name == "Main Collection"


def test_collection_generates_uuid():
    collection = Collection(name="Main Collection")

    assert isinstance(collection.uuid, str)
    assert len(collection.uuid) > 0


def test_collections_have_unique_uuid():
    collection_a = Collection(name="Collection A")
    collection_b = Collection(name="Collection B")

    assert collection_a.uuid != collection_b.uuid


def test_collection_metadata_default():
    collection = Collection(name="Main Collection")

    assert collection.metadata == {}


def test_collection_has_metadata():
    collection = Collection(
        name="Main Collection",
        metadata={"category": "environment"},
    )

    assert collection.has_metadata


def test_collection_has_valid_name():
    collection = Collection(name="Main Collection")

    assert collection.has_name()


def test_collection_without_name():
    collection = Collection(name="   ")

    assert not collection.has_name()