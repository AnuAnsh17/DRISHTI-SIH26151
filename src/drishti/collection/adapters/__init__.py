"""
OSINT collector adapters for DRISHTI.
"""

from .synthetic import SyntheticCollector
from ..registry import registry

# Register the synthetic collector
registry.register("synthetic", SyntheticCollector)

__all__ = ["SyntheticCollector"]
