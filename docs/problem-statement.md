# SIH26151 Problem Statement
## Dark web threat actor de-anonymization

### Background
Dark web platforms enable threat actors to operate with perceived anonymity, engaging in illicit activities including data breaches, malware distribution, and illegal transactions. Traditional attribution methods often fail due to sophisticated operational security (OPSEC) practices, pseudonym usage, and infrastructure hopping.

### Challenge
Law enforcement and cybersecurity agencies struggle to reliably attribute dark web activities to real-world identities due to:
- Fragmented evidence across multiple platforms
- Sophisticated OPSEC measures (handle rotation, timing obfuscation)
- Lack of integrated analysis frameworks for multi-source correlation
- High false positive rates in existing attribution systems
- Limited explainability in AI-driven attribution approaches

### SIH26151 Objective
Develop an evidence-driven threat actor attribution platform that enables systematic de-anonymization of dark web actors through transparent, evidence-based analysis rather than opaque black-box decisions.

### Core Requirements
1. **Evidence-Driven Attribution**: All attribution hypotheses must be traceable to specific evidence elements with quantified confidence
2. **Explainable Analysis**: System must preserve evidence provenance and enable investigator verification of conclusions
3. **Multi-Platform Correlation**: Ability to link actor identities across dark web markets, forums, clearnet sites, and infrastructure
4. **Temporal Analysis**: Tracking of actor evolution over time including migration events and OPSEC changes
5. **Human-in-the-Loop**: Investigators must be able to review, validate, and refine automated attribution hypotheses
6. **Synthetic Validation**: Platform must be evaluable against a controlled synthetic dark web lab with known ground truth

### Attribution Levels
The system shall support graduated levels of attribution confidence:
- **Suspected**: Low confidence, based on weak or circumstantial evidence
- **Credible**: Medium confidence, corroborated by multiple evidence types
- **Confirmed**: High confidence, supported by strong convergent evidence with minimal contradictions
- **Refuted**: Evidence sufficient to disprove hypothesized linkage

### Investigator Workflow
1. **Evidence Collection**: Gather data from diverse sources (web, APIs, Tor, synthetic)
2. **Evidence Normalization**: Standardize data formats and validate integrity
3. **Entity Extraction**: Identify mentions of actors, aliases, infrastructure, etc.
4. **Entity Resolution**: Disambiguate and link mentions to resolved entities
5. **Evidence Correlation**: Find relationships between resolved entities across evidence types
6. **Attribution Scoring**: Combine evidence to generate confidence-weighted hypotheses
7. **Human Review**: Investigators examine evidence trails and validate/refute hypotheses
8. **Reporting**: Generate actionable intelligence reports with evidence traceability

### Success Metrics
- Attribution precision ≥75% at ≥60% recall (MVP threshold)
- False attribution rate ≤5%
- False link rate ≤10% in entity resolution
- Explainability: ≥70% of confidence traceable to specific evidence
- End-to-end functionality from collection to report generation
- Successfully resolve ≥60% of ground truth linkages in synthetic lab
