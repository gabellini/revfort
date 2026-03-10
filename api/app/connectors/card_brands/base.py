from abc import abstractmethod
from typing import Any

from app.connectors.base import BaseConnector


class CardBrandConnector(BaseConnector):
    """Base class for direct card brand API connectors (Visa, Mastercard)."""

    @abstractmethod
    async def get_chargeback_alerts(
        self, merchant_id: str, start_date: str, end_date: str
    ) -> list[dict[str, Any]]:
        """Fetch chargeback alerts directly from the card brand."""
        ...

    @abstractmethod
    async def submit_dispute_response(
        self, case_id: str, evidence: dict[str, Any]
    ) -> dict[str, Any]:
        """Submit dispute response directly to the card brand."""
        ...

    @abstractmethod
    async def get_case_status(self, case_id: str) -> dict[str, Any]:
        """Check case status directly with the card brand."""
        ...
