from abc import abstractmethod
from typing import Any

from app.connectors.base import BaseConnector


class EcommerceConnector(BaseConnector):
    """Base class for e-commerce platform connectors."""

    @abstractmethod
    async def get_order(self, order_id: str) -> dict[str, Any]:
        """Fetch order details including products, shipping, and customer info."""
        ...

    @abstractmethod
    async def get_customer(self, customer_id: str) -> dict[str, Any]:
        """Fetch customer details and purchase history."""
        ...

    @abstractmethod
    async def get_shipping_info(self, order_id: str) -> dict[str, Any]:
        """Fetch shipping/delivery information for an order."""
        ...
