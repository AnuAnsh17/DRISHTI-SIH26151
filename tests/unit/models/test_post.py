"""
Unit tests for Post model.
"""
from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.post import Post
from src.drishti.core.models.base import EntityReference


def test_post_creation():
    """Test that Post can be created with required fields."""
    post = Post(
        platform="forum",
        content="This is a test post",
        source="test_source",
        source_type="web"
    )
    
    assert post.platform == "forum"
    assert post.content == "This is a test post"
    assert post.source == "test_source"
    assert post.source_type == "web"
    assert isinstance(post.id, UUID)
    assert isinstance(post.created_at, datetime)
    assert isinstance(post.timestamp, datetime)
    assert post.author is None  # default
    assert post.mentioned_entities == []  # default
    assert post.investigation is None  # default


def test_post_with_author_reference():
    """Test Post with author relationship."""
    author_ref = EntityReference(
        id=UUID('44444444-4444-4444-4444-444444444444'),
        entity_type="Alias",
        relationship="AUTHORED_BY"
    )
    
    post = Post(
        platform="forum",
        content="This is a test post",
        source="test_source",
        source_type="web",
        author=author_ref
    )
    
    assert post.author is not None
    assert post.author.id == UUID('44444444-4444-4444-4444-444444444444')
    assert post.author.entity_type == "Alias"


def test_post_timestamps():
    """Test Post timestamp fields."""
    post_time = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    
    post = Post(
        platform="forum",
        content="This is a test post",
        source="test_source",
        source_type="web",
        timestamp=post_time
    )
    
    assert post.timestamp == post_time


def test_post_mentioned_entities():
    """Test Post with mentioned entities."""
    entity_ref1 = EntityReference(
        id=UUID('55555555-5555-5555-5555-555555555555'),
        entity_type="Actor",
        relationship="MENTIONED_IN"
    )
    entity_ref2 = EntityReference(
        id=UUID('66666666-6666-6666-6666-666666666666'),
        entity_type="Wallet",
        relationship="MENTIONED_IN"
    )
    
    post = Post(
        platform="forum",
        content="This is a test post mentioning entities",
        source="test_source",
        source_type="web",
        mentioned_entities=[entity_ref1, entity_ref2]
    )
    
    assert len(post.mentioned_entities) == 2
    assert post.mentioned_entities[0].id == UUID('55555555-5555-5555-5555-555555555555')
    assert post.mentioned_entities[1].id == UUID('66666666-6666-6666-6666-666666666666')


def test_post_confidence_validation():
    """Test that Post confidence is validated."""
    # Valid confidence
    post = Post(
        platform="forum",
        content="test",
        source="test",
        source_type="test",
        confidence=0.6
    )
    assert post.confidence == 0.6
    
    # Invalid confidence
    with pytest.raises(ValidationError):
        Post(
            platform="forum",
            content="test",
            source="test",
            source_type="test",
            confidence=1.5
        )
