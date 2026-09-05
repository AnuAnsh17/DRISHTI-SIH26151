"""
Models for DRISHTI OSINT collection framework.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import Field, ConfigDict

from src.drishti.core.models.evidence import Evidence
from src.drishti.core.models.base import BaseEntity, ProvenanceMixin


class SourceType(Enum):
    """
    Controlled source categories suitable for DRISHTI.
    """

    SURFACE_WEB = "surface_web"
    PUBLIC_FORUM = "public_forum"
    PUBLIC_SOCIAL = "public_social"
    PUBLIC_REPOSITORY = "public_repository"
    PASTE_SOURCE = "paste_source"
    SECURITY_REPORT = "security_report"
    CERTIFICATE_TRANSPARENCY = "certificate_transparency"
    PASSIVE_DNS = "passive_dns"
    ONION_METADATA = "onion_metadata"
    SYNTHETIC = "synthetic"


class RawObservation(BaseEntity, ProvenanceMixin):
    """
    Represents an item obtained from an OSINT source before entity extraction.

    RawObservation maintains the link between collected data and its provenance,
    allowing the system to trace evidence back to its origin.
    """

    observation_id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for this observation"
    )
    source: str = Field(
        ...,
        description="Source name or identifier (e.g., 'Twitter', 'GitHub', 'CT logs')",
    )
    source_type: SourceType = Field(..., description="Type/platform of the source")
    observed_at: Optional[datetime] = Field(
        default=None,
        description="When the observed event occurred (if different from collection time)",
    )
    collected_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When the data was collected",
    )
    title: Optional[str] = Field(
        default=None, description="Title or identifier where applicable"
    )
    content: Optional[Any] = Field(
        default=None, description="Content or structured payload of the observation"
    )
    source_url: Optional[str] = Field(
        default=None,
        description="URL where the observation was obtained (if applicable)",
    )
    collection_method: str = Field(
        default="unknown", description="Method used to collect the observation"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional source-specific metadata"
    )
    reliability: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Source reliability score for this observation",
    )

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat(),
            UUID: str,
        }
    )

    def to_evidence(
        self, evidence_type: str, subject: str, object_value: Any
    ) -> Evidence:
        """
        Convert this RawObservation to an Evidence object.

        This method preserves provenance information when transforming
        raw observations into the canonical evidence model.

        Args:
            evidence_type: Type of evidence (e.g., 'alias_mention', 'post_content')
            subject: What the evidence is about
            object_value: The actual evidence value

        Returns:
            Evidence object with preserved provenance
        """
        # Preserve provenance fields from RawObservation
        provenance_data = {
            "source": self.source,
            "source_type": self.source_type,  # Already a string due to use_enum_values=True
            "collected_at": self.collected_at,
            "observation_timestamp": self.observed_at,
            "confidence": self.reliability,  # Use reliability as initial confidence
            "explanation": f"Collected via {self.collection_method} from {self.source}",
            "reference_id": str(self.observation_id),
        }

        evidence = Evidence(
            evidence_type=evidence_type,
            subject=subject,
            object_value=object_value,
            **provenance_data,
        )

        # Link back to this observation
        evidence.extracted_entities = []  # Will be populated during extraction

        return evidence
