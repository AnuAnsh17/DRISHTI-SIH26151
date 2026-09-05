# Synthetic Dark Web Lab - Ground Truth
## SIH26151 — Dark web threat actor de-anonymization

## Overview
This document defines the ground truth relationships and attributes for the synthetic dark web ecosystem used to evaluate the SIH26151 platform. All entities, relationships, and events are intentionally designed with known characteristics to enable objective validation of system performance.

## Actors

### Actor Alpha
**True Identity**: Security researcher "Dr. Alex Smith" (fictional)
**Activity Period**: January 2024 - Present
**Primary Motivation**: Financial gain through illicit services
**Operational Security Level**: Moderate (some OPSEC mistakes)

#### Aliases
- "QuantumBreaker" (handle) - Used on Marketplace A, Forum C
- "SigmaCoder" (handle) - Used on Marketplace B, Onion Service D
- "alex.s@protonmail.com" (email) - Used for service registrations
- "0x742d35Cc6634C0532925a3b8D4C0532950532950" (Bitcoin wallet) - Primary wallet

#### Writing Style Characteristics
- Prefers technical terminology
- Uses formal grammar with occasional slang
- Average sentence length: 22 words
- Frequent use of parentheses for clarification
- Consistent spelling of "definitely" (not "definately")

#### Infrastructure
- Onion Service D hosted on IP 203.0.113.45 (ASN 13335 - CLOUDFLARENET)
- Clearnet Site E resolves to IP 203.0.113.46 (ASN 13335 - CLOUDFLARENET)
- SSL certificate fingerprint: sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- PGP key fingerprint: sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

#### Wallet Activity
- Primary wallet: 0x742d35Cc6634C0532925a3b8D4C0532950532950
- Received 2.5 BTC between Jan-Aug 2024
- Sent 1.8 BTC to known exchange addresses
- Transaction pattern: Regular weekly withdrawals

#### Relationships
- Trusts Actor Bravo (mutual trust score: 0.7)
- Mentions Actor Charlie in 3 forum posts (negative context)
- Supported by Infrastructure X (hosting provider)

### Actor Bravo
**True Identity**: Former IT contractor "Jordan Lee" (fictional)
**Activity Period**: March 2024 - Present
**Primary Motivation**: Ideological (hacktivism) with financial secondary
**Operational Security Level**: High (strong OPSEC practices)

#### Aliases
- "NetGhost" (handle) - Used on Marketplace B, Forum C
- "DigitalPhantom" (handle) - Used on Onion Service D
- "jordan.lee@tutanota.com" (email) - Used for service registrations
- "0x8ba1f109551bD432803012645Ac136ddd64DBA72d" (Bitcoin wallet) - Primary wallet

#### Writing Style Characteristics
- Concise, direct language
- Minimal use of adjectives
- Average sentence length: 16 words
- Frequent use of technical acronyms without explanation
- Consistent lowercase usage (deliberate stylistic choice)

#### Infrastructure
- Onion Service D shares hosting with Actor Alpha (same IP range)
- Marketplace B hosted on IP 198.51.100.22 (ASN 14061 - DIGITALOCEAN-ASN)
- SSL certificate fingerprint: sha256:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
- PGP key fingerprint: sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

#### Wallet Activity
- Primary wallet: 0x8ba1f109551bD432803012645Ac136ddd64DBA72d
- Received 0.8 BTC between Mar-Aug 2024
- Sent 0.6 BTC to mixing service
- Transaction pattern: Irregular, burst activity

#### Relationships
- Trusts Actor Alpha (mutual trust score: 0.7)
- No known relationship with Actor Charlie
- Uses Infrastructure Y (VPS provider)

### Actor Charlie
**True Identity**: Organized crime member "Carlos Mendoza" (fictional)
**Activity Period**: January 2024 - May 2024 (migrated June 2024)
**Primary Motivation**: Financial gain through ransomware
**Operational Security Level**: Low (frequent OPSEC mistakes)

#### Aliases (Pre-Migration)
- "RansomLord" (handle) - Used on Marketplace A, Forum C
- "CryptoKing" (handle) - Used on Marketplace B
- "carlos.mendoza@protonmail.com" (email) - Used for service registrations
- "0x1f9840a85d5aF5bf1D1B629q081Ce3Ra1f08F6d3" (Bitcoin wallet) - Primary wallet

#### Aliases (Post-Migration)
- "ShadowOperator" (handle) - Used on Marketplace B, Forum C (from June 2024)
- "StealthCoder" (handle) - Used on Onion Service D (from June 2024)
- "c.mendoza@protonmail.com" (email) - Used for service registrations (from June 2024)
- "0x2b5Ad5c4795c026514f8317c7a215E21bDcAaDb4" (Bitcoin wallet) - New wallet (from June 2024)

