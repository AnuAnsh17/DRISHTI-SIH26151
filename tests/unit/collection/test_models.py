"""
Unit tests for collection models.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError

from src.drishti.collection.models import RawObservation, SourceType
from src.drishti.core.models.evidence import Evidence


def test_source_type_enum():
    """Test that SourceType enum has expected values."""
    assert SourceType.SURFACE_WEB.value == "surface_web"
    assert SourceType.PUBLIC_FORUM.value == "public_forum"
    assert SourceType.PUBLIC_SOCIAL.value == "public_social"
    assert SourceType.PUBLIC_REPOSITORY.value == "public_repository"
    assert SourceType.PASTE_SOURCE.value == "paste_source"
    assert SourceType.SECURITY_REPORT.value == "security_report"
    assert SourceType.CERTIFICATE_TRANSPARENCY.value == "certificate_transparency"
    assert SourceType.PASSIVE_DNS.value == "passive_dns"
    assert SourceType.ONION_METADATA.value == "onion_metadata"
    assert SourceType.SYNTHETIC.value == "synthetic"


def test_raw_observation_creation():
    """Test that RawObservation can be created with required fields."""
    observed_at = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    collected_at = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    obs = RawObservation(
        source="test_source",
        source_type=SourceType.SYNTHETIC,
        title="Test Observation",
        content="Test content",
        observed_at=observed_at,
        collected_at=collected_at
    )

    assert obs.source == "test_source"
    assert obs.source_type == "synthetic"  # With use_enum_values=True, returns the value
    assert obs.title == "Test Observation"
    assert obs.content == "Test content"
    assert obs.observed_at == observed_at
    assert obs.collected_at == collected_at
    assert isinstance(obs.observation_id, UUID)
    assert obs.reliability == 0.5  # default
    assert obs.collection_method == "unknown"  # default
    assert obs.metadata == {}  # default


def test_raw_observation_defaults():
    """Test RawObservation default values."""
    obs = RawObservation(
        source="test_source",
        source_type=SourceType.SYNTHETIC
    )

    assert obs.source == "test_source"
    assert obs.source_type == "synthetic"  # With use_enum_values=True, returns the value
    assert obs.title is None
    assert obs.content is None
    assert obs.observed_at is None
    assert isinstance(obs.collected_at, datetime)
    assert obs.reliability == 0.5
    assert obs.collection_method == "unknown"
    assert obs.metadata == {}


def test_raw_observation_validation():
    """Test RawObservation field validation."""
    # Test reliability validation
    with pytest.raises(ValidationError):
        RawObservation(
            source="test_source",
            source_type=SourceType.SYNTHETIC,
            reliability=1.5  # > 1.0
        )

    with pytest.raises(ValidationError):
        RawObservation(
            source="test_source",
            source_type=SourceType.SYNTHETIC,
            reliability=-0.5  # < 0.0
        )


def test_raw_observation_to_evidence():
    """Test converting RawObservation to Evidence."""
    obs = RawObservation(
        source="test_source",
        source_type=SourceType.SYNTHETIC,
        title="Test Observation",
        content="test_value",
        reliability=0.8,
        collection_method="test_method"
    )

    evidence = obs.to_evidence(
        evidence_type="test_evidence",
        subject="test_subject",
        object_value="test_object"
    )

    assert isinstance(evidence, Evidence)
    assert evidence.evidence_type == "test_evidence"
    assert evidence.subject == "test_subject"
    assert evidence.object_value == "test_object"
    assert evidence.source == "test_source"
    assert evidence.source_type == "synthetic"  # String value due to use_enum_values=True
    assert evidence.confidence == 0.8  # from reliability
    assert "Collected via test_method from test_source" in evidence.explanation
    assert evidence.reference_id == str(obs.observation_id)


def test_raw_observation_serialization():
    """Test RawObservation serialization to dict and back."""
    observed_at = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    collected_at = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    obs = RawObservation(
        source="test_source",
        source_type=SourceType.SYNTHETIC,
        title="Test Observation",
        content="test_content",
        observed_at=observed_at,
        collected_at=collected_at,
        reliability=0.9,
        collection_method="test_collection",
        metadata={"key": "value"}
    )

    # Serialize to dict
    obs_dict = obs.model_dump()
    assert isinstance(obs_dict, dict)
    assert obs_dict["source"] == "test_source"
    assert obs_dict["source_type"] == "synthetic"
    assert obs_dict["title"] == "Test Observation"
    assert obs_dict["content"] == "test_content"
    assert obs_dict["reliability"] == 0.9
    assert obs_dict["collection_method"] == "test_collection"
    assert obs_dict["metadata"] == {"key": "value"}

    # Deserialize from dict
    obs_restored = RawObservation.model_validate(obs_dict)
    assert obs_restored.source == obs.source
    assert obs_restored.source_type == obs.source_type
    assert obs_restored.title == obs.title
    assert obs_restored.content == obs.content
    assert obs_restored.observed_at == obs.observed_at
    assert obs_restored.collected_at == obs.collected_at
    assert obs_restored.reliability == obs.reliability
    assert obs_restored.collection_method == obs.collection_method
    assert obs_restored.metadata == obs.metadata