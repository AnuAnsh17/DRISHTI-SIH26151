# Threat Model
## SIH26151 — Dark web threat actor de-anonymization

### Overview
This document outlines the threat model for the SIH26151 platform, identifying potential threats to the system's integrity, confidentiality, and availability, along with corresponding mitigations. The platform is designed for authorized threat intelligence analysis and must resist various attack vectors that could compromise its functionality or lead to erroneous attribution.

### Assets to Protect
1. **Data**: Collected threat intelligence, evidence, entity relationships, attribution hypotheses
2. **System Integrity**: Correct functioning of collection, analysis, and reporting components
3. **Attribution Accuracy**: Prevention of false positives and erroneous conclusions
4. **User Trust**: Confidence that the system provides reliable, explainable results
5. **Operational Continuity**: Availability for investigative work
6. **Provenance Tracking**: Integrity of evidence lineage and source reliability
7. **Algorithm Integrity**: Protection against manipulation of scoring and resolution models

### Threat Actors
- **External Adversaries**: Entities seeking to disrupt or manipulate the platform
- **Malicious Data Providers**: Sources supplying false or misleading information
- **Insider Threats**: Authorized users misusing system capabilities
- **Competing Interests**: Parties seeking to discredit or undermine attribution results
- **Threat Actors Under Investigation**: Subjects attempting to evade detection or plant false evidence

### Threat Categories and Mitigations

#### 1. Data Poisoning and Contamination
**Threat**: Malicious actors inject false data to manipulate attribution results, create false links, or obscure real relationships.

**Specific Vectors**:
- False forum posts with planted identifiers
- Fake PGP keys or wallet addresses
- Spoofed SSL certificates or domain registrations
- Manipulated cryptocurrency transactions
- Synthetic identities designed to create false correlations

**Mitigations**:
- **Source Reliability Scoring**: Weight evidence by source trustworthiness
- **Cross-Source Corroboration**: Require multiple independent sources for high-confidence links
- **Temporal Consistency Checks**: Validate that evidence aligns with known activity patterns
- **Provenance Tracking**: Maintain complete lineage from collection to conclusion
- **Outlier Detection**: Statistical analysis to identify anomalous data patterns
- **Source Validation**: Verify authenticity of data sources when possible
- **Evidence Versioning**: Track changes and updates to evidence over time
- **Manual Review Thresholds**: Require investigator review for high-impact hypotheses

#### 2. False Attribution and Misidentification
**Threat**: System produces incorrect attribution links, either false positives (linking unrelated entities) or false negatives (missing real links).

**Specific Vectors**:
- Convergent evolution: unrelated actors developing similar traits
- Shared infrastructure (CDNs, cloud services, hosting providers)
- Identifier sharing or theft (PGP keys, wallets, handles)
- Behavioral mimicry or intentional obfuscation
- Coincidental similarities in writing style or timing
- Exchange or mixer usage obscuring wallet ownership

**Mitigations**:
- **Evidence Hierarchy**: Distinguish between hard identifiers and soft signals
- **Confidence Thresholds**: Require sufficient evidence weight before accepting links
- **Alternative Hypothesis Generation**: Actively consider competing explanations
- **Falsifiability Conditions**: Define what evidence would refute each hypothesis
- **Uncertainty Quantification**: Provide confidence intervals, not point estimates
- **Human-in-the-Loop**: Require expert validation for actionable conclusions
- **Performance Metrics**: Track false positive/negative rates during testing
- **Contextual Analysis**: Consider operational context when evaluating evidence

#### 3. Source and Collector Compromise
**Threat**: Adversaries compromise data collection mechanisms to feed manipulated data or gather intelligence about the platform's operations.

**Specific Vectors**:
- Compromised web scrapers or API collectors
- Man-in-the-middle attacks on data feeds
- Fake websites or services designed to attract collection
- Malicious Tor exit nodes modifying traffic
- Compromised synthetic data generators
- Supply chain attacks on third-party data providers

**Mitigations**:
- **Collector Isolation**: Run collectors in sandboxed environments
- **Input Validation**: Validate and sanitize all incoming data
- **Collector Health Monitoring**: Detect anomalous behavior or failure patterns
- **Multiple Collection Methods**: Use diverse approaches to reduce single-point failure
- **Network Security**: Encrypt collector communications where appropriate
- **Code Signing**: Verify integrity of collector software updates
- **Rate Limiting and Etiquette**: Avoid overwhelming sources or appearing hostile
- **Redundancy**: Maintain backup collectors for critical data sources

