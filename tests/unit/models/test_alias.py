"""
Unit tests for Alias model.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.alias import Alias
from src.drishti.core.models.base import EntityReference


def test_alias_creation():
    """Test that Alias can be created with required fields."""
    alias = Alias(
        handle="test_handler", platform="forum", source="test_source", source_type="web"
    )

    assert alias.handle == "test_handler"
    assert alias.platform == "forum"
    assert alias.source == "test_source"
    assert alias.source_type == "web"
    assert isinstance(alias.id, UUID)
    assert isinstance(alias.created_at, datetime)
    assert alias.actor is None  # default
    assert alias.posts == []  # default


def test_alias_with_actor_reference():
    """Test Alias with actor relationship."""
    actor_ref = EntityReference(
        id=UUID("22222222-2222-2222-2222-222222222222"),
        entity_type="Actor",
        relationship="OWNED_BY",
    )

    alias = Alias(
        handle="test_handler",
        platform="forum",
        source="test_source",
        source_type="web",
        actor=actor_ref,
    )

    assert alias.actor is not None
    assert alias.actor.id == UUID("22222222-2222-2222-2222-222222222222")
    assert alias.actor.entity_type == "Actor"


def test_alias_timestamps():
    """Test Alias timestamp fields."""
    first_seen = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    last_seen = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    alias = Alias(
        handle="test_handler",
        platform="forum",
        source="test_source",
        source_type="web",
        first_seen=first_seen,
        last_seen=last_seen,
    )

    assert alias.first_seen == first_seen
    assert alias.last_seen == last_seen


def test_alias_confidence_validation():
    """Test that Alias confidence is validated."""
    # Valid confidence
    alias = Alias(
        handle="test",
        platform="test",
        source="test",
        source_type="test",
        confidence=0.7,
    )
    assert alias.confidence == 0.7

    # Invalid confidence
    with pytest.raises(ValidationError):
        Alias(
            handle="test",
            platform="test",
            source="test",
            source_type="test",
            confidence=-0.1,
        )
