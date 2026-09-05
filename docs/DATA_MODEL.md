# Data Model and Intelligence Schema
## SIH26151 — Dark web threat actor de-anonymization

### Overview
This document defines the canonical intelligence schema for the SIH26151 platform. The model is designed to support evidence-driven attribution with explicit confidence scoring, provenance tracking, and temporal modeling.

### Core Design Principles

1. **Evidence-Centric**: Every assertion must be backed by evidence with traceable provenance
2. **Uncertainty-Aware**: Confidence scores and uncertainty intervals quantify belief strength
3. **Temporal Support**: Track when entities and relationships were valid
4. **Provenance-Tracked**: Record source, collection method, and reliability for all data
5. **Explainable**: Design allows tracing conclusions back to raw evidence
6. **Extensible**: Schema accommodates new entity types and relationship types as needed

### Entity Definitions

All entities share common properties:
- `id`: Unique identifier (UUID recommended)
- `created_at`: Timestamp when record was first created in system
- `updated_at`: Timestamp of last modification
- `confidence`: Overall confidence in entity existence/validity (0-1)
- `sources`: Array of source references contributing to this entity
- `provenance`: Metadata about how this entity was derived

#### Actor
Represents a threat actor, cybercriminal group, or individual behind malicious activities.

**Properties**:
- `first_seen`: Earliest timestamp associated with this actor
- `last_seen`: Most recent timestamp associated with this actor
- `canonical_name`: Primary name or identifier (if known)
- `description`: Free-form description of actor activities/motivations
- `attribution_status`: Enum [pending, confirmed, rejected, disputed]

**Relationships**:
- `ACTOR_USES_ALIAS` → Alias
- `ACTOR_POSTED` → Post
- `ACTOR_USES_PGP` → PGPKey
- `ACTOR_USES_WALLET` → Wallet
- `ACTOR_LINKED_TO_DOMAIN` → ClearnetDomain
- `ACTOR_LINKED_TO_SERVICE` → OnionService/ClearnetService
- `ACTOR_USES_INFRASTRUCTURE` → Infrastructure
- `ACTOR_HAS_BEHAVIOUR_PROFILE` → BehaviourProfile
- `ACTOR_HAS_STYLOMETRIC_PROFILE` → StylometricProfile
- `ACTOR_TRUSTS` → Actor (trust relationships)
- `ACTOR_SUPPORTED_BY` → Infrastructure/Service
- `ACTOR_MENTIONED_IN` → Post (reverse of Post mentions Actor)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Alias
Alternative names, handles, or identifiers used by an actor.

**Properties**:
- `value`: The actual alias text (handle, username, etc.)
- `type`: Enum [handle, username, email, nickname, callsign, etc.]
- `platform`: Platform or service where alias used (optional)
- `first_seen`: First observed usage
- `last_seen`: Most recent usage
- `case_sensitive`: Boolean indicating if case matters for matching

**Relationships**:
- `USED_BY` → Actor (reverse of ACTOR_USES_ALIAS)
- `MIGRATED_TO` → Alias (for evolution over time)
- `APPEARS_IN` → Post (mentions in content)
- `ASSOCIATED_WITH` → Wallet/PGPKey/Domain (direct associations)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Post
Individual piece of content (forum post, marketplace listing, message, etc.).

**Properties**:
- `content`: The actual text/content
- `content_hash`: Cryptographic hash (SHA-256) for deduplication
- `platform`: Service/platform where posted
- `url`: Direct URL or identifier (if available)
- `timestamp`: When posted/published
- `language`: Detected language (ISO 639-1 code)
- `length`: Character/word count
- `sentiment`: Optional sentiment analysis score
- `topics`: Array of detected topics/tags

**Relationships**:
- `POSTED_BY` → Actor (reverse of ACTOR_POSTED)
- `POSTED_ON` → Platform/Service node (or direct property)
- `MENTIONS` → Entity (Actor, Alias, Wallet, etc.)
- `MENTIONED_BY` → Entity (reverse of Post mentions Entity)
- `SIMILAR_TO` → Post (stylistic similarity)
- `REPLY_TO` → Post (conversation structure)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### OnionService
Tor hidden service.

