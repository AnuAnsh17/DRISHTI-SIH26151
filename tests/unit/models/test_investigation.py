"""
Unit tests for Investigation model.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.investigation import Investigation, InvestigationStatus
from src.drishti.core.models.base import EntityReference


def test_investigation_creation():
    """Test that Investigation can be created with required fields."""
    investigation = Investigation(title="Test Investigation")

    assert investigation.title == "Test Investigation"
    assert isinstance(investigation.id, UUID)
    assert isinstance(investigation.created_at, datetime)
    assert investigation.description is None  # default
    assert investigation.status == InvestigationStatus.OPEN  # default
    assert investigation.actors == []  # default
    assert investigation.posts == []  # default
    assert investigation.evidence == []  # default
    assert investigation.hypotheses == []  # default


def test_investigation_with_all_fields():
    """Test Investigation with all fields populated."""
    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    actor_ref = EntityReference(
        id=UUID("11111111-1111-1111-1111-111111111111"),
        entity_type="Actor",
        relationship="INVESTIGATED",
    )
    post_ref = EntityReference(
        id=UUID("22222222-2222-2222-2222-222222222222"),
        entity_type="Post",
        relationship="PART_OF",
    )
    investigation = Investigation(
        title="Test Investigation",
        description="A test investigation for unit testing",
        status=InvestigationStatus.CLOSED,
        actors=[actor_ref],
        posts=[post_ref],
        evidence=[UUID("33333333-3333-3333-3333-333333333333")],
        hypotheses=[UUID("44444444-4444-4444-4444-444444444444")],
    )

    assert investigation.title == "Test Investigation"
    assert investigation.description == "A test investigation for unit testing"
    assert investigation.status == InvestigationStatus.CLOSED
    assert len(investigation.actors) == 1
    assert investigation.actors[0].id == UUID("11111111-1111-1111-1111-111111111111")
    assert len(investigation.posts) == 1
    assert investigation.posts[0].id == UUID("22222222-2222-2222-2222-222222222222")
    assert len(investigation.evidence) == 1
    assert investigation.evidence[0] == UUID("33333333-3333-3333-3333-333333333333")
    assert len(investigation.hypotheses) == 1
    assert investigation.hypotheses[0] == UUID("44444444-4444-4444-4444-444444444444")


def test_investigation_status_validation():
    """Test that investigation status works."""
    # Valid statuses should work
    for status in [
        InvestigationStatus.OPEN,
        InvestigationStatus.CLOSED,
        InvestigationStatus.ARCHIVED,
    ]:
        investigation = Investigation(title="Test", status=status)
        assert investigation.status == status


def test_investigation_timestamps():
    """Test Investigation timestamp fields."""
    created_time = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    updated_time = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    investigation = Investigation(
        title="Test Investigation", created_at=created_time, updated_at=updated_time
    )

    assert investigation.created_at == created_time
    assert investigation.updated_at == updated_time
