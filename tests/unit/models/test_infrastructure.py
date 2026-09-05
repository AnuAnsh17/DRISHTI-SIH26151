"""
Unit tests for Infrastructure model.
"""
from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.infrastructure import Infrastructure
from src.drishti.core.models.base import EntityReference


def test_infrastructure_creation():
    """Test that Infrastructure can be created with required fields."""
    infra = Infrastructure(
        ip_address="203.0.113.45",
        infrastructure_type="ip",
        source="test_source",
        source_type="web"
    )
    
    assert infra.ip_address == "203.0.113.45"
    assert infra.infrastructure_type == "ip"
    assert infra.source == "test_source"
    assert infra.source_type == "web"
    assert isinstance(infra.id, UUID)
    assert isinstance(infra.created_at, datetime)
    assert infra.onion_services == []  # default
    assert infra.clearnet_domains == []  # default
    assert infra.actors == []  # default
    assert infra.posts == []  # default


def test_infrastructure_with_domain():
    """Test Infrastructure with domain."""
    infra = Infrastructure(
        domain="example.com",
        infrastructure_type="domain",
        source="test_source",
        source_type="dns"
    )
    
    assert infra.domain == "example.com"
    assert infra.infrastructure_type == "domain"
    assert infra.source == "test_source"
    assert infra.source_type == "dns"


def test_infrastructure_with_asn():
    """Test Infrastructure with ASN."""
    infra = Infrastructure(
        asn="AS13335",
        infrastructure_type="asn",
        source="test_source",
        source_type="bgp"
    )
    
    assert infra.asn == "AS13335"
    assert infra.infrastructure_type == "asn"
    assert infra.source == "test_source"
    assert infra.source_type == "bgp"


def test_infrastructure_with_certificate():
    """Test Infrastructure with SSL certificate."""
    infra = Infrastructure(
        ssl_certificate_fingerprint="sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcd",
        infrastructure_type="certificate",
        source="test_source",
        source_type="ssl"
    )
    
    assert infra.ssl_certificate_fingerprint == "sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcd"
    assert infra.infrastructure_type == "certificate"
    assert infra.source == "test_source"
    assert infra.source_type == "ssl"


def test_infrastructure_relationships():
    """Test Infrastructure with relationships."""
    actor_ref = EntityReference(
        id=UUID('99999999-9999-9999-9999-999999999999'),
        entity_type="Actor",
        relationship="USES"
    )
    onion_ref = EntityReference(
        id=UUID('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'),
        entity_type="OnionService",
        relationship="HOSTED_ON"
    )
    
    infra = Infrastructure(
        ip_address="203.0.113.45",
        infrastructure_type="ip",
        source="test_source",
        source_type="web",
        actors=[actor_ref],
        onion_services=[onion_ref]
    )
    
    assert len(infra.actors) == 1
    assert infra.actors[0].id == UUID('99999999-9999-9999-9999-999999999999')
    assert len(infra.onion_services) == 1
    assert infra.onion_services[0].id == UUID('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa')


def test_infrastructure_timestamps():
    """Test Infrastructure timestamp fields."""
    collected_at = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    observation_timestamp = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    infra = Infrastructure(
        ip_address="203.0.113.45",
        infrastructure_type="ip",
        source="test_source",
        source_type="web",
        collected_at=collected_at,
        observation_timestamp=observation_timestamp
    )

    assert infra.collected_at == collected_at
    assert infra.observation_timestamp == observation_timestamp


def test_infrastructure_confidence_validation():
    """Test that Infrastructure confidence is validated."""
    # Valid confidence
    infra = Infrastructure(
        ip_address="203.0.113.45",
        infrastructure_type="ip",
        source="test",
        source_type="test",
        confidence=0.8
    )
    assert infra.confidence == 0.8
    
    # Invalid confidence
    with pytest.raises(ValidationError):
        Infrastructure(
            ip_address="203.0.113.45",
            infrastructure_type="ip",
            source="test",
            source_type="test",
            confidence=1.5
        )
