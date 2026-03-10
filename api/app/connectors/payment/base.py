from abc import abstractmethod
from typing import Any

from app.connectors.base import BaseConnector


class PaymentConnector(BaseConnector):
    """Base class for payment provider connectors."""

    @abstractmethod
    async def list_chargebacks(
        self, merchant_id: str, start_date: str, end_date: str
    ) -> list[dict[str, Any]]:
        """Fetch chargebacks from the payment provider."""
        ...

    @abstractmethod
    async def get_transaction(self, transaction_id: str) -> dict[str, Any]:
        """Get transaction details by ID."""
        ...

    @abstractmethod
    async def submit_dispute(
        self, chargeback_id: str, evidence: dict[str, Any]
    ) -> dict[str, Any]:
        """Submit a dispute for a chargeback."""
        ...

    @abstractmethod
    async def get_dispute_status(self, dispute_id: str) -> dict[str, Any]:
        """Check the current status of a dispute."""
        ...
