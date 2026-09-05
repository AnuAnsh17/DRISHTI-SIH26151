"""
Unit tests for AttributionHypothesis model.
"""
from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.attribution import AttributionHypothesis
from src.drishti.core.models.base import EntityReference


def test_attributionhypothesis_creation():
    """Test that AttributionHypothesis can be created with required fields."""
    hypothesis = AttributionHypothesis(
        hypothesis_type="alias_to_actor",
        subject="test_handler",
        candidate_entities=[
            EntityReference(
                id=UUID('11111111-1111-1111-1111-111111111111'),
                entity_type="Actor",
                relationship="POSSIBLY_SAME_AS"
            )
        ]
    )

    assert hypothesis.hypothesis_type == "alias_to_actor"
    assert hypothesis.subject == "test_handler"
    assert len(hypothesis.candidate_entities) == 1
    assert hypothesis.candidate_entities[0].id == UUID('11111111-1111-1111-1111-111111111111')
    assert isinstance(hypothesis.id, UUID)
    assert isinstance(hypothesis.created_at, datetime)
    assert hypothesis.association_score == 0.0  # default
    assert hypothesis.confidence == 0.0  # default
    assert hypothesis.supporting_evidence == []  # default
    assert hypothesis.contradicting_evidence == []  # default
    assert hypothesis.explanation is None  # default
    assert hypothesis.investigation is None  # default


def test_attributionhypothesis_with_all_fields():
    """Test AttributionHypothesis with all fields populated."""
    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    inv_ref = EntityReference(
        id=UUID('22222222-2222-2222-2222-222222222222'),
        entity_type="Investigation",
        relationship="PART_OF"
    )
    
    hypothesis = AttributionHypothesis(
        hypothesis_type="wallet_to_actor",
        subject="0x742d35Cc6634C0532925a3b8D4C0532950532950",
        candidate_entities=[
            EntityReference(
                id=UUID('33333333-3333-3333-3333-333333333333'),
                entity_type="Actor",
                relationship="OWNED_BY",
                confidence=0.8
            )
        ],
        association_score=0.75,
        confidence=0.82,
        supporting_evidence=[UUID('44444444-4444-4444-4444-444444444444')],
        contradicting_evidence=[UUID('55555555-5555-5555-5555-555555555555')],
        explanation="Strong wallet linkage with temporal consistency",
        source="blockchain_analysis",
        source_type="crypto",
        investigation=inv_ref
    )
    
    assert hypothesis.hypothesis_type == "wallet_to_actor"
    assert hypothesis.subject == "0x742d35Cc6634C0532925a3b8D4C0532950532950"
    assert hypothesis.association_score == 0.75
    assert hypothesis.confidence == 0.82
    assert len(hypothesis.supporting_evidence) == 1
    assert hypothesis.supporting_evidence[0] == UUID('44444444-4444-4444-4444-444444444444')
    assert len(hypothesis.contradicting_evidence) == 1
    assert hypothesis.contradicting_evidence[0] == UUID('55555555-5555-5555-5555-555555555555')
    assert hypothesis.explanation == "Strong wallet linkage with temporal consistency"
    assert hypothesis.investigation is not None
    assert hypothesis.investigation.id == UUID('22222222-2222-2222-2222-222222222222')


def test_attributionhypothesis_scores_validation():
    """Test that association_score and confidence are validated to be between 0 and 1."""
    # Valid scores
    hypothesis = AttributionHypothesis(
        hypothesis_type="test",
        subject="test",
        candidate_entities=[
            EntityReference(
                id=UUID('11111111-1111-1111-1111-111111111111'),
                entity_type="Actor",
                relationship="TEST"
            )
        ],
        association_score=0.5,
        confidence=0.6,
        source="test",
        source_type="test"
    )
    assert hypothesis.association_score == 0.5
    assert hypothesis.confidence == 0.6
    
    # Invalid association_score > 1
    with pytest.raises(ValidationError):
        AttributionHypothesis(
            hypothesis_type="test",
            subject="test",
            candidate_entities=[
                EntityReference(
                    id=UUID('11111111-1111-1111-1111-111111111111'),
                    entity_type="Actor",
                    relationship="TEST"
                )
            ],
            association_score=1.5,
            confidence=0.5,
            source="test",
            source_type="test"
        )
    
    # Invalid confidence < 0
    with pytest.raises(ValidationError):
        AttributionHypothesis(
            hypothesis_type="test",
            subject="test",
            candidate_entities=[
                EntityReference(
                    id=UUID('11111111-1111-1111-1111-111111111111'),
                    entity_type="Actor",
                    relationship="TEST"
                )
            ],
            association_score=0.5,
            confidence=-0.2,
            source="test",
            source_type="test"
        )


def test_attributionhypothesis_investigation_reference():
    """Test AttributionHypothesis with investigation reference."""
    inv_ref = EntityReference(
        id=UUID('66666666-6666-6666-6666-666666666666'),
        entity_type="Investigation",
        relationship="BELONGS_TO"
    )
    
    hypothesis = AttributionHypothesis(
        hypothesis_type="test",
        subject="test",
        candidate_entities=[
            EntityReference(
                id=UUID('11111111-1111-1111-1111-111111111111'),
                entity_type="Actor",
                relationship="TEST"
            )
        ],
        source="test",
        source_type="test",
        investigation=inv_ref
    )
    
    assert hypothesis.investigation is not None
    assert hypothesis.investigation.id == UUID('66666666-6666-6666-6666-666666666666')
    assert hypothesis.investigation.entity_type == "Investigation"
