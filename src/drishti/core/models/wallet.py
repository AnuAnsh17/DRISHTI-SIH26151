"""
Wallet model for DRISHTI intelligence schema.
"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, ProvenanceMixin, EntityReference


class Wallet(BaseEntity, ProvenanceMixin):
    """
    Wallet represents a cryptocurrency wallet address.
    """

    address: str = Field(..., description="Wallet address")
    blockchain: str = Field(..., description="Blockchain (e.g., bitcoin, ethereum)")
    first_seen: Optional[datetime] = Field(
        default=None, description="First time this wallet was observed"
    )
    last_seen: Optional[datetime] = Field(
        default=None, description="Last time this wallet was observed"
    )
    # Relationships
    actor: Optional[EntityReference] = Field(
        default=None, description="Actor that owns this wallet"
    )
    transactions: List[EntityReference] = Field(
        default_factory=list, description="Transactions involving this wallet"
    )