**Properties**:
- `address`: .onion address
- `status`: Enum [active, inactive, unknown, deprecated]
- `first_seen`: First observed in Tor network
- `last_seen`: Most recent observation
- `title`: Service title from HTML (if available)
- `description`: Service description
- `service_type`: Enum [marketplace, forum, blog, service, etc.]
- `software`: Detected software/platform (if identifiable)
- `version`: Software version (if detectable)

**Relationships**:
- `HOSTED_ON` → Infrastructure (IP, ASN, hosting provider)
- `SHARES_CERTIFICATE_WITH` → ClearnetDomain (via SSL certificate)
- `SHARES_INFRASTRUCTURE_WITH` → OnionService/ClearnetDomain
- `RESOLVES_TO` → IPAddress (historical/current)
- `HAS_CERTIFICATE` → SSLCertificate
- `MENTIONED_IN` → Post
- `BELONGS_TO_INVESTIGATION` → Investigation

#### ClearnetDomain
Standard internet domain name.

**Properties**:
- `domain`: The domain name (e.g., example.com)
- `registrar`: Domain registrar (if available)
- `creation_date`: Registration date
- `expiration_date`: Expiration date
- `last_updated`: Last WHOIS update
- `status`: Enum [active, expired, pending, locked]
- `registrant_info`: Registrant contact information (if available)
- `name_servers`: Array of nameservers
- `mx_records`: Array of mail exchange records
- `txt_records`: Array of TXT records (SPF, DKIM, etc.)

**Relationships**:
- `RESOLVES_TO` → IPAddress (current)
- `HAS_HISTORICAL_IP` → IPAddress (historical resolutions)
- `USES_NAMESERVER` → Infrastructure (nameserver)
- `USES_MAIL_SERVER` → Infrastructure (mail server)
- `SHARES_CERTIFICATE_WITH` → OnionService (via SSL certificate)
- `SHARES_INFRASTRUCTURE_WITH` → ClearnetDomain/OnionService
- `MENTIONED_IN` → Post
- `BELONGS_TO_INVESTIGATION` → Investigation

#### IPAddress
Internet protocol address.

**Properties**:
- `address`: IP address string (IPv4 or IPv6)
- `version`: Enum [IPv4, IPv6]
- `asn`: Associated ASN number (if known)
- `organization`: Organization to which IP is allocated
- `geography`: Geographic information (country, city, with accuracy disclaimer)
- `hosting_provider`: Inferred hosting provider (if detectable)
- `first_seen`: First observed
- `last_seen`: Most recent observation
- `is_static`: Boolean indicating likelihood of static assignment
- `reputation_score`: Optional threat intelligence reputation

**Relationships**:
- `RESOLVED_FROM` → ClearnetDomain (reverse of domain resolves to IP)
- `ASSOCIATED_WITH` → ASN
- `LOCATED_IN` → Geography (if modeled separately)
- `PROVIDES_SERVICE` → OnionService/ClearnetService
- `USED_BY` → Actor (hosting actor infrastructure)
- `SHARES_NETWORK_WITH` → IPAddress (same subnet/allocation)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### ASN
Autonomous System Number.

**Properties**:
- `number`: ASN number
- `description`: ASN description
- `organization`: Owning organization
- `allocation_date`: Date of allocation
- `status`: Enum [allocated, reserved, deprecated]
- `peer_asns`: Array of peer ASN numbers (if known)
- `customer_asns`: Array of customer ASN numbers (if known)

**Relationships**:
- `ORIGINATES_FROM` → IPAddress (reverse of IP has ASN)
- `PEERS_WITH` → ASN
- `PROVIDES_TRANSIT_FOR` → ASN (customer relationships)
- `USED_BY` → Actor (network-level infrastructure)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### SSLCertificate
SSL/TLS certificate.

