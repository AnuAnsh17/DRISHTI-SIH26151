"""
Collector interface for DRISHTI OSINT collection framework.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from src.drishti.collection.models import RawObservation, SourceType


class CollectorInterface(ABC):
    """
    Abstract base class for all OSINT collectors.

    Collectors are responsible for acquiring data from specific sources
    while maintaining provenance and source reliability information.
    """

    def __init__(
        self, source_name: str, source_type: SourceType, reliability: float = 0.5
    ):
        """
        Initialize a collector.

        Args:
            source_name: Human-readable name of the source (e.g., "Twitter", "GitHub")
            source_type: Type of source from SourceType enum
            reliability: Initial reliability score (0.0 to 1.0)
        """
        self.source_name = source_name
        self.source_type = source_type
        self.reliability = max(0.0, min(1.0, reliability))  # Clamp to [0, 1]

    @abstractmethod
    def collect(self, **kwargs) -> List[RawObservation]:
        """
        Collect observations from the source.

        Args:
            **kwargs: Source-specific collection parameters

        Returns:
            List of RawObservation objects

        Raises:
            CollectionError: If collection fails
        """
        pass

    def get_source_info(self) -> dict:
        """
        Get information about this collector's source.

        Returns:
            Dictionary containing source metadata
        """
        return {
            "source_name": self.source_name,
            "source_type": self.source_type.value,
            "reliability": self.reliability,
            "collector_type": self.__class__.__name__,
        }

    def update_reliability(self, new_reliability: float):
        """
        Update the source reliability score.

        Args:
            new_reliability: New reliability score (0.0 to 1.0)
        """
        self.reliability = max(0.0, min(1.0, new_reliability))


class CollectionError(Exception):
    """Exception raised when collection fails."""

    def __init__(self, message: str, source_name: str, collector_type: str):
        super().__init__(
            f"[{collector_type}] Failed to collect from {source_name}: {message}"
        )
        self.source_name = source_name
        self.collector_type = collector_type
