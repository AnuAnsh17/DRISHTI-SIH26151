"""
Unit tests for base models.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.base import BaseEntity, ProvenanceMixin, EntityReference
from src.drishti.core.models.evidence import Evidence


def test_base_entity_creation():
    """Test that BaseEntity can be created with default values."""
    entity = BaseEntity()
    assert isinstance(entity.id, UUID)
    assert isinstance(entity.created_at, datetime)
    # updated_at should be None by default
    assert entity.updated_at is None


def test_base_entity_with_values():
    """Test that BaseEntity accepts custom values."""
    custom_id = UUID("12345678-1234-5678-1234-567812345678")
    custom_time = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    entity = BaseEntity(id=custom_id, created_at=custom_time, updated_at=custom_time)

    assert entity.id == custom_id
    assert entity.created_at == custom_time
    assert entity.updated_at == custom_time


def test_provenance_mixin():
    """Test ProvenanceMixin fields."""
    prov = ProvenanceMixin(
        source="test_source",
        source_type="web",
        collected_at=datetime(2023, 1, 1, 12, 0, 0),
        observation_timestamp=datetime(2023, 1, 1, 10, 0, 0),
        confidence=0.8,
        explanation="Test explanation",
        reference_id="ref123",
    )

    assert prov.source == "test_source"
    assert prov.source_type == "web"
    assert prov.confidence == 0.8
    assert prov.explanation == "Test explanation"
    assert prov.reference_id == "ref123"


def test_provenance_confidence_validation():
    """Test that confidence is validated to be between 0 and 1."""
    # Valid confidence
    prov = ProvenanceMixin(source="test", source_type="test", confidence=0.5)
    assert prov.confidence == 0.5

    # Invalid confidence > 1
    with pytest.raises(ValidationError):
        ProvenanceMixin(source="test", source_type="test", confidence=1.5)

    # Invalid confidence < 0
    with pytest.raises(ValidationError):
        ProvenanceMixin(source="test", source_type="test", confidence=-0.5)


def test_entity_reference():
    """Test EntityReference creation."""
    ref_id = UUID("12345678-1234-5678-1234-567812345678")
    ref = EntityReference(
        id=ref_id, entity_type="Actor", relationship="USES", confidence=0.9
    )

    assert ref.id == ref_id
    assert ref.entity_type == "Actor"
    assert ref.relationship == "USES"
    assert ref.confidence == 0.9


def test_evidence_creation():
    """Test Evidence model creation."""
    evidence = Evidence(
        evidence_type="alias_mention",
        subject="Test Subject",
        object_value="test_alias",
        source="test_source",
        source_type="web",
    )

    assert evidence.evidence_type == "alias_mention"
    assert evidence.subject == "Test Subject"
    assert evidence.object_value == "test_alias"
    assert evidence.source == "test_source"
    assert evidence.source_type == "web"
    assert isinstance(evidence.id, UUID)
    assert isinstance(evidence.created_at, datetime)
    assert evidence.extracted_entities == []


def test_evidence_serialization():
    """Test Evidence serialization to dict and back."""
    evidence = Evidence(
        evidence_type="alias_mention",
        subject="Test Subject",
        object_value="test_alias",
        source="test_source",
        source_type="web",
        confidence=0.8,
    )

    # Serialize to dict
    evidence_dict = evidence.model_dump()
    assert isinstance(evidence_dict, dict)
    assert evidence_dict["evidence_type"] == "alias_mention"
    assert evidence_dict["subject"] == "Test Subject"
    assert "id" in evidence_dict
    assert "created_at" in evidence_dict

    # Deserialize from dict
    evidence_restored = Evidence.model_validate(evidence_dict)
    assert evidence_restored.id == evidence.id
    assert evidence_restored.evidence_type == evidence.evidence_type
    assert evidence_restored.subject == evidence.subject
    assert evidence_restored.object_value == evidence.object_value