#### 4. Model Manipulation and Adversarial Machine Learning
**Threat**: Adversaries manipulate or evade machine learning models used for stylometry, behavioral analysis, or clustering.

**Specific Vectors**:
- Adversarial stylometry: deliberate alteration of writing style
- Behavioral evasion: changing activity patterns to avoid detection
- Feature manipulation: crafting data to trigger specific model outputs
- Model poisoning: injecting training data to bias models
- Extraction attacks: reverse-engineering model parameters through queries

**Mitigations**:
- **Model Diversity**: Use multiple complementary approaches (not relying on single ML model)
- **Adversarial Testing**: Regularly test models against known evasion techniques
- **Uncertainty Quantification**: Provide confidence scores that decrease under adversarial conditions
- **Feature Obfuscation**: Hide which features are most influential in models
- **Regular Retraining**: Update models with fresh data to prevent staleness
- **Human Oversight**: Use ML as investigative aid, not sole decision-maker
- **Explainability**: Focus on models that provide interpretable results
- **Conservative Thresholds**: Require stronger evidence when model confidence is low

#### 5. Graph Poisoning and Relationship Injection
**Threat**: Adversaries inject false relationships or entities into the graph database to create misleading connection paths or obscure real ones.

**Specific Vectors**:
- Fake entity creation with false attributes
- Spurious relationship insertion (e.g., false infrastructure sharing)
- Temporal manipulation: creating false historical relationships
- Confidence inflation: artificially boosting relationship confidence scores
- Entity merging: incorrectly linking unrelated entities through false evidence

**Mitigations**:
- **Relationship Validation**: Verify new relationships against evidence before insertion
- **Provenance Tracking**: Track source and confidence for all relationships
- **Temporal Consistency**: Reject relationships with impossible timelines
- **Degree Monitoring**: Detect and investigate sudden increases in entity connections
- **Graph Analytics**: Use community detection and centrality to identify anomalous patterns
- **Access Controls**: Restrict graph modification to authorized components
- **Audit Logging**: Log all graph modifications for forensic analysis
- **Relationship Expiration**: Implement automatic review of stale relationships

#### 6. Confidence Score Manipulation
**Threat**: Adversaries manipulate the evidence combination or scoring process to inflate or deflate attribution confidence inappropriately.

**Specific Vectors**:
- Evidence weighting manipulation: altering how different evidence types are combined
- Source reliability spoofing: fabricating high-reliability sources
- Confidence feedback loops: using system output to reinforce false hypotheses
- Temporal window manipulation: selecting time ranges to maximize spurious correlations
- Selective evidence presentation: hiding contradictory evidence

**Mitigations**:
- **Transparent Scoring**: Use explainable models (Dempster-Shafer, weighted scoring with documentation)
- **Evidence Auditing**: Trace confidence scores back to individual evidence items
- **Source Independence Checks**: Verify evidence sources are not colluding
- **Temporal Robustness**: Test scoring across multiple time windows
- **Complete Evidence Presentation**: Show supporting and contradicting evidence
- **Calibration Monitoring**: Regularly check that predicted confidence matches empirical accuracy
- **Human Review**: Require investigator agreement on final confidence scores
- **Version Control**: Track changes to scoring algorithms and parameters

#### 7. Privacy Violations and Data Exposure
**Threat**: Unauthorized exposure of collected data, potentially revealing sensitive information about sources, methods, or subjects under investigation.

**Specific Vectors**:
- Database breaches or leaks
- Insecure API endpoints exposing raw data
- Log files containing sensitive information
- Improper data handling or storage practices
- Inadequate anonymization of exported reports
- Side-channel attacks revealing processing patterns

**Mitigations**:
- **Data Minimization**: Collect only data necessary for analysis
- **Access Controls**: Role-based access to sensitive data
- **Encryption**: Encrypt data at rest and in transit
- **Secure Development**: Follow security best practices in coding
- **Audit Logging**: Monitor access to sensitive data
- **Data Masking**: Anonymize or pseudonymize data in non-essential contexts
- **Secure Export**: Apply appropriate controls to exported data
- **Regular Security Scans**: Vulnerability scanning and penetration testing
- **Incident Response**: Procedures for data breach notification and containment

#### 8. Availability and Service Disruption
**Threat**: Attacks aimed at making the platform unavailable or degrading its performance.

