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
        default=None, description="IP address (IPv4 or IPv6)"
    )
    domain: Optional[str] = Field(default=None, description="Domain name")
    asn: Optional[str] = Field(default=None, description="Autonomous System Number")
    ssl_certificate_fingerprint: Optional[str] = Field(
        default=None, description="SSL/TLS certificate fingerprint"
    )
    infrastructure_type: str = Field(
        ..., description="Type of infrastructure: ip, domain, asn, certificate, etc."
    )
    # Relationships
    onion_services: List[EntityReference] = Field(
        default_factory=list, description="Onion services hosted on this infrastructure"
    )
    clearnet_domains: List[EntityReference] = Field(
        default_factory=list,
        description="Clearnet domains associated with this infrastructure",
    )
    actors: List[EntityReference] = Field(
        default_factory=list, description="Actors using this infrastructure"
    )
    posts: List[EntityReference] = Field(
        default_factory=list, description="Posts mentioning this infrastructure"
    )

    @validator("infrastructure_type")
    def infrastructure_type_must_match_field(cls, v, values):
        """Ensure that exactly one of the identifier fields is set based on infrastructure_type."""
        allowed_types = ["ip", "domain", "asn", "certificate"]
        if v not in allowed_types:
            raise ValueError(f"infrastructure_type must be one of {allowed_types}")

        # Check that the corresponding field is set
        if v == "ip" and not values.get("ip_address"):
            raise ValueError(
                'ip_address must be provided when infrastructure_type is "ip"'
            )
        if v == "domain" and not values.get("domain"):
            raise ValueError(
                'domain must be provided when infrastructure_type is "domain"'
            )
        if v == "asn" and not values.get("asn"):
            raise ValueError('asn must be provided when infrastructure_type is "asn"')
        if v == "certificate" and not values.get("ssl_certificate_fingerprint"):
            raise ValueError(
                'ssl_certificate_fingerprint must be provided when infrastructure_type is "certificate"'
            )

        # Ensure only one identifier field is set
        ip_set = bool(values.get("ip_address"))
        domain_set = bool(values.get("domain"))
        asn_set = bool(values.get("asn"))
        cert_set = bool(values.get("ssl_certificate_fingerprint"))

        if v == "ip" and not (
            ip_set and not domain_set and not asn_set and not cert_set
        ):
            raise ValueError(
                'When infrastructure_type is "ip", only ip_address should be set'
            )
        if v == "domain" and not (
            domain_set and not ip_set and not asn_set and not cert_set
        ):
            raise ValueError(
                'When infrastructure_type is "domain", only domain should be set'
            )
        if v == "asn" and not (
            asn_set and not ip_set and not domain_set and not cert_set
        ):
            raise ValueError(
                'When infrastructure_type is "asn", only asn should be set'
            )
        if v == "certificate" and not (
            cert_set and not ip_set and not domain_set and not asn_set
        ):
            raise ValueError(
                'When infrastructure_type is "certificate", only ssl_certificate_fingerprint should be set'
            )

        return v