#### Writing Style Characteristics
- Emotional, expressive language
- Frequent use of exclamation points
- Average sentence length: 28 words
- Inconsistent capitalization
- Frequent spelling errors ("teh" instead of "the")

#### Infrastructure (Pre-Migration)
- Marketplace A hosted on IP 203.0.113.50 (ASN 16509 - AMAZON-02)
- Forum C hosted on IP 203.0.113.51 (ASN 16509 - AMAZON-02)
- SSL certificate fingerprint: sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
- PGP key fingerprint: sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

#### Infrastructure (Post-Migration)
- Marketplace B moved to IP 198.51.100.25 (ASN 14061 - DIGITALOCEAN-ASN) (June 2024)
- Onion Service D moved to IP 198.51.100.26 (ASN 14061 - DIGITALOCEAN-ASN) (June 2024)
- New SSL certificate fingerprint: sha256:gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
- New PGP key fingerprint: sha256:hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

#### Wallet Activity (Pre-Migration)
- Primary wallet: 0x1f9840a85d5aF5bf1D1B629q081Ce3Ra1f08F6d3
- Received 4.2 BTC between Jan-May 2024
- Sent 3.9 BTC to known mixer addresses
- Transaction pattern: Large irregular deposits

#### Wallet Activity (Post-Migration)
- New wallet: 0x2b5Ad5c4795c026514f8317c7a215E21bDcAaDb4
- Received 1.1 BTC between Jun-Aug 2024
- Sent 0.9 BTC to exchange addresses
- Transaction pattern: Regular small transactions

#### Relationships
- No trust relationship with Actor Alpha or Bravo
- Frequently mentions Actor Alpha in negative context (4 posts)
- Had business relationship with Actor Bravo (pre-March 2024)

## Services

### Marketplace A
- **Type**: Illicit goods marketplace
- **Active**: January 2024 - Present
- **Primary Language**: English
- **Registration Required**: Yes (email verification)
- **Payment Method**: Bitcoin only
- **Notable Actors**: 
  - Actor Alpha (as "QuantumBreaker")
  - Actor Charlie (pre-Migration: "RansomLord")

### Marketplace B
- **Type**: Illicit services marketplace
- **Active**: March 2024 - Present
- **Primary Language**: English
- **Registration Required**: Yes (email + PGP verification)
- **Payment Method**: Bitcoin and Monero
- **Notable Actors**:
  - Actor Alpha (as "SigmaCoder")
  - Actor Bravo (as "NetGhost" and "DigitalPhantom")
  - Actor Charlie (pre-Migration: "CryptoKing", post-Migration: "ShadowOperator")

### Forum C
- **Type**: Threat actor discussion forum
- **Active**: January 2024 - Present
- **Primary Language**: English
- **Registration Required**: Yes (invitation only)
- **Payment Method**: None (information sharing focus)
- **Notable Actors**:
  - Actor Alpha (as "QuantumBreaker" and "SigmaCoder")
  - Actor Bravo (as "NetGhost" and "DigitalPhantom")
  - Actor Charlie (pre-Migration: "RansomLord", post-Migration: "ShadowOperator")

### Onion Service D
- **Type**: Illicit content hosting service
- **Active**: May 2024 - Present
- **Primary Language**: English
- **Access**: Tor hidden service only
- **Payment Method**: Bitcoin for access
- **Notable Actors**:
  - Actor Alpha (as "SigmaCoder")
  - Actor Bravo (as "DigitalPhantom")
  - Actor Charlie (post-Migration: "StealthCoder")

### Clearnet Site E
- **Type**: Surface web presence/service
- **Active**: February 2024 - Present
- **Primary Language**: English
- **Access**: Public internet
- **Notable Features**:
  - Links to Onion Service D via SSL certificate
  - Shares infrastructure with Onion Service D
  - Used for customer support and communications
- **Notable Actors**:
  - Actor Alpha (linked via SSL certificate)
  - Actor Bravo (linked via SSL certificate)

## Infrastructure Elements

### IP Addresses
- 203.0.113.45: Hosts Onion Service D (Actor Alpha/Bravo/Charlie post-Mig)
- 203.0.113.46: Hosts Clearnet Site E (Actor Alpha/Bravo)
- 203.0.113.50: Hosts Marketplace A (pre-Migration Charlie)
- 203.0.113.51: Hosts Forum C (pre-Migration Charlie)
- 198.51.100.22: Hosts Marketplace B (Actor Bravo)
- 198.51.100.25: Hosts Marketplace B (post-Migration Charlie)
- 198.51.100.26: Hosts Onion Service D (post-Migration Charlie)

