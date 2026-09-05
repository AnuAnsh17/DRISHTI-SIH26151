"""
Actor model for DRISHTI intelligence schema.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, ProvenanceMixin, EntityReference


class Actor(BaseEntity, ProvenanceMixin):
    """
    Actor represents a threat actor, cybercriminal group, or individual 
    behind malicious activities.
    """
    first_seen: Optional[datetime] = Field(
        default=None,
        description="Earliest timestamp associated with this actor"
    )
    last_seen: Optional[datetime] = Field(
        default=None,
        description="Most recent timestamp associated with this actor"
    )
    canonical_name: Optional[str] = Field(
        default=None,
        description="Primary name or identifier (if known)"
    )
    description: Optional[str] = Field(
        default=None,
        description="Free-form description of actor activities/motivations"
    )
    attribution_status: str = Field(
        default="pending",
        description="Attribution status: pending, confirmed, rejected, disputed"
    )
    # Relationships (will be populated via references)
    aliases: List[EntityReference] = Field(
        default_factory=list,
        description="Aliases used by this actor"
    )
    posts: List[EntityReference] = Field(
        default_factory=list,
        description="Posts authored by this actor"
    )
    pgp_keys: List[EntityReference] = Field(
        default_factory=list,
        description="PGP keys used by this actor"
    )
    wallets: List[EntityReference] = Field(
        default_factory=list,
        description="Cryptocurrency wallets used by this actor"
    )
    onion_services: List[EntityReference] = Field(
        default_factory=list,
        description="Onion services linked to this actor"
    )
    infrastructure: List[EntityReference] = Field(
        default_factory=list,
        description="Infrastructure used by this actor"
    )
    behaviour_profile: Optional[EntityReference] = Field(
        default=None,
        description="Behaviour profile of this actor"
    )
    stylometric_profile: Optional[EntityReference] = Field(
        default=None,
        description="Stylometric profile of this actor"
    )
    trust_relationships: List[EntityReference] = Field(
        default_factory=list,
        description="Trust relationships with other actors"
    )
    supported_by: List[EntityReference] = Field(
        default_factory=list,
        description="Infrastructure/services supporting this actor"
    )
    mentioned_in: List[EntityReference] = Field(
        default_factory=list,
        description="Posts mentioning this actor (reverse of posts)"
    )
    investigation: Optional[EntityReference] = Field(
        default=None,
        description="Investigation this actor belongs to"
    )