**Properties**:
- `fingerprint`: SHA-256 fingerprint (primary identifier)
- `sha1_fingerprint`: SHA-1 fingerprint (for compatibility)
- `md5_fingerprint`: MD5 fingerprint (non-security purposes)
- `issuer`: Certificate Authority
- `subject`: Certificate subject (DN string)
- `subject_alternative_names`: Array of SANs
- `validity_not_before`: Start of validity period
- `validity_not_after`: End of validity period
- `serial_number`: Certificate serial number
- `signature_algorithm`: Algorithm used for signature
- `key_algorithm`: Public key algorithm (RSA, ECDSA, etc.)
- `key_size`: Key size in bits
- `extensions`: Certificate extensions (parsed)
- `transparency_logged`: Boolean indicating presence in CT logs
- `first_seen`: First observed in CT logs or scans
- `last_seen`: Most recent observation

**Relationships**:
- `USED_BY` → OnionService/ClearnetService
- `ISSUED_BY` → Organization (CA)
- `BOUND_TO_DOMAIN` → ClearnetDomain (via SAN or CN)
- `SHARED_BY` → OnionService/ClearnetDomain (multiple services using same cert)
- `REVOKED_BY` → Certificate Revocation List (if modeled)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### PGPKey
PGP public key.

**Properties**:
- `fingerprint`: Key fingerprint (primary identifier)
- `key_id`: Short key ID (hex)
- `creation_date`: Key creation timestamp
- `expiration_date`: Key expiration timestamp (if set)
- `algorithm`: Public key algorithm (RSA, ECDSA, etc.)
- `key_size`: Key size in bits
- `user_ids`: Array of user ID strings
- `signatures`: Array of signature hashes (from other keys)
- `subkeys`: Array of subkey information
- `revocation_certificate`: Boolean indicating if revoked
- `first_seen`: First observed in key dumps or communications
- `last_seen`: Most recent observation
- `is_valid`: Boolean indicating current validity (not expired/revoked)

**Relationships**:
- `OWNED_BY` → Actor
- `USED_FOR_SIGNING` → Post/Message (digital signatures)
- `ENCRYPTED_FOR` → Actor (intended recipient)
- `SHARED_WITH` → PGPKey (cross-signing)
- `CERTIFIED_BY` → PGPKey (trusted introducer)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Wallet
Cryptocurrency wallet address.

**Properties**:
- `address`: Wallet address string
- `blockchain`: Enum [Bitcoin, Ethereum, Litecoin, etc.]
- `address_type`: Enum [legacy, nested_segwit, native_segwit, taproot, etc.]
- `first_seen`: First observed on blockchain
- `last_seen`: Most recent observation
- `balance`: Current balance (optional, requires node)
- `total_received`: Total amount received (optional)
- `total_sent`: Total amount sent (optional)
- `transaction_count`: Number of transactions (optional)
- `is_contract`: Boolean indicating if address is a smart contract
- `label`: Optional label from threat intelligence (exchange, mixer, etc.)
- `cluster_id`: Reference to wallet cluster (if clustered)

**Relationships**:
- `OWNED_BY` → Actor
- `SENT_TRANSACTION` → Transaction (outgoing)
- `RECEIVED_TRANSACTION` → Transaction (incoming)
- `PART_OF_CLUSTER` → WalletCluster (if modeled)
- `ASSOCIATED_WITH` → Exchange/Service (if labeled)
- `LINKED_TO` → Actor/Alias (direct attribution)
- `SIMILAR_TO` → Wallet (behavioral/temporal similarity)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Transaction
Blockchain transaction.

**Properties**:
- `hash`: Transaction hash (primary identifier)
- `blockchain`: Enum [Bitcoin, Ethereum, etc.]
- `block_height`: Block height where confirmed
- `block_timestamp`: Block timestamp
- `confirmation_count`: Number of confirmations
- `fee`: Transaction fee paid
- `size`: Transaction size in bytes
- `version`: Transaction version
- `locktime`: Transaction locktime
- `inputs`: Array of input references (tx_hash, output_index)
- `outputs`: Array of output details (address, amount, script_type)
- `status`: Enum [unconfirmed, confirmed, orphaned]

