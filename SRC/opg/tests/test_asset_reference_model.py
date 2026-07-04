from opg.project_model.asset_reference import AssetReference


def test_asset_reference_has_asset_id():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
    )

    assert asset.asset_id == "asset-001"


def test_asset_reference_has_uri():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
    )

    assert asset.uri == "assets/models/character.glb"


def test_asset_reference_metadata_default():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
    )

    assert asset.metadata == {}


def test_asset_reference_has_metadata():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
        metadata={"type": "model"},
    )

    assert asset.has_metadata


def test_asset_reference_has_valid_asset_id():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
    )

    assert asset.has_asset_id()


def test_asset_reference_without_asset_id():
    asset = AssetReference(
        asset_id="   ",
        uri="assets/models/character.glb",
    )

    assert not asset.has_asset_id()


def test_asset_reference_has_valid_uri():
    asset = AssetReference(
        asset_id="asset-001",
        uri="assets/models/character.glb",
    )

    assert asset.has_uri()


def test_asset_reference_without_uri():
    asset = AssetReference(
        asset_id="asset-001",
        uri="   ",
    )

    assert not asset.has_uri()