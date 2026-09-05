"""
Unit tests for Actor model.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.actor import Actor, AttributionStatus
from src.drishti.core.models.base import EntityReference


def test_actor_creation():
    """Test that Actor can be created with required fields."""
    actor = Actor(source="test_source", source_type="web")

    assert isinstance(actor.id, UUID)
    assert actor.source == "test_source"
    assert actor.source_type == "web"
    assert actor.attribution_status == AttributionStatus.PENDING  # default
    assert actor.aliases == []  # default empty list
    assert actor.posts == []  # default empty list


def test_actor_with_all_fields():
    """Test Actor with all fields populated."""
    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    alias_ref = EntityReference(
        id=UUID("11111111-1111-1111-1111-111111111111"),
        entity_type="Alias",
        relationship="USES",
    )

    actor = Actor(
        source="test_source",
        source_type="web",
        first_seen=now,
        last_seen=now,
        canonical_name="Test Actor",
        description="A test actor",
        attribution_status=AttributionStatus.CONFIRMED,
        aliases=[alias_ref],
        confidence=0.9,
    )

    assert actor.first_seen == now
    assert actor.last_seen == now
    assert actor.canonical_name == "Test Actor"
    assert actor.description == "A test actor"
    assert actor.attribution_status == AttributionStatus.CONFIRMED
    assert len(actor.aliases) == 1
    assert actor.aliases[0].id == UUID("11111111-1111-1111-1111-111111111111")
    assert actor.confidence == 0.9


def test_actor_attribution_status_validation():
    """Test that attribution status works."""
    # Valid statuses should work
    for status in [
        AttributionStatus.PENDING,
        AttributionStatus.CONFIRMED,
        AttributionStatus.REJECTED,
        AttributionStatus.DISPUTED,
    ]:
        actor = Actor(source="test", source_type="test", attribution_status=status)
        assert actor.attribution_status == status


def test_actor_confidence_validation():
    """Test that Actor confidence is validated."""
    # Valid confidence
    actor = Actor(source="test", source_type="test", confidence=0.5)
    assert actor.confidence == 0.5

    # Invalid confidence
    with pytest.raises(ValidationError):
        Actor(source="test", source_type="test", confidence=1.5)
