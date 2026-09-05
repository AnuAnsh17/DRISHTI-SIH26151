"""
Unit tests for Wallet model.
"""

from datetime import datetime, timezone
from uuid import UUID
import pytest
from pydantic import ValidationError
from src.drishti.core.models.wallet import Wallet
from src.drishti.core.models.base import EntityReference


def test_wallet_creation():
    """Test that Wallet can be created with required fields."""
    wallet = Wallet(
        address="0x742d35Cc6634C0532925a3b8D4C0532950532950",
        blockchain="ethereum",
        source="test_source",
        source_type="web",
    )

    assert wallet.address == "0x742d35Cc6634C0532925a3b8D4C0532950532950"
    assert wallet.blockchain == "ethereum"
    assert wallet.source == "test_source"
    assert wallet.source_type == "web"
    assert isinstance(wallet.id, UUID)
    assert isinstance(wallet.created_at, datetime)
    assert wallet.actor is None  # default
    assert wallet.transactions == []  # default


def test_wallet_with_actor_reference():
    """Test Wallet with actor relationship."""
    actor_ref = EntityReference(
        id=UUID("33333333-3333-3333-3333-333333333333"),
        entity_type="Actor",
        relationship="OWNED_BY",
    )

    wallet = Wallet(
        address="0x742d35Cc6634C0532925a3b8D4C0532950532950",
        blockchain="ethereum",
        source="test_source",
        source_type="web",
        actor=actor_ref,
    )

    assert wallet.actor is not None
    assert wallet.actor.id == UUID("33333333-3333-3333-3333-333333333333")


def test_wallet_timestamps():
    """Test Wallet timestamp fields."""
    first_seen = datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    last_seen = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    wallet = Wallet(
        address="0x742d35Cc6634C0532925a3b8D4C0532950532950",
        blockchain="ethereum",
        source="test_source",
        source_type="web",
        first_seen=first_seen,
        last_seen=last_seen,
    )

    assert wallet.first_seen == first_seen
    assert wallet.last_seen == last_seen


def test_wallet_confidence_validation():
    """Test that Wallet confidence is validated."""
    # Valid confidence
    wallet = Wallet(
        address="0x742d35Cc6634C0532925a3b8D4C0532950532950",
        blockchain="ethereum",
        source="test",
        source_type="test",
        confidence=0.8,
    )
    assert wallet.confidence == 0.8

    # Invalid confidence
    with pytest.raises(ValidationError):
        Wallet(
            address="0x742d35Cc6634C0532925a3b8D4C0532950532950",
            blockchain="ethereum",
            source="test",
            source_type="test",
            confidence=1.5,
        )
