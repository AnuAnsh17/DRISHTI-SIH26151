"""
Unit tests for PGPKey model.
"""
from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.pgp_key import PGPKey
from src.drishti.core.models.base import EntityReference


def test_pgpkey_creation():
    """Test that PGPKey can be created with required fields."""
    pgp_key = PGPKey(
        fingerprint="abcdef1234567890abcdef1234567890abcdef12",
        source="test_source",
        source_type="web"
    )
    
    assert pgp_key.fingerprint == "abcdef1234567890abcdef1234567890abcdef12"
    assert pgp_key.source == "test_source"
    assert pgp_key.source_type == "web"
    assert isinstance(pgp_key.id, UUID)
    assert isinstance(pgp_key.created_at, datetime)
    assert pgp_key.actor is None  # default
    assert pgp_key.posts == []  # default


def test_pgpkey_with_actor_reference():
    """Test PGPKey with actor relationship."""
    actor_ref = EntityReference(
        id=UUID('77777777-7777-7777-7777-777777777777'),
        entity_type="Actor",
        relationship="USED_BY"
    )
    
    pgp_key = PGPKey(
        fingerprint="abcdef1234567890abcdef1234567890abcdef12",
        source="test_source",
        source_type="web",
        actor=actor_ref
    )
    
    assert pgp_key.actor is not None
    assert pgp_key.actor.id == UUID('77777777-7777-7777-7777-777777777777')
    assert pgp_key.actor.entity_type == "Actor"


def test_pgpkey_timestamps():
    """Test PGPKey timestamp fields."""
    first_seen = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    last_seen = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    
    pgp_key = PGPKey(
        fingerprint="abcdef1234567890abcdef1234567890abcdef12",
        source="test_source",
        source_type="web",
        first_seen=first_seen,
        last_seen=last_seen
    )
    
    assert pgp_key.first_seen == first_seen
    assert pgp_key.last_seen == last_seen


def test_pgpkey_confidence_validation():
    """Test that PGPKey confidence is validated."""
    # Valid confidence
    pgp_key = PGPKey(
        fingerprint="abcdef1234567890abcdef1234567890abcdef12",
        source="test",
        source_type="test",
        confidence=0.9
    )
    assert pgp_key.confidence == 0.9
    
    # Invalid confidence
    with pytest.raises(ValidationError):
        PGPKey(
            fingerprint="abcdef1234567890abcdef1234567890abcdef12",
            source="test",
            source_type="test",
            confidence=-0.2
        )