**Relationships**:
- `SPENT_BY` → Wallet (input spending)
- `CREATED_BY` → Wallet (output creation)
- `PART_OF_BLOCK` → Block
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Infrastructure
Generic infrastructure element (can be specialized via type).

**Properties**:
- `type`: Enum [ip_address, asn, nameserver, mail_server, hosting_provider, 
               CDN, proxy, VPN, server, service, etc.]
- `value`: The actual infrastructure value (hostname, IP, etc.)
- `provider`: Organization providing the infrastructure (if known)
- `geography`: Geographic location (with accuracy disclaimer)
- `first_seen`: First observed
- `last_seen`: Most recent observation
- `is_static`: Boolean indicating persistence likelihood
- `reputation_score`: Optional threat intelligence reputation
- `metadata`: Key-value pairs for type-specific attributes

**Relationships**:
- `USED_BY` → Actor (actor utilizes this infrastructure)
- `PROVIDES_SERVICE` → OnionService/ClearnetService
- `SHARED_WITH` → Infrastructure (same provider/type)
- `LOCATED_IN` → Geography (if modeled separately)
- `RESOLVES_FROM` → ClearnetDomain (reverse of domain resolves to infrastructure)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### BehaviourProfile
Results of behavioral analysis on an actor.

**Properties**:
- `feature_vector`: Array of numerical features representing behavior
- `model_version`: Version of behavioral model used
- `analysis_date`: When analysis was performed
- `confidence`: Confidence in this behavioral profile
- `feature_names`: Array describing each feature in vector
- `temporal_patterns`: Detected periodicities (if any)
- `activity_baseline`: Baseline activity level

**Relationships**:
- `DESCRIBES` → Actor
- `SIMILAR_TO` → BehaviourProfile (behavioral similarity)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### StylometricProfile
Results of stylometric analysis on text or actor.

**Properties**:
- `feature_vector`: Array of numerical features representing writing style
- `model_version`: Version of stylometric model used
- `analysis_date`: When analysis was performed
- `confidence`: Confidence in this stylometric profile
- `feature_names`: Array describing each feature in vector
- `text_sample_id`: Reference to analyzed text (if applicable)
- `language`: Language of analyzed text

**Relationships**:
- `DESCRIBES` → Actor/Post/Alias
- `SIMILAR_TO` → StylometricProfile (stylistic similarity)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Evidence
Piece of information supporting assertions.

**Properties**:
- `id`: Unique evidence identifier
- `type`: Enum [certificate_match, domain_match, ip_match, wallet_reuse, 
               pgp_key_match, stylometry_match, behavior_match, 
               infrastructure_correlation, post_content, etc.]
- `source`: Origin of evidence (collector name, API, manual, etc.)
- `source_reliability`: Reliability score of source (0-1)
- `collected_at`: When evidence was collected
- `observed_at`: When the evidenced phenomenon was observed
- `content_hash`: Hash of raw evidence content (for verification)
- `confidence`: Confidence in this evidence item (0-1)
- `entity_ids`: Array of entity IDs this evidence pertains to
- `relationship_ids`: Array of relationship IDs this evidence supports
- `deprecated_by`: Evidence ID that supersedes this (if any)
- `validation_status`: Enum [raw, validated, disputed, refuted]

**Relationships**:
- `SUPPORTS` → Entity/Relationship/Hypothesis
- `CONTRADICTS` → Entity/Relationship/Hypothesis
- `DERIVED_FROM` → Evidence (evidence transformation/chaining)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### AttributionHypothesis
Proposed attribution link to be evaluated.

**Properties**:
- `id`: Unique hypothesis identifier
- `actor_id`: Actor being attributed
- `target_entity_id`: Entity being attributed to (Actor, Alias, etc.)
- `hypothesis_type`: Enum [identity_link, alias_migration, infrastructure_link, 
                           wallet_association, pgp_key_sharing, etc.]
