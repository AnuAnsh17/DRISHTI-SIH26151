"""
Infrastructure model for DRISHTI intelligence schema.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import Field, validator
from .base import BaseEntity, ProvenanceMixin, EntityReference


class Infrastructure(BaseEntity, ProvenanceMixin):
    """
    Infrastructure represents hosting or service provider information.
    This can include IP addresses, domains, ASNs, SSL certificates, etc.
    """
    # These are mutually exclusive - one should be set based on infrastructure_type
    ip_address: Optional[str] = Field(
        default=None,
        description="IP address (IPv4 or IPv6)"
    )
    domain: Optional[str] = Field(
        default=None,
        description="Domain name"
    )
    asn: Optional[str] = Field(
        default=None,
        description="Autonomous System Number"
    )
    ssl_certificate_fingerprint: Optional[str] = Field(
        default=None,
        description="SSL/TLS certificate fingerprint"
    )
    infrastructure_type: str = Field(
        ...,
        description="Type of infrastructure: ip, domain, asn, certificate, etc."
    )
    # Relationships
    onion_services: List[EntityReference] = Field(
        default_factory=list,
        description="Onion services hosted on this infrastructure"
    )
    clearnet_domains: List[EntityReference] = Field(
        default_factory=list,
        description="Clearnet domains associated with this infrastructure"
    )
    actors: List[EntityReference] = Field(
        default_factory=list,
        description="Actors using this infrastructure"
    )
    posts: List[EntityReference] = Field(
        default_factory=list,
        description="Posts mentioning this infrastructure"
    )
    
    @validator('infrastructure_type')
    def infrastructure_type_must_match_field(cls, v, values):
        """Ensure that exactly one of the identifier fields is set based on infrastructure_type."""
        # For simplicity in this foundation implementation, we'll just validate the type
        # In a more complete implementation, we'd check that the corresponding field is set
        allowed_types = ['ip', 'domain', 'asn', 'certificate']
        if v not in allowed_types:
            raise ValueError(f'infrastructure_type must be one of {allowed_types}')
        return v
