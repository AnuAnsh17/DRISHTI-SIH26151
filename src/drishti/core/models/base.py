"""
Base models for DRISHTI intelligence schema.
"""

from datetime import datetime, timezone
from typing import Optional, List, Any
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict


class BaseEntity(BaseModel):
    """
    Base entity with common properties for all intelligence objects.

    All entities share:
    - id: Unique identifier (UUID recommended)
    - created_at: Timestamp when record was first created in system
    - updated_at: Timestamp of last modification
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True,
    )

    id: UUID = Field(default_factory=uuid4, description="Unique identifier")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when record was first created in system",
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Timestamp of last modification"
    )


class ProvenanceMixin(BaseModel):
    """
    Mixin for provenance tracking.

    Provenance metadata about how this entity was derived.
    """

    source: str = Field(..., description="Source of the data")
    source_type: str = Field(..., description="Type/platform of the source")
    collected_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When the data was collected",
    )
    observation_timestamp: Optional[datetime] = Field(
        default=None, description="When the observed event occurred"
    )
    confidence: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Confidence in the data (0.0 to 1.0)"
    )
    explanation: Optional[str] = Field(
        default=None, description="Explanation of the data or confidence"
    )
    reference_id: Optional[str] = Field(
        default=None, description="Original/reference identifier from source"
    )


class EntityReference(BaseModel):
    """Reference to another entity."""

    id: UUID = Field(..., description="Entity ID")
    entity_type: str = Field(..., description="Type of entity")
    relationship: str = Field(..., description="Nature of the relationship")
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence in this relationship"
    )
