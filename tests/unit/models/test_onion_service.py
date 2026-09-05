"""
Unit tests for OnionService model.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.onion_service import OnionService
from src.drishti.core.models.base import EntityReference


def test_onionservice_creation():
    """Test that OnionService can be created with required fields."""
    onion_service = OnionService(
        onion_address="abcdef123456.onion", source="test_source", source_type="tor"
    )

    assert onion_service.onion_address == "abcdef123456.onion"
    assert onion_service.source == "test_source"
    assert onion_service.source_type == "tor"
    assert isinstance(onion_service.id, UUID)
    assert isinstance(onion_service.created_at, datetime)
    assert onion_service.actor is None  # default
    assert onion_service.infrastructure == []  # default
    assert onion_service.posts == []  # default


def test_onionservice_with_actor_reference():
    """Test OnionService with actor relationship."""
    actor_ref = EntityReference(
        id=UUID("88888888-8888-8888-8888-888888888888"),
        entity_type="Actor",
        relationship="OPERATES",
    )

    onion_service = OnionService(
        onion_address="abcdef123456.onion",
        source="test_source",
        source_type="tor",
        actor=actor_ref,
    )

    assert onion_service.actor is not None
    assert onion_service.actor.id == UUID("88888888-8888-8888-8888-888888888888")
    assert onion_service.actor.entity_type == "Actor"


def test_onionservice_timestamps():
    """Test OnionService timestamp fields."""
    first_seen = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    last_seen = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    onion_service = OnionService(
        onion_address="abcdef123456.onion",
        source="test_source",
        source_type="tor",
        first_seen=first_seen,
        last_seen=last_seen,
    )

    assert onion_service.first_seen == first_seen
    assert onion_service.last_seen == last_seen


def test_onionservice_confidence_validation():
    """Test that OnionService confidence is validated."""
    # Valid confidence
    onion_service = OnionService(
        onion_address="abcdef123456.onion",
        source="test",
        source_type="test",
        confidence=0.7,
    )
    assert onion_service.confidence == 0.7

    # Invalid confidence
    with pytest.raises(ValidationError):
        OnionService(
            onion_address="abcdef123456.onion",
            source="test",
            source_type="test",
            confidence=1.5,
        )
