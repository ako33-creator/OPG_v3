from uuid import UUID, uuid4


class UUIDManager:
    """
    Central UUID management service for the OPG Project Model.

    Provides UUID generation and validation independently
    from any Runtime or Driver.
    """

    @staticmethod
    def generate() -> str:
        return str(uuid4())

    @staticmethod
    def is_valid(value: str) -> bool:
        if not isinstance(value, str):
            return False

        try:
            UUID(value)
        except (ValueError, AttributeError, TypeError):
            return False

        return True