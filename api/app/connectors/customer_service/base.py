from abc import abstractmethod
from typing import Any

from app.connectors.base import BaseConnector


class CustomerServiceConnector(BaseConnector):
    """Base class for customer service platform connectors."""

    @abstractmethod
    async def search_tickets(
        self, customer_email: str, order_id: str | None = None
    ) -> list[dict[str, Any]]:
        """Search for support tickets related to a customer or order."""
        ...

    @abstractmethod
    async def get_ticket(self, ticket_id: str) -> dict[str, Any]:
        """Fetch full ticket details including conversation history."""
        ...