- `confidence`: Overall confidence in hypothesis (0-1)
- `status`: Enum [proposed, supported, disputed, refuted, confirmed]
- `first_seen`: Earliest evidence supporting hypothesis
- `last_seen`: Most recent evidence supporting hypothesis
- `strength_factors`: Array of factors increasing confidence
- `weakness_factors`: Array of factors decreasing confidence
- `alternative_explanations`: Array of competing explanations
- `falsifiability_conditions`: What evidence would refute this hypothesis

**Relationships**:
- `ABOUT` → Actor (subject actor)
- `ATTRIBUTES_TO` → Target entity
- `BASED_ON` → Evidence (supporting evidence)
- `CONTRADICTED_BY` → Evidence (contradicting evidence)
- `EVOLVES_TO` → AttributionHypothesis (updated version)
- `BELONGS_TO_INVESTIGATION` → Investigation

#### Investigation
Investigative effort or case.

**Properties**:
- `id`: Unique investigation identifier
- `title`: Investigative title
- `description`: Detailed description
- `start_date`: Investigation start time
- `end_date`: Investigation end time (null if ongoing)
- `lead_analyst`: Primary investigator
- `analyst_team`: Array of analyst identifiers
- `status`: Enum [open, active, paused, closed, archived]
- `priority`: Enum [low, medium, high, critical]
- `classification`: Classification level (if applicable)
- `keywords`: Array of investigative keywords/tags
- `findings_summary`: Summary of conclusions
- `recommendations`: Array of recommended actions

**Relationships**:
- `HAS_ACTOR` → Actor (investigation subject)
- `HAS_EVIDENCE` → Evidence (collected evidence)
- `HAS_HYPOTHESIS` → AttributionHypothesis (proposed links)
- `HAS_DOCUMENT` → Document (reports, notes, etc.)
- `CHILD_OF` → Investigation (sub-investigations)
- `PARENT_OF` → Investigation (parent investigations)

### Relationship Definitions

All relationships share common properties:
- `confidence`: Confidence in this specific relationship (0-1)
- `first_seen`: When relationship was first observed
- `last_seen`: When relationship was last observed
- `source`: Source of this relationship information
- `source_reliability`: Reliability of the source
- `evidence_id`: Reference to primary evidence supporting this relationship
- `provenance`: Metadata about how this relationship was derived

#### Directional Relationships (examples)
- `(Actor)-[ACTOR_USES_ALIAS {confidence: 0.95}]→(Alias)`
- `(Post)-[POSTED_ON {platform: "MarketplaceX"}]→(Service)`
- `(OnionService)-[SHARES_CERTIFICATE_WITH {confidence: 0.98}]→(ClearnetDomain)`
- `(Wallet)-[OWNED_BY {confidence: 0.8}]→(Actor)`
- `(Actor)-[STYLISTICALLY_SIMILAR {similarity_score: 0.85}]→(Actor)`

#### Bidirectional/Undirectional Relationships (modeled as two directional)
- `(Infrastructure)-[SHARED_WITH]→(Infrastructure)` (can be same type or different)
- `(Actor)-[TRUSTS]→(Actor)` (may not be symmetric)

### Temporal Modeling

#### Valid Time Intervals
- Entities and relationships store `first_seen` and `last_seen` timestamps
- Enables point-in-time queries: "What was known about actor X on date T?"
- Supports temporal range queries: "Show all relationships active during 2024"
- Allows for entity and relationship evolution over time
- Supports retroactive analysis as new evidence arrives

