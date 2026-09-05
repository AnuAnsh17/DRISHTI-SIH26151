"""
Synthetic collector for DRISHTI OSINT collection framework.

Generates realistic but clearly synthetic observations for development and testing.
"""

import hashlib
import hmac
import logging
import random
from datetime import datetime, timedelta
from typing import List, Optional
from uuid import UUID, uuid4

from ..base import CollectorInterface, CollectionError
from ..models import RawObservation, SourceType

logger = logging.getLogger(__name__)


class SyntheticCollector(CollectorInterface):
    """
    Synthetic data collector for DRISHTI.

    Generates realistic but clearly synthetic observations containing combinations of:
    - usernames/handles
    - PGP fingerprints
    - wallet identifiers
    - onion-service references
    - clearnet domains
    - timestamps
    - posts/messages
    - infrastructure metadata
    - behavioural metadata

    The generator is deterministic when supplied with a seed.
    """

    def __init__(self, seed: Optional[int] = None):
        """
        Initialize the synthetic collector.

        Args:
            seed: Optional seed for deterministic generation
        """
        super().__init__(
            source_name="Synthetic Data Generator",
            source_type=SourceType.SYNTHETIC,
            reliability=0.9,  # High reliability for synthetic data in controlled environments
        )
        self.seed = seed
        if seed is not None:
            random.seed(seed)

        # Synthetic data templates
        self._usernames = [
            "cyberphantom",
            "darkoperator",
            "nullpointer",
            "rootkit",
            "shadowbroker",
            "ghostinwire",
            "blackhat",
            "whitehat",
            "greyninja",
            "darktracer",
            "onionlover",
            "deepwebsurfer",
        ]

        self._domains = [
            "example.com",
            "testdomain.org",
            "fakewebsite.net",
            "syntheticsite.com",
            "demodomain.io",
        ]

        self._onion_services = [
            "abcdefghijklmnop.onion",
            "qrstuvwxyz123456.onion",
            "onionservice789test.onion",
            "syntheticonion123.onion",
        ]

        self._pgp_fingerprints = [
            "ABCDEF1234567890ABCDEF1234567890ABCDEF12",
            "8901EFGH4567IJKL8901EFGH4567IJKL8901EFGH",
            "MNOP3456QRST7890UVWX3456QRST7890UVWX34",
        ]

        self._wallet_addresses = [
            "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",  # Bitcoin example
            "0x742d35Cc6634C0532925a3b8D4C0532950532950",  # Ethereum example
            "tb1qw508d6qextdTL9fcek5H0x8za79z9u9e3yd5f0",  # Bitcoin Bech32 example
        ]

        self._post_templates = [
            "Just discovered a new vulnerability in {} - details soon",
            "Sharing some interesting findings about {} from my research",
            "Looking for collaborators on {} project. DM if interested",
            "Updated my {} repository with new features and fixes",
            "Anyone have experience with {}? Need some guidance",
            "Breaking: New {} technique discovered in underground forums",
            "Just released version 2.0 of my {} tool - check it out!",
            "Seeking feedback on my {} methodology for threat intelligence",
        ]

        self._infrastructure_types = [
            "web_server",
            "mail_server",
            "dns_server",
            "database_server",
        ]

    def collect(self, count: int = 10, **kwargs) -> List[RawObservation]:
        """
        Generate synthetic observations.

        Args:
            count: Number of observations to generate
            **kwargs: Additional parameters (ignored for synthetic collector)

        Returns:
            List of synthetic RawObservation objects
        """
        observations = []

        for i in range(count):
            try:
                observation = self._generate_observation(i)
                observations.append(observation)
            except Exception as e:
                logger.warning(f"Failed to generate synthetic observation {i}: {e}")
                # Continue generating other observations

        return observations

    def _generate_observation(self, index: int) -> RawObservation:
        """
        Generate a single synthetic observation.

        Args:
            index: Observation index (used for deterministic generation)

        Returns:
            Synthetic RawObservation object
        """
        # Use index to seed deterministic generation if needed
        if self.seed is not None:
            # Create deterministic variation based on seed and index
            combined_seed = hash(f"{self.seed}:{index}")
            random.seed(combined_seed)

        # Randomly select observation type
        obs_type = random.choice(["post", "infrastructure", "credential", "domain"])

        if obs_type == "post":
            return self._generate_post_observation(index)
        elif obs_type == "infrastructure":
            return self._generate_infrastructure_observation(index)
        elif obs_type == "credential":
            return self._generate_credential_observation(index)
        else:  # domain
            return self._generate_domain_observation(index)

    def _generate_post_observation(self, index: int) -> RawObservation:
        """Generate a synthetic social media/post observation."""
        username = random.choice(self._usernames)
        template = random.choice(self._post_templates)

        # Fill template with random data
        filler = random.choice(self._domains + self._onion_services[:2])
        content = template.format(filler)

        # Generate timestamp (within last 30 days) - deterministic based on seed
        days_ago = random.randrange(30)
        hours_ago = random.randrange(24)
        # Use a fixed base time for determinism, then subtract the random offset
        base_time = datetime(2026, 1, 1, tzinfo=timezone.utc)
        observed_at = base_time + timedelta(days=days_ago, hours=hours_ago)

        return RawObservation(
            source=f"synthetic_{random.choice(['twitter', 'reddit', 'github', 'forum'])}",
            source_type=SourceType.PUBLIC_SOCIAL,
            observed_at=observed_at,
            title=f"Post by {username}",
            content=content,
            source_url=f"https://synthetic.platform/{username}/post/{random.randrange(1000000)}",
            collection_method="api_simulation",
            reliability=self.reliability,
            metadata={
                "username": username,
                "platform": "synthetic_social",
                "post_type": random.choice(["original", "reply", "retweet"]),
                "engagement": {
                    "likes": random.randrange(1000),
                    "shares": random.randrange(100),
                    "comments": random.randrange(50),
                },
            },
        )

    def _generate_infrastructure_observation(self, index: int) -> RawObservation:
        """Generate a synthetic infrastructure observation."""
        infra_type = random.choice(self._infrastructure_types)
        domain = random.choice(self._domains)

        # Generate synthetic SSL certificate-like data
        cert_data = self._generate_synthetic_cert_data()

        return RawObservation(
            source="synthetic_certificate_transparency",
            source_type=SourceType.CERTIFICATE_TRANSPARENCY,
            title=f"SSL Certificate for {domain}",
            content=cert_data,
            source_url=f"https://ct.synthetic.example/log/{random.randbytes(8).hex()}",
            collection_method="ct_log_monitoring",
            reliability=self.reliability,
            metadata={
                "domain": domain,
                "infrastructure_type": infra_type,
                "certificate": cert_data,
                "ip_address": f"{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}",
                "asn": f"AS{random.randrange(99999)}",
                "issuer": "Let's Encrypt Synthetic Authority",
            },
        )

    def _generate_credential_observation(self, index: int) -> RawObservation:
        """Generate a synthetic credential observation."""
        cred_type = random.choice(["pgp_key", "wallet", "password"])

        if cred_type == "pgp_key":
            fingerprint = random.choice(self._pgp_fingerprints)
            return RawObservation(
                source="synthetic_keybase",
                source_type=SourceType.PUBLIC_REPOSITORY,
                title=f"PGP Key: {fingerprint[:16]}...",
                content=f"-----BEGIN PGP PUBLIC KEY BLOCK-----\n{synthetic_pgp_key()}\n-----END PGP PUBLIC KEY BLOCK-----",
                source_url=f"https://keybase.io/syntheticuser/key/{fingerprint}",
                collection_method="api_fetch",
                reliability=self.reliability,
                metadata={
                    "fingerprint": fingerprint,
                    "key_id": fingerprint[-8:],
                    "username": f"syntheticuser{random.randrange(1000)}",
                    "key_type": "RSA",
                    "key_length": 4096,
                },
            )
        elif cred_type == "wallet":
            address = random.choice(self._wallet_addresses)
            return RawObservation(
                source="synthetic_blockchain_explorer",
                source_type=SourceType.PUBLIC_REPOSITORY,
                title=f"Wallet Address: {address[:16]}...",
                content=f"Blockchain wallet with balance: {random.randrange(10)} BTC",
                source_url=f"https://blockchain.synthetic.example/address/{address}",
                collection_method="blockchain_exploration",
                reliability=self.reliability,
                metadata={
                    "address": address,
                    "currency": "BTC",
                    "balance": random.randrange(100) / 10.0,
                    "transaction_count": random.randrange(50),
                },
            )
        else:  # password
            return RawObservation(
                source="synthetic_paste_site",
                source_type=SourceType.PASTE_SOURCE,
                title="Password List Leak",
                content=self._generate_synthetic_password_list(),
                source_url=f"https://paste.synthetic.example/{random.randbytes(4).hex()}",
                collection_method="paste_monitoring",
                reliability=self.reliability,
                metadata={
                    "paste_type": "credentials",
                    "estimated_count": random.randrange(100) + 10,
                    "source_mention": "security breach",
                },
            )

    def _generate_domain_observation(self, index: int) -> RawObservation:
        """Generate a synthetic domain/Passive DNS observation."""
        domain = random.choice(self._domains)
        onion_service = random.choice(self._onion_services)

        return RawObservation(
            source="synthetic_passive_dns",
            source_type=SourceType.PASSIVE_DNS,
            title=f"DNS Record: {domain}",
            content=f"A record: {domain} -> {random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}",
            source_url=f"https://dns.synthetic.example/query/{domain}",
            collection_method="dns_query",
            reliability=self.reliability,
            metadata={
                "domain": domain,
                "record_type": random.choice(["A", "AAAA", "CNAME", "MX", "TXT"]),
                "ip_address": f"{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}",
                "ttl": random.choice([300, 900, 1800, 3600, 7200]),
                "associated_onion": (
                    random.choice([None, onion_service])
                    if random.randrange(2) == 0
                    else None
                ),
            },
        )

    def _generate_synthetic_cert_data(self) -> dict:
        """Generate synthetic SSL certificate data."""
        # Use deterministic timing based on a fixed base date
        base_time = datetime(2026, 1, 1, tzinfo=timezone.utc)
        not_before = base_time + timedelta(days=30)  # 30 days after base
        not_after = base_time + timedelta(days=365)  # 365 days after base

        return {
            "subject": f"CN={random.choice(self._domains)}",
            "issuer": "Let's Encrypt Synthetic Authority X3",
            "serial_number": f"{random.randrange(10**16):016x}",
            "not_before": not_before.isoformat(),
            "not_after": not_after.isoformat(),
            "signature_algorithm": "SHA256-RSA",
            "public_key_algorithm": "RSA",
            "public_key_size": 2048,
        }

    def _generate_synthetic_password_list(self) -> str:
        """Generate a synthetic password list for paste sites."""
        passwords = [
            "password123",
            "admin123",
            "letmein",
            "qwerty123",
            "welcome123",
            "monkey123",
            "sunshine123",
            "iloveyou123",
        ]

        k = random.randrange(5) + 3
        selected = random.sample(passwords, k=k)
        return "\n".join([f"user{i}:{pwd}" for i, pwd in enumerate(selected)])


def synthetic_pgp_key() -> str:
    """Generate a synthetic PGP key block (simplified)."""
    return f"""mQENBF{synthetic_hex(16)}BCAD{synthetic_hex(8)}EE{synthetic_hex(4)}
{synthetic_hex(16)} ={synthetic_hex(8)}
=synthetic
-----END PGP PUBLIC KEY BLOCK-----"""


def synthetic_hex(length: int) -> str:
    """Generate synthetic hex string of specified length."""
    return random.randbytes(length // 2).hex()


# Import timezone at module level to avoid circular imports
from datetime import timezone
