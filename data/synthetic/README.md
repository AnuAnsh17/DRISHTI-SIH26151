# Synthetic Dark Web Lab for SIH26151

## Overview
This directory contains the synthetic dark web ecosystem designed for evaluation and testing of the SIH26151 platform. The lab provides a controlled environment with known ground truth relationships to validate the system's attribution capabilities.

## Lab Structure

### Services
- **Marketplace A**: Dark web marketplace for goods and services
- **Marketplace B**: Competing dark web marketplace
- **Forum C**: Discussion forum for threat actors
- **Onion Service D**: Hidden service hosting illicit content
- **Clearnet Site E**: Surface web site linked to onion services

### Actors
- **Actor Alpha**: Primary threat actor with multiple aliases
- **Actor Bravo**: Secondary threat actor
- **Actor Charlie**: Third threat actor with migration behavior

## Ground Truth Documentation

Each actor has the following attributes:
- Multiple aliases across platforms
- Writing style samples
- PGP key(s)
- Cryptocurrency wallet(s)
- Timestamps of activity
- Relationships with other actors
- Infrastructure connections
- Documented migration events

## Evaluation Purpose
The synthetic lab allows the system to:
1. Test entity resolution accuracy
2. Validate stylometry and behavioral analysis
3. Measure infrastructure correlation effectiveness
4. Evaluate attribution confidence scoring
5. Measure false positive and false negative rates
6. Test temporal analysis capabilities
7. Validate cross-platform entity mapping

## Usage
- Data generators in `/home/erebus/scripts/synthetic/`
- Ground truth documentation in `/home/erebus/data/synthetic/GROUND_TRUTH.md`
- Test scenarios in `/home/erebus/tests/synthetic/`

## Important Notes
- This is a synthetic environment for controlled testing only
- No real dark web services are replicated or targeted
- All data is artificially generated with known characteristics
- Ground truth is intentionally not obfuscated to enable clear validation