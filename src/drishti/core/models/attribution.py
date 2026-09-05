"""
AttributionHypothesis model for DRISHTI intelligence schema.
"""

from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from pydantic import Field
from .base import BaseEntity, EntityReference


class AttributionHypothesis(BaseEntity):
    """
    AttributionHypothesis represents a proposed linkage between evidence
    and an actor/identity with confidence and evidence trail.
    """

    hypothesis_type: str = Field(..., description="Type of attribution hypothesis")
    subject: str = Field(
        ..., description="What is being attributed (alias, post, etc.)"
    )
    candidate_entities: List[EntityReference] = Field(
        ..., description="Potential entities being attributed to"
    )
    association_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Raw association score before confidence calibration",
    )
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Calibrated confidence in this hypothesis (0.0 to 1.0)",
    )
    supporting_evidence: List[UUID] = Field(
        default_factory=list, description="Evidence IDs supporting this hypothesis"
    )
    contradicting_evidence: List[UUID] = Field(
        default_factory=list, description="Evidence IDs contradicting this hypothesis"
    )
    explanation: Optional[str] = Field(
        default=None, description="Explanation of the hypothesis and evidence"
    )
    investigation: Optional[EntityReference] = Field(
        default=None, description="Investigation this hypothesis belongs to"
    )
