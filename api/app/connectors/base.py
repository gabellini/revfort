from abc import ABC, abstractmethod
from typing import Any


class BaseConnector(ABC):
    """Base class for all external service connectors."""

    @abstractmethod
    async def authenticate(self) -> None:
        """Establish authentication with the external service."""
        ...

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the connector can reach the external service."""
        ...
