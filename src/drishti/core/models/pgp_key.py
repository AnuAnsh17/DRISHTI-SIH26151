"""
PGPKey model for DRISHTI intelligence schema.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, ProvenanceMixin, EntityReference


class PGPKey(BaseEntity, ProvenanceMixin):
    """
    PGPKey represents a Pretty Good Privacy encryption key.
    """
    fingerprint: str = Field(..., description="PGP key fingerprint")
    first_seen: Optional[datetime] = Field(
        default=None,
        description="First time this PGP key was observed"
    )
    last_seen: Optional[datetime] = Field(
        default=None,
        description="Last time this PGP key was observed"
    )
    # Relationships
    actor: Optional[EntityReference] = Field(
        default=None,
        description="Actor that uses this PGP key"
    )
    posts: List[EntityReference] = Field(
        default_factory=list,
        description="Posts signed with this key"
    )