**Specific Vectors**:
- Denial-of-service attacks on collection infrastructure
- Resource exhaustion through expensive queries
- Database corruption or locking issues
- Dependency failures (external APIs, services)
- Malicious data designed to cause processing errors
- Infrastructure failures (power, network, hardware)

**Mitigations**:
- **Rate Limiting**: Protect collectors and APIs from overload
- **Resource Quotas**: Limit computational resources per query or operation
- **Graceful Degradation**: Continue operation with reduced functionality when possible
- **Health Checks**: Monitor service availability and performance
- **Redundancy**: Design for failure tolerance where appropriate
- **Input Validation**: Prevent malformed data from causing crashes
- **Timeouts**: Cancel long-running or stuck operations
- **Backup and Recovery**: Regular backups with tested restore procedures
- **Monitoring and Alerting**: Detect availability issues promptly

#### 9. Legal and Compliance Risks
**Threat**: Platform usage violates laws, regulations, or ethical guidelines, leading to legal liability or reputational damage.

**Specific Vectors**:
- Unauthorized access to prohibited data sources
- Collection of personal data without proper authorization
- Export of data violating data protection regulations
- Attribution used for unlawful surveillance or repression
- Violations of terms of service for data sources or APIs
- Inadequate oversight or accountability mechanisms

**Mitigations**:
- **Authorized Sources Only**: Restrict collection to public, authorized, or synthetic data
- **Purpose Limitation**: Use data strictly for stated research purposes
- **Data Protection Compliance**: Follow GDPR, CCPA, etc. where applicable
- **Ethical Review**: Establish oversight for sensitive operations
- **Terms of Service Compliance**: Respect API and data source usage policies
- **Attribution Disclaimers**: Clearly state limitations and uncertainty in results
- **Use Case Restrictions**: Prohibit unlawful or unethical applications
- **Audit Trails**: Maintain logs for accountability and investigation
- **Legal Consultation**: Regular review with legal counsel as needed

#### 10. Insider Threat and Privilege Abuse
**Threat**: Authorized users misuse system capabilities for personal gain, revenge, or unauthorized investigations.

**Specific Vectors**:
- Unauthorized data exports or leaks
- Improper attribution targeting specific individuals
- Manipulation of evidence or scoring for personal reasons
- Access to or modification of ongoing investigations
- Use of system for non-authorized purposes
- Credential sharing or privilege escalation

**Mitigations**:
- **Least Privilege Access**: Users only get access needed for their role
- **Separation of Duties**: Critical operations require multiple authorized users
- **Activity Logging**: Comprehensive logging of user actions
- **Access Reviews**: Periodic review of user permissions
- **Behavioral Analytics**: Detect anomalous user behavior patterns
- **Strong Authentication**: Multi-factor authentication for sensitive access
- **Session Management**: Secure session handling and timeout
- **Acceptable Use Policies**: Clear guidelines on appropriate system use
- **Whistleblower Protections**: Safe channels for reporting misuse

### Risk Assessment Matrix

| Threat Category | Likelihood | Impact | Risk Level | Primary Mitigations |
|----------------|------------|--------|------------|---------------------|
| Data Poisoning | Medium | High | High | Source reliability, corroboration, provenance |
| False Attribution | Medium | High | High | Evidence hierarchy, uncertainty quantification, human review |
| Source Compromise | Low | Medium | Medium | Collector isolation, input validation, health monitoring |
| Model Manipulation | Medium | Medium | Medium | Model diversity, adversarial testing, explainability |
| Graph Poisoning | Low | High | Medium | Relationship validation, provenance, access controls |
| Confidence Manipulation | Low | High | Medium | Transparent scoring, evidence auditing, calibration |
| Privacy Violations | Low | High | Medium | Data minimization, encryption, access controls |
| Availability Disruption | Medium | Medium | Medium | Rate limiting, resource quotas, health checks |
| Legal/Compliance | Low | High | Medium | Authorized sources, purpose limitation, compliance review |
| Insider Threat | Low | High | Medium | Least privilege, separation of duties, activity logging |

### Assumptions and Exclusions

#### Assumptions
1. **Authorized Data Only**: All data collection relies on publicly available, authorized, or synthetic sources
2. **No Active Countermeasures**: Platform does not engage in active deception, hacking, or counterintelligence operations
3. **Human Oversight**: Investigators provide final validation and interpretation of automated results
4. **Synthetic Data Validity**: Synthetic datasets accurately represent relevant aspects of real-world threat landscapes
5. **Evolving Threats**: Threat actor techniques evolve, requiring continuous model updating
6. **Resource Constraints**: Operating within student project limitations for scale and complexity

