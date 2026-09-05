"""
OnionService model for DRISHTI intelligence schema.
"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, ProvenanceMixin, EntityReference


class OnionService(BaseEntity, ProvenanceMixin):
    """
    OnionService represents a Tor hidden service.
    """

    onion_address: str = Field(
        ..., description="Onion service address (e.g., abcdef123456.onion)"
    )
    first_seen: Optional[datetime] = Field(
        default=None, description="First time this service was observed"
    )
    last_seen: Optional[datetime] = Field(
        default=None, description="Last time this service was observed"
    )
    # Relationships
    actor: Optional[EntityReference] = Field(
        default=None, description="Actor operating this service"
    )
    infrastructure: List[EntityReference] = Field(
        default_factory=list, description="Infrastructure hosting this service"
    )
    posts: List[EntityReference] = Field(
        default_factory=list, description="Posts mentioning this service"
    )
