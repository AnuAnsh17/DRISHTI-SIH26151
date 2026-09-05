"""
Alias model for DRISHTI intelligence schema.
"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, ProvenanceMixin, EntityReference


class Alias(BaseEntity, ProvenanceMixin):
    """
    Alias represents a pseudonym, handle, or identifier used by an actor.
    """

    handle: str = Field(..., description="The alias/handle value")
    platform: str = Field(..., description="Platform where alias is used")
    first_seen: Optional[datetime] = Field(
        default=None, description="First time this alias was observed"
    )
    last_seen: Optional[datetime] = Field(
        default=None, description="Last time this alias was observed"
    )
    # Relationships
    actor: Optional[EntityReference] = Field(
        default=None, description="Actor that uses this alias"
    )
    posts: List[EntityReference] = Field(
        default_factory=list, description="Posts where this alias appears"
    )