#### Exclusions (Out of Scope)
1. **Active Deanonymization**: No engagement in active attacks against Tor or anonymity networks
2. **Malware Development**: No creation or distribution of malicious software
3. **Credential Theft**: No attempt to steal passwords, keys, or credentials
4. **Unauthorized Access**: No attempts to breach systems or services without authorization
5. **Physical Surveillance**: No real-world tracking or physical monitoring of individuals
6. **Legal Interception**: No wiretapping, intercepting communications, or similar activities
7. **Offensive Operations**: No offensive cyber operations or hack-back capabilities
8. **Real-Time Surveillance**: No continuous monitoring of specific individuals or groups
9. **Data Fabrication**: No creation of false evidence to support predetermined conclusions
10. **Deterministic Attribution**: No claims of certain attribution without appropriate evidence and uncertainty quantification

### Security Controls by System Layer

#### Collection Layer
- **Controls**: Sandboxed execution, input validation, rate limiting, source verification, health monitoring, network segmentation
- **Monitoring**: Collection success rates, error patterns, resource usage, anomalous data volumes

#### Normalization and Extraction Layers
- **Controls**: Input validation, schema validation, whitelisting of allowed transformations, sandboxed processing
- **Monitoring**: Processing latency, error rates, extraction quality metrics

#### Resolution and Correlation Layers
- **Controls**: Evidence validation, confidence bounds, temporal checks, source reliability weighting, manual review workflows
- **Monitoring**: Resolution accuracy, confidence distributions, link strength metrics, contradiction detection rates

#### Graph and Storage Layer
- **Controls**: Access controls, encryption at rest, audit logging, relationship validation, backup and recovery
- **Monitoring**: Query performance, storage utilization, backup integrity, anomalous graph patterns

#### Scoring and Attribution Layer
- **Controls**: Explainable models, uncertainty quantification, evidence tracing, calibration monitoring, human review requirements
- **Monitoring**: Score calibration, false positive/negative rates, hypothesis validation rates, evidence trail completeness

#### Presentation and Reporting Layer
- **Controls**: Output validation, data minimization in exports, access controls on reports, watermarking, distribution tracking
- **Monitoring**: Export volumes, access patterns, report completeness, user feedback on usability

### Incident Response Procedures

#### Detection
- **Automated Alerts**: Anomalies in data patterns, processing errors, authentication failures
- **Manual Reports**: User-suspected issues, auditor findings, external notifications
- **Health Checks**: Regular automated checks of system components

#### Response
1. **Triage**: Assess severity, scope, and potential impact
2. **Containment**: Isolate affected components to prevent spread
3. **Eradication**: Remove malicious elements and address root causes
4. **Recovery**: Restore normal operations from clean state
5. **Post-Incident**: Conduct review, update defenses, report findings

#### Communication
- **Internal**: Notify system administrators, development team, and stakeholders
- **External**: Follow legal requirements for data breach notification if applicable
- **Documentation**: Maintain incident records for accountability and improvement

### Testing and Validation

#### Threat Modeling Validation
- **Red Team Exercises**: Periodic simulated attacks to test defenses
- **Penetration Testing**: Authorized attempts to breach system security
- **Code Review**: Security-focused review of critical components
- **Threat Intelligence Feeds**: Monitor for emerging threats relevant to platform

#### Resilience Testing
- **Chaos Engineering**: Controlled introduction of failures to test resilience
- **Load Testing**: Verify performance under expected and peak loads
- **Failover Testing**: Validate backup and recovery procedures
- **Dependency Testing**: Assess impact of external service failures

#### Attribution Validation
- **Synthetic Ground Truth**: Test against synthetic datasets with known relationships
- **Historical Validation**: Test against historical cases with known outcomes (when available)
- **Expert Review**: Have domain experts evaluate attribution conclusions
- **Blind Testing**: Test analysts without revealing expected outcomes

### Conclusion
This threat model provides a comprehensive framework for securing the SIH26151 platform against a wide range of threats. By implementing the outlined mitigations and following security best practices throughout the system lifecycle, the platform can maintain its integrity, reliability, and usefulness as a threat intelligence analysis tool while adhering to ethical and legal constraints. Regular review and updating of this threat model is essential as the threat landscape evolves.