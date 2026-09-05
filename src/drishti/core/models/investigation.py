"""
Investigation model for DRISHTI intelligence schema.
"""

from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from enum import Enum
from pydantic import Field
from .base import BaseEntity, EntityReference


class InvestigationStatus(str, Enum):
    """Status of an investigation."""

    OPEN = "open"
    CLOSED = "closed"
    ARCHIVED = "archived"


class Investigation(BaseEntity):
    """
    Investigation represents ongoing investigative work with timeline and notes.
    """

    title: str = Field(..., description="Investigation title/name")
    description: Optional[str] = Field(
        default=None, description="Detailed description of the investigation"
    )
    # Relationships
    actors: List[EntityReference] = Field(
        default_factory=list, description="Actors involved in this investigation"
    )
    posts: List[EntityReference] = Field(
        default_factory=list, description="Posts involved in this investigation"
    )
    evidence: List[UUID] = Field(
        default_factory=list, description="Evidence IDs in this investigation"
    )
    hypotheses: List[UUID] = Field(
        default_factory=list,
        description="Attribution hypothesis IDs in this investigation",
    )
    status: InvestigationStatus = Field(
        default=InvestigationStatus.OPEN,
        description="Investigation status: open, closed, archived",
    )
