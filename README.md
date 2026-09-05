# DRISHTI — Evidence-Driven Threat Actor Attribution & Intelligence Platform

**SIH Problem Statement: SIH26151**  
*Blockchain & Cybersecurity Theme*

DRISHTI is an evidence-driven threat actor attribution and intelligence platform designed for the Smart India Hackathon 2026 (SIH26151). The platform focuses on de-anonymizing dark web threat actors through explainable, evidence-based analysis rather than opaque AI decisions.

## Overview

The platform implements a complete intelligence pipeline:
- **Collection**: Gathering data from various sources (web, APIs, Tor, synthetic)
- **Normalization**: Standardizing and validating collected data
- **Extract**: Identifying entities and relationships in normalized data
- **Resolve**: Probabilistic entity disambiguation using Fellegi-Sunter framework
- **Correlate**: Multi-evidence analysis and pattern detection
- **Graph**: Knowledge graph storage and relationship mapping
- **Score**: Evidence-weighted attribution confidence scoring
- **Human Review**: Investigator validation and feedback
- **Report**: Actionable intelligence exports and visualization

## Key Features

- Evidence-driven attribution with explainable confidence scoring
- Probabilistic entity resolution (Fellegi-Sunter framework)
- Multi-layer stylometry and behavioral analysis
- Infrastructure and cryptocurrency intelligence correlation
- Temporal graph modeling for tracking entity evolution
- Plugin-based collector architecture
- Synthetic dark web lab for objective evaluation
- Principled confidence modeling (Dempster-Shafer/Bayesian frameworks)
- Provenance tracking and source reliability scoring
- Human-in-the-loop attribution with evidence preservation

## Research Foundation

This project is built upon comprehensive research including:
- Dark web market analysis and threat actor behavior studies
- Attribution frameworks and confidence modeling approaches
- Stylometry and authorship attribution techniques
- Graph-based cyber threat intelligence methodologies
- Cryptocurrency transaction graph analysis
- Existing tool evaluations (OnionScan, Maltego, OpenCTI, MISP)

## Team Structure

The platform is designed for a six-person student team with clearly defined ownership areas:
1. **Collection + Ingestion** - Data acquisition systems
2. **Backend + Data Engineering** - APIs, data storage, pipeline orchestration
3. **Graph + Entity Resolution** - Disambiguation and graph capabilities
4. **NLP + Stylometry + Behaviour** - Text and behavioral analysis
5. **Infrastructure + Crypto Intelligence** - Correlation and analysis
6. **Frontend + Visualization + Integration** - Investigator dashboard and reporting

## Development Approach

Following a three-scope approach:
- **Scope 1**: 48-hour proof of concept with synthetic data
- **Scope 2**: SIH-ready minimum viable product (12-14 weeks)
- **Scope 3**: Ambitious production architecture (additional 8-12 weeks)

## Evaluation

Performance validated against a synthetic dark web lab with known ground truth relationships, enabling objective measurement of:
- Entity resolution precision and recall
- Attribution accuracy and false positive rates
- Explainability and evidence traceability
- End-to-end investigation workflow effectiveness

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Ethical and Legal Compliance

DRISHTI is designed for authorized security testing, defensive security, CTF challenges, and educational contexts only. The platform incorporates privacy by design, purpose limitation, data minimization, and prohibits covert third-party surveillance or destructive techniques.
