from dataclasses import dataclass, field


@dataclass(frozen=True)
class AssetReference:
    """
    Persistent reference to an external asset.

    The Project Model stores asset identity and location data
    without loading or owning the external asset itself.
    """

    asset_id: str

    uri: str

    metadata: dict = field(default_factory=dict)

    @property
    def has_metadata(self) -> bool:
        return bool(self.metadata)

    def has_asset_id(self) -> bool:
        return bool(self.asset_id.strip())

    def has_uri(self) -> bool:
        return bool(self.uri.strip())