#### Temporal Queries Examples
```cypher
// Find actor aliases active in 2024
MATCH (a:Actor)-[r:ACTOR_USES_ALIAS]->(al:Alias)
WHERE r.first_seen <= date('2024-12-31') AND r.last_seen >= date('2024-01-01')
RETURN a.id AS actor, al.value AS alias, r.confidence AS confidence

// Find infrastructure changes for an onion service over time
MATCH (os:OnionService)-[r:HOSTED_ON]->(ip:IPAddress)
WHERE os.address = 'abcdef123456.onion'
RETURN os.address AS service, r.first_seen AS from, r.last_seen AS to, 
       ip.address AS ip_address, r.confidence AS confidence
ORDER BY r.first_seen

// Find all posts by an actor during a specific investigation
MATCH (inv:Investigation {id: 'inv_001'})<-[:BELONGS_TO_INVESTIGATION]-(a:Actor)-[p:ACTOR_POSTED]->(po:Post)
WHERE p.first_seen <= inv.end_date AND p.last_seen >= inv.start_date
RETURN po.content AS post_content, po.timestamp AS post_time
```

### Evidence Model

#### Evidence Properties Detail
- **Source Reliability**: 
  - 0.9-1.0: Authorized API access, law enforcement seizure, verified disclosure
  - 0.7-0.9: Reputable threat intelligence, academic publication, verified bug bounty
  - 0.5-0.7: Security researcher blog, moderated forum, reputable news
  - 0.3-0.5: Anonymous source, unmoderated forum, unverified social media
  - 0.0-0.3: Unverified claim, rumor, known unreliable source

- **Evidence Confidence Factors**:
  - Directness: How directly evidence links to hypothesis (direct/circumstantial)
  - Independence: Degree of independence from other evidence
  - Specificity: How uniquely evidence points to particular hypothesis
  - Temporal Consistency: Alignment with hypothesized activity period
  - Corroboration: Number of independent sources supporting same conclusion
  - Contradiction: Evidence challenging the hypothesis

#### Evidence Types
- `certificate_match`: SSL certificate sharing between services
- `domain_match`: Domain registration or resolution correlation
- `ip_match`: IP address or netblock sharing
- `wallet_reuse`: Cryptocurrency wallet address reuse
- `pgp_key_match`: PGP key fingerprint or key sharing
- `stylometry_match`: Writing style similarity above threshold
- `behavior_match`: Behavioral pattern similarity above threshold
- `infrastructure_correlation`: Shared infrastructure beyond basic correlation
- `post_content`: Textual content mentioning entities
- `transaction_link`: Blockchain transaction linking wallets
- `social_link`: Communication or interaction evidence
- `technical_signature`: Malware, tool, or technique signature
- `financial_flow`: Money flow analysis beyond simple wallet reuse
- `operational_pattern`: Timing, frequency, or operational behavior
- `geographic_correlation`: Geographic location evidence
- `linguistic_feature`: Language, dialect, or writing patterns
- `temporal_pattern`: Timing patterns (circadian, response latency, etc.)
- `reputation_score`: Threat intelligence reputation or scoring
- `manual_analysis`: Investigator-derived conclusion
- `synthetic_data`: Evidence from synthetic dataset (for testing/validation)

### Schema Implementation Notes

#### Storage Considerations
- **Primary Storage**: Graph database (Neo4j) for entities and relationships
- **Evidence Storage**: Can be stored as nodes in graph or in document store
- **Indexes**: 
  - Entity ID lookups
  - Timestamp ranges for temporal queries
  - Type-based filters (entity_type, relationship_type)
  - Confidence thresholds for filtering
  - Source reliability filters
  - Full-text search for content fields

#### Validation Rules
- Timestamps: `last_seen` >= `first_seen`
- Confidence scores: 0.0 <= value <= 1.0
- Source reliability: 0.0 <= value <= 1.0
- Required fields: id, created_at, entity_type-specific required fields
- Relationships: must connect valid entity types
- Evidence: must reference valid entities/relationships when applicable

#### Evolution and Versioning
- Schema changes should be backward compatible when possible
- Breaking changes require migration scripts
- Entity and relationship versions can be tracked via `model_version` or similar
- Major version increments for significant schema changes
- Minor version increments for backward-compatible additions
- Patch version increments for bug fixes and minor adjustments

