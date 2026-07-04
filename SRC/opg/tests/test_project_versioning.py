"""Tests for the OPG Project Model versioning support."""

from opg.project_model import ProjectVersion


def test_project_version_stores_version_components():
    version = ProjectVersion(1, 2, 3)

    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3


def test_project_version_converts_to_tuple():
    version = ProjectVersion(1, 2, 3)

    assert version.to_tuple() == (1, 2, 3)


def test_project_version_converts_to_string():
    version = ProjectVersion(1, 2, 3)

    assert str(version) == "1.2.3"


def test_project_versions_can_be_equal():
    version_a = ProjectVersion(1, 2, 3)
    version_b = ProjectVersion(1, 2, 3)

    assert version_a == version_b


def test_project_versions_can_be_different():
    version_a = ProjectVersion(1, 2, 3)
    version_b = ProjectVersion(1, 2, 4)

    assert version_a != version_b


def test_project_versions_can_be_ordered():
    older = ProjectVersion(1, 2, 3)
    newer = ProjectVersion(1, 3, 0)

    assert older < newer