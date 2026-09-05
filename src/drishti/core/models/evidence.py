"""
Evidence model for DRISHTI intelligence schema.
"""

from datetime import datetime, timezone
from typing import List, Any, Optional
from uuid import UUID
from pydantic import Field, ConfigDict
from .base import BaseEntity, ProvenanceMixin


class Evidence(BaseEntity, ProvenanceMixin):
    """
    Evidence represents a raw data item with provenance and reliability.

    Evidence is the foundation of all attribution in DRISHTI.
    """

    evidence_type: str = Field(..., description="Type of evidence")
    subject: str = Field(..., description="What the evidence is about")
    object_value: Any = Field(..., description="The actual evidence value")
    extracted_entities: List[UUID] = Field(
        default_factory=list,
        description="References to entities extracted from this evidence",
    )

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat(),
            UUID: str,
        }
    )