### Usage Examples

#### Creating an Actor with Alias
```
// Create actor
CREATE (a:Actor {
  id: "actor_001",
  created_at: datetime(),
  updated_at: datetime(),
  confidence: 0.9,
  first_seen: date('2024-01-15'),
  last_seen: date('2024-08-20'),
  description: "Suspected ransomware operator"
})

// Create alias
CREATE (al:Alias {
  id: "alias_001",
  created_at: datetime(),
  updated_at: datetime(),
  confidence: 0.95,
  value: "QuantumBreaker",
  type: "handle",
  first_seen: date('2024-02-01'),
  last_seen: date('2024-08-15')
})

// Create relationship
CREATE (a)-[r:ACTOR_USES_ALIAS {
  confidence: 0.95,
  first_seen: date('2024-02-01'),
  last_seen: date('2024-08-15'),
  source: "web_scraper",
  source_reliability: 0.8,
  evidence_id: "ev_001"
}]->(al)
```

#### Querying Temporal Relationships
```
// Find all infrastructure used by actor during July 2024
MATCH (a:Actor {id: "actor_001"})-[r:USES_INFRASTRUCTURE]->(i:Infrastructure)
WHERE r.first_seen <= date('2024-07-31') AND r.last_seen >= date('2024-07-01')
RETURN i.type AS infra_type, i.value AS infra_value, 
       r.confidence AS confidence, r.first_seen AS start, r.last_seen AS end
ORDER BY r.first_seen
```

#### Combining Evidence for Attribution
```
// Find posts with similar writing style to suspect
MATCH (p1:Post {id: "post_suspect"})-[:STYLISTICALLY_SIMILAR {similarity_score: $min_sim}]->(p2:Post)
WHERE p1.posted_by = "actor_001"
WITH collect(p2) AS similar_posts
// Check if similar posts mention same wallet
MATCH (p:Post)-[:MENTIONS]->(w:Wallet)
WHERE p IN similar_posts
WITH w, count(p) AS mention_count
WHERE mention_count >= $min_mentions
// Check if wallet has transaction patterns matching actor behavior
MATCH (a:Actor {id: "actor_001"})-[:USES_WALLET]->(w)
RETURN w.address AS wallet, 
       size(similar_posts) AS similar_post_count,
       mention_count AS wallet_mentions
```

### Data Quality and Integrity

#### Constraints
- No circular relationships that create logical impossibilities
- Confidence scores must be between 0 and 1 inclusive
- Timestamps must be valid and follow chronological constraints
- Entity references in relationships must point to existing entities
- Evidence must have valid source and type identifiers

#### Quality Assurance
- Automated validation during data ingestion
- Periodic consistency checks for temporal relationships
- Confidence score calibration against known ground truth
- Provenance tracking for auditability
- Regular schema validation against actual data

### Extensibility Guidelines

#### Adding New Entity Types
1. Define entity properties and required fields
2. Specify possible relationship types to/from other entities
3. Determine if temporal modeling is needed
4. Add to investigation relationship possibilities
5. Update documentation and validation rules

#### Adding New Relationship Types
1. Define source and target entity types
2. Specify directional or bidirectional nature
3. Define relationship-specific properties
4. Determine confidence scoring methodology
5. Add temporal support if needed
6. Update documentation

#### Adding New Evidence Types
1. Define evidence type identifier
2. Specify what entities/relationships it supports
3. Define evidence-specific properties
4. Establish confidence scoring methodology
5. Define source reliability guidelines
6. Add to investigator workflow if applicable

### Conclusion
This data model provides a comprehensive, evidence-driven framework for dark web threat actor attribution. It supports the required functionality of continuous collection, infrastructure analysis, cross-platform mapping, AI-based profiling, analytical frontend, autonomous mode, and export capabilities while ensuring explainability, uncertainty quantification, and temporal awareness. The model is designed to be extensible and adaptable to evolving understanding of threat actor behaviors and techniques.