"""Tests for the OPG Project Model Metadata model."""

from opg.project_model import Metadata


def test_metadata_starts_empty():
    metadata = Metadata()

    assert metadata.to_dict() == {}


def test_metadata_can_set_and_get_value():
    metadata = Metadata()

    metadata.set("author", "OXAHO")

    assert metadata.get("author") == "OXAHO"


def test_metadata_get_returns_default_for_missing_key():
    metadata = Metadata()

    assert metadata.get("missing", "default") == "default"


def test_metadata_can_remove_value():
    metadata = Metadata()
    metadata.set("author", "OXAHO")

    metadata.remove("author")

    assert metadata.has("author") is False


def test_metadata_remove_missing_key_does_not_raise():
    metadata = Metadata()

    metadata.remove("missing")


def test_metadata_can_check_key_existence():
    metadata = Metadata()
    metadata.set("version", 1)

    assert metadata.has("version") is True
    assert metadata.has("missing") is False


def test_metadata_can_clear_all_values():
    metadata = Metadata()
    metadata.set("author", "OXAHO")
    metadata.set("version", 1)

    metadata.clear()

    assert metadata.to_dict() == {}


def test_metadata_to_dict_returns_copy():
    metadata = Metadata()
    metadata.set("author", "OXAHO")

    values = metadata.to_dict()
    values["author"] = "Modified"

    assert metadata.get("author") == "OXAHO"