### ASNs
- ASN 13335 (CLOUDFLARENET): IPs 203.0.113.45, 203.0.113.46
- ASN 16509 (AMAZON-02): IPs 203.0.113.50, 203.0.113.51
- ASN 14061 (DIGITALOCEAN-ASN): IPs 198.51.100.22, 198.51.100.25, 198.51.100.26

### SSL Certificates
- Cert Alpha: sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  - Used by: Onion Service D (pre-Jun 2024), Clearnet Site E
  - Validity: Jan 2024 - Jan 2025
- Cert Bravo: sha256:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
  - Used by: Marketplace B
  - Validity: Mar 2024 - Mar 2025
- Cert Charlie Pre-Mig: sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  - Used by: Marketplace A, Forum C (pre-Jun 2024)
  - Validity: Jan 2024 - Jun 2024
- Cert Charlie Post-Mig: sha256:gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
  - Used by: Marketplace B, Onion Service D (post-Jun 2024)
  - Validity: Jun 2024 - Jun 2025

### PGP Keys
- Key Alpha: sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
  - Used by: Actor Alpha for signing/posts
- Key Bravo: sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
  - Used by: Actor Bravo for signing/posts
- Key Charlie Pre-Mig: sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  - Used by: Actor Charlie (pre-Jun 2024)
- Key Charlie Post-Mig: sha256:hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
  - Used by: Actor Charlie (post-Jun 2024)

## Temporal Events

### Migration Events
- **June 15, 2024**: Actor Charlie migrates infrastructure and identities
  - Marketplace A → Marketplace B
  - Forum C → Same forum (different alias)
  - New PGP key generated
  - New Bitcoin wallet created
  - SSL certificates updated

### Trust Establishment
- **March 1, 2024**: Mutual trust established between Actor Alpha and Actor Bravo
  - PGP key cross-signing observed
  - Joint forum posts
  - Shared infrastructure usage

### Conflict Events
- **ongoing**: Actor Charlie negative mentions of Actor Alpha
  - 4 forum posts accusing Alpha of being an informant
  - No verifiable evidence provided

## Evaluation Scenarios

### Scenario 1: Basic Attribution
- **Input**: Forum posts by "QuantumBreaker" and "SigmaCoder"
- **Expected Output**: High confidence linkage to Actor Alpha
- **Evidence**: Writing style similarity, PGP key use, temporal consistency

### Scenario 2: Cross-Platform Mapping
- **Input**: 
  - Marketplace A listing by "RansomLord"
  - Forum C post by "ShadowOperator"
  - Bitcoin transaction to wallet 0x2b5Ad5c4795c026514f8317c7a215E21bDcAaDb4
- **Expected Output**: High confidence linkage to Actor Charlie (post-Migration)
- **Evidence**: Migration pattern, wallet linkage, temporal consistency

### Scenario 3: Infrastructure Correlation
- **Input**: 
  - Onion Service D at 203.0.113.45
  - Clearnet Site E at 203.0.113.46
  - Shared SSL certificate fingerprint
- **Expected Output**: Medium confidence linkage between services
- **Evidence**: Certificate sharing, IP proximity, ASN sharing
- **Note**: Should NOT result in high confidence attribution without additional evidence

### Scenario 4: Trust Network Analysis
- **Input**: 
  - Actor Alpha and Actor Bravo PGP key cross-signing
  - Joint forum posts
  - Shared infrastructure usage patterns
- **Expected Output**: Medium-high confidence trust relationship
- **Evidence**: Multiple corroborating evidence types

### Scenario 5: False Positive Resistance
- **Input**:
  - Actor Bravo and Actor Charlie both use ASN 14061
  - Similar transaction timing patterns
  - Similar geographic targeting in posts
- **Expected Output**: Low confidence linkage (should not attribute)
- **Evidence**: Infrastructure sharing is weak evidence alone
- **Note**: Tests system's ability to avoid over-attribution based on weak correlations

## Validation Metrics
The ground truth enables measurement of:
- **Entity Resolution**: Precision, recall, F1-score for alias resolution
- **Attribution Accuracy**: Precision and recall for actor identification
- **Temporal Analysis**: Ability to track entity evolution over time
- **Confidence Calibration**: Do predicted probabilities match empirical accuracy?
- **False Positive Rate**: Critical metric for attribution systems
- **Explainability**: Can system trace conclusions to specific evidence?

## Usage Instructions
1. Load synthetic data using generators in `/home/erebus/scripts/synthetic/`
2. Run system evaluation pipeline
3. Compare results against this ground truth document
4. Calculate metrics using scripts in `/home/erebus/evaluation/`
5. Document any discrepancies for system improvement

## Important Notes
- This ground truth is intentionally comprehensive for thorough evaluation
- In real operations, ground truth would be partial and uncertain
- The synthetic lab represents a simplified threat landscape
- Evaluation should focus on both positive detection and false positive avoidance
- All timestamps and technical details are consistent and verifiable