"""
OSINT collection framework for DRISHTI.
"""

from .base import CollectorInterface, CollectionError
from .models import RawObservation, SourceType
from .registry import registry, CollectorRegistry

# Import adapters to make them available for registration
from . import adapters

__all__ = [
    "CollectorInterface",
    "CollectionError",
    "RawObservation",
    "SourceType",
    "registry",
    "CollectorRegistry",
]
