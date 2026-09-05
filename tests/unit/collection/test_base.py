"""
Unit tests for collection base classes.
"""

import pytest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

from src.drishti.collection.base import CollectorInterface, CollectionError
from src.drishti.collection.models import RawObservation, SourceType


class TestCollector(CollectorInterface):
    """Test collector implementation."""

    def __init__(self, source_name="test_collector", source_type=SourceType.SYNTHETIC, reliability=0.7):
        # Call parent constructor first
        super().__init__(source_name, source_type, reliability)
        # Then initialize test-specific attributes
        self.collection_count = 0
        self.should_fail = False

    def collect(self, **kwargs):
        self.collection_count += 1
        if self.should_fail:
            raise CollectionError("Test failure", self.source_name, self.__class__.__name__)

        # Return a simple observation
        return [
            RawObservation(
                source=self.source_name,
                source_type=self.source_type,
                title=f"Test observation {self.collection_count}",
                content=f"content_{self.collection_count}",
                reliability=self.reliability
            )
        ]


def test_collector_initialization():
    """Test collector initialization."""
    collector = TestCollector("test_source", SourceType.PUBLIC_SOCIAL, 0.8)

    assert collector.source_name == "test_source"
    assert collector.source_type == SourceType.PUBLIC_SOCIAL
    assert collector.reliability == 0.8


def test_collector_reliability_clamping():
    """Test that reliability is clamped to [0, 1]."""
    # Test values > 1.0
    collector = TestCollector("test", SourceType.SYNTHETIC, 1.5)
    assert collector.reliability == 1.0

    # Test values < 0.0
    collector = TestCollector("test", SourceType.SYNTHETIC, -0.5)
    assert collector.reliability == 0.0

    # Test normal values
    collector = TestCollector("test", SourceType.SYNTHETIC, 0.5)
    assert collector.reliability == 0.5


def test_collector_update_reliability():
    """Test updating collector reliability."""
    collector = TestCollector("test", SourceType.SYNTHETIC, 0.5)

    collector.update_reliability(0.9)
    assert collector.reliability == 0.9

    # Test clamping
    collector.update_reliability(1.5)
    assert collector.reliability == 1.0

    collector.update_reliability(-0.5)
    assert collector.reliability == 0.0


def test_collector_get_source_info():
    """Test getting source information."""
    collector = TestCollector("test_source", SourceType.PUBLIC_FORUM, 0.7)
    info = collector.get_source_info()

    assert info["source_name"] == "test_source"
    assert info["source_type"] == "public_forum"
    assert info["reliability"] == 0.7
    assert info["collector_type"] == "TestCollector"


def test_collector_successful_collection():
    """Test successful collection."""
    collector = TestCollector("test", SourceType.SYNTHETIC)
    observations = collector.collect()

    assert len(observations) == 1
    assert collector.collection_count == 1
    assert isinstance(observations[0], RawObservation)
    assert observations[0].source == "test"
    assert observations[0].source_type == "synthetic"  # String value due to use_enum_values=True


def test_collector_failed_collection():
    """Test failed collection raises CollectionError."""
    collector = TestCollector("test", SourceType.SYNTHETIC)
    collector.should_fail = True

    with pytest.raises(CollectionError) as exc_info:
        collector.collect()

    assert "Test failure" in str(exc_info.value)
    assert "test" in str(exc_info.value)
    assert "TestCollector" in str(exc_info.value)


def test_collector_interface_is_abstract():
    """Test that CollectorInterface cannot be instantiated directly."""
    with pytest.raises(TypeError):
        CollectorInterface("test", SourceType.SYNTHETIC)