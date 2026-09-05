"""
Post model for DRISHTI intelligence schema.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import EntityReference
from .base import BaseEntity, ProvenanceMixin


class Post(BaseEntity, ProvenanceMixin):
    """
    Post represents a content item (forum post, marketplace listing, etc.).
    """
    platform: str = Field(..., description="Platform where post appears")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="When the post was created/published"
    )
    content: str = Field(..., description="The actual post content")
    # Relationships
    author: Optional[EntityReference] = Field(
        default=None,
        description="Alias that authored this post"
    )
    mentioned_entities: List[EntityReference] = Field(
        default_factory=list,
        description="Entities mentioned in this post"
    )
    investigation: Optional[EntityReference] = Field(
        default=None,
        description="Investigation this post belongs to"
    )
