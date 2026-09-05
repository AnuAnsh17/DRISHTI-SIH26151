"""
Unit tests for collector registry.
"""

import pytest
from unittest.mock import Mock

from src.drishti.collection.registry import CollectorRegistry, registry
from src.drishti.collection.base import CollectorInterface, CollectionError
from src.drishti.collection.models import SourceType


class MockCollector(CollectorInterface):
    """Mock collector for testing."""

    def __init__(self, name="mock", source_type=SourceType.SYNTHETIC):
        super().__init__(name, source_type)

    def collect(self, **kwargs):
        return []


class AnotherMockCollector(CollectorInterface):
    """Another mock collector for testing."""

    def __init__(self, name="another", source_type=SourceType.SURFACE_WEB):
        super().__init__(name, source_type)

    def collect(self, **kwargs):
        return []


def test_registry_initialization():
    """Test registry initialization."""
    reg = CollectorRegistry()
    assert len(reg.list_collectors()) == 0
    assert len(reg._collectors) == 0
    assert len(reg._instances) == 0


def test_registry_register_collector():
    """Test registering a collector."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    assert "test_mock" in reg.list_collectors()
    assert reg.get_collector_info("test_mock")["class"] == "MockCollector"


def test_registry_register_invalid_collector():
    """Test registering invalid collector class."""
    reg = CollectorRegistry()

    class NotACollector:
        pass

    with pytest.raises(ValueError, match="must extend CollectorInterface"):
        reg.register("invalid", NotACollector)


def test_registry_get_collector():
    """Test getting a registered collector."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    collector = reg.get("test_mock")
    assert isinstance(collector, MockCollector)
    assert collector.source_name == "mock"  # Default name from MockCollector
    assert collector.source_type == SourceType.SYNTHETIC


def test_registry_get_unregistered_collector():
    """Test getting an unregistered collector."""
    reg = CollectorRegistry()

    with pytest.raises(KeyError, match="not registered"):
        reg.get("nonexistent")


def test_registry_get_collector_class():
    """Test getting collector class without instantiation."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    collector_class = reg.get_class("test_mock")
    assert collector_class == MockCollector


def test_registry_get_collector_info():
    """Test getting collector information."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    info = reg.get_collector_info("test_mock")
    assert info["name"] == "test_mock"
    assert info["class"] == "MockCollector"
    assert info["module"] == MockCollector.__module__
    assert info["doc"] == MockCollector.__doc__


def test_registry_list_collectors():
    """Test listing all registered collectors."""
    reg = CollectorRegistry()
    reg.register("mock1", MockCollector)
    reg.register("mock2", AnotherMockCollector)

    collectors = reg.list_collectors()
    assert len(collectors) == 2
    assert "mock1" in collectors
    assert "mock2" in collectors


def test_registry_unregister_collector():
    """Test unregistering a collector."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    assert "test_mock" in reg.list_collectors()
    reg.unregister("test_mock")
    assert "test_mock" not in reg.list_collectors()

    # Should not be able to get it anymore
    with pytest.raises(KeyError):
        reg.get("test_mock")


def test_registry_unregister_nonexistent():
    """Test unregistering nonexistent collector (should not fail)."""
    reg = CollectorRegistry()
    # Should not raise exception
    reg.unregister("nonexistent")


def test_registry_cached_instances():
    """Test that registry caches collector instances."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)

    # Get same collector twice
    collector1 = reg.get("test_mock")
    collector2 = reg.get("test_mock")

    # Should be the same instance (cached)
    assert collector1 is collector2
    assert len(reg._instances) == 1


def test_registry_clear_instances():
    """Test clearing cached instances."""
    reg = CollectorRegistry()
    reg.register("test_mock", MockCollector)
    reg.register("another_mock", AnotherMockCollector)

    # Get instances to cache them
    reg.get("test_mock")
    reg.get("another_mock")

    assert len(reg._instances) == 2

    reg.clear_instances()
    assert len(reg._instances) == 0

    # Getting again should create new instances
    collector1 = reg.get("test_mock")
    collector2 = reg.get("test_mock")
    assert collector1 is collector2  # Should still cache
    assert len(reg._instances) == 1


def test_global_registry_has_synthetic():
    """Test that the global registry has the synthetic collector registered."""
    # The synthetic collector should be registered via adapters/__init__.py
    collectors = registry.list_collectors()
    assert "synthetic" in collectors

    # Should be able to get it
    synthetic_collector = registry.get("synthetic")
    from src.drishti.collection.adapters.synthetic import SyntheticCollector
    assert isinstance(synthetic_collector, SyntheticCollector)


def test_registry_multiple_registrations_same_name():
    """Test registering collector with same name twice."""
    reg = CollectorRegistry()
    reg.register("test", MockCollector)
    reg.register("test", AnotherMockCollector)  # Should overwrite

    # Should get the second one
    collector = reg.get("test")
    assert isinstance(collector, AnotherMockCollector)
    assert collector.source_type == SourceType.SURFACE_WEB


def test_registry_collector_with_parameters():
    """Test registry with collector requiring parameters."""
    class ParameterizedCollector(CollectorInterface):
        def __init__(self, param1):  # No default - required parameter
            # Call parent with fixed values for testing
            super().__init__("param_source", SourceType.SYNTHETIC)
            self.param1 = param1

        def collect(self, **kwargs):
            return []

    reg = CollectorRegistry()
    reg.register("param", ParameterizedCollector)

    # This will fail because our simple registry doesn't handle parameters
    # In a real implementation, we might use factories or dependency injection
    # For now, we expect it to fail when trying to instantiate without params
    with pytest.raises(TypeError):
        reg.get("param")  # Missing required parameter