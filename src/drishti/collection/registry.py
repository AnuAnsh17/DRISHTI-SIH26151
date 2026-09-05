"""
Collector registry for DRISHTI OSINT collection framework.
"""

import logging
from typing import Dict, List, Optional, Type
from uuid import UUID

from .base import CollectorInterface, CollectionError
from .models import SourceType

logger = logging.getLogger(__name__)


class CollectorRegistry:
    """
    Registry for discovering and instantiating OSINT collectors.

    Collectors can be registered by name and retrieved when needed.
    This allows for dynamic plugin-style addition of new collection sources.
    """

    def __init__(self):
        self._collectors: Dict[str, Type[CollectorInterface]] = {}
        self._instances: Dict[str, CollectorInterface] = {}

    def register(self, name: str, collector_class: Type[CollectorInterface]):
        """
        Register a collector class with the registry.

        Args:
            name: Unique identifier for the collector
            collector_class: Collector class that extends CollectorInterface
        """
        if not issubclass(collector_class, CollectorInterface):
            raise ValueError(
                f"Collector class {collector_class} must extend CollectorInterface"
            )

        self._collectors[name] = collector_class
        logger.debug(f"Registered collector: {name}")

    def unregister(self, name: str):
        """
        Unregister a collector from the registry.

        Args:
            name: Identifier of the collector to unregister
        """
        if name in self._collectors:
            del self._collectors[name]
            # Also remove any cached instance
            if name in self._instances:
                del self._instances[name]
            logger.debug(f"Unregistered collector: {name}")

    def get(self, name: str) -> CollectorInterface:
        """
        Get an instantiated collector by name.

        Args:
            name: Identifier of the collector to retrieve

        Returns:
            Instantiated collector object

        Raises:
            KeyError: If collector is not registered
        """
        if name not in self._collectors:
            raise KeyError(f"Collector '{name}' not registered in registry")

        # Return cached instance if available
        if name in self._instances:
            return self._instances[name]

        # Create and cache new instance
        collector_class = self._collectors[name]
        # Note: Collectors must be instantiated with appropriate parameters
        # This basic implementation assumes a default constructor or factory pattern
        # For more complex initialization, consider using factory functions
        try:
            instance = collector_class()
            self._instances[name] = instance
            logger.debug(f"Instantiated collector: {name}")
            return instance
        except Exception as e:
            logger.error(f"Failed to instantiate collector '{name}': {e}")
            raise

    def get_class(self, name: str) -> Type[CollectorInterface]:
        """
        Get the collector class by name (without instantiation).

        Args:
            name: Identifier of the collector class to retrieve

        Returns:
            Collector class

        Raises:
            KeyError: If collector is not registered
        """
        if name not in self._collectors:
            raise KeyError(f"Collector '{name}' not registered in registry")
        return self._collectors[name]

    def list_collectors(self) -> List[str]:
        """
        List all registered collector names.

        Returns:
            List of registered collector names
        """
        return list(self._collectors.keys())

    def get_collector_info(self, name: str) -> dict:
        """
        Get information about a registered collector.

        Args:
            name: Identifier of the collector

        Returns:
            Dictionary containing collector information

        Raises:
            KeyError: If collector is not registered
        """
        if name not in self._collectors:
            raise KeyError(f"Collector '{name}' not registered in registry")

        collector_class = self._collectors[name]
        return {
            "name": name,
            "class": collector_class.__name__,
            "module": collector_class.__module__,
            "doc": collector_class.__doc__,
        }

    def clear_instances(self):
        """Clear all cached collector instances."""
        self._instances.clear()
        logger.debug("Cleared all cached collector instances")


# Global registry instance
registry = CollectorRegistry()
