# Functional and Non-Functional Requirements
## SIH26151 — Dark web threat actor de-anonymization

## Functional Requirements

### 1. Data Collection Subsystem
- **FR-1.1**: Plugin-based collector architecture supporting web scraping, API ingestion, and Tor data collection
- **FR-1.2**: Collect data from at least 3 different source types (web, API, Tor/synthetic)
- **FR-1.3**: Implement source reliability tracking and validation mechanisms
- **FR-1.4**: Apply rate limiting and etiquette protocols for target sources
- **FR-1.5**: Provide complete provenance metadata with all collected data (source, timestamp, collection method)
- **FR-1.6**: Handle source failures gracefully with retry logic and error reporting

### 2. Data Normalization Subsystem
- **FR-2.1**: Convert diverse data formats to a canonical intelligence schema
- **FR-2.2**: Achieve ≥95% format conversion accuracy for target data types
- **FR-2.3**: Detect and handle duplicate records with ≥90% precision and ≥80% recall
- **FR-2.4**: Validate data integrity and identify malformed/invalid entries
- **FR-2.5**: Maintain processing overhead <20% increase over raw ingestion time
- **FR-2.6**: Preserve provenance metadata throughout normalization process

### 3. Entity and Relationship Extraction Subsystem
- **FR-3.1**: Extract entity mentions (actors, aliases, infrastructure, wallets, etc.) from normalized text
- **FR-3.2**: Extract relationship candidates between entities (co-mention, temporal proximity, etc.)
- **FR-3.3**: Achieve ≥80% precision and ≥70% recall for entity mention extraction
- **FR-3.4**: Achieve ≥0.70 F1-score for relationship extraction
- **FR-3.5**: Provide confidence calibration for extractions (Brier score <0.15)
- **FR-3.6**: Support entity type-specific evaluation and tuning

### 4. Entity Resolution Subsystem
- **FR-4.1**: Implement probabilistic entity resolution using Fellegi-Sunter framework
- **FR-4.2**: Achieve ≥85% precision and ≥75% recall for entity resolution (critical for attribution)
- **FR-4.3**: Maintain false link rate <5%
- **FR-4.4**: Achieve ≥80% cluster purity (resolved entities refer to same real entity)
- **FR-4.5**: Provide resolution stability ≥90% for resolved entities over time
- **FR-4.6**: Support temporal entity evolution and versioning
- **FR-4.7**: Implement conflict detection and resolution mechanisms
- **FR-4.8**: Provide explainable resolution decisions with evidence tracing

### 5. Correlation Subsystem
- **FR-5.1**: Analyze multi-evidence patterns and relationships between resolved entities
- **FR-5.2**: Infrastructure correlation: ≥80% precision, ≥70% recall for shared infrastructure identification
- **FR-5.3**: Stylometric similarity: ≥75% precision, ≥65% recall for same-author text identification
- **FR-5.4**: Behavioral similarity: ≥70% precision, ≥60% recall for similar behavior pattern identification
- **FR-5.5**: Wallet linkage: ≥80% precision for wallet/entity relationships (strong evidence)
- **FR-5.6**: Evidence combination effectiveness: ≥20% F1-score improvement over best single evidence type

### 6. Graph Storage and Query Subsystem
- **FR-6.1**: Store entities and relationships in a graph database (Neo4j recommended)
- **FR-6.2**: Execute attribution path queries (<3 hops) in <2s
- **FR-6.3**: Process batch updates (<5s) and make new entities/relationships queryable
- **FR-6.4**: Execute neighborhood expansion queries (<3s for 2-hop)
- **FR-6.5**: Maintain storage efficiency <1KB average per node/relationship
- **FR-6.6**: Handle concurrent queries (<5s 95th percentile for 10 concurrent queries)

### 7. Attribution Scoring Subsystem
- **FR-7.1**: Combine evidence from multiple sources to generate attribution hypotheses
- **FR-7.2**: Achieve ≥80% precision and ≥60% recall for attribution (high confidence threshold)
- **FR-7.3**: Maintain false attribution rate <3%
- **FR-7.4**: Provide confidence calibration (Brier score <0.10, responsiveness to evidence)
- **FR-7.5**: Ensure explainability: ≥80% of confidence traceable to specific evidence items
- **FR-7.6**: Generate ≥70% of relevant alternative hypotheses for consideration
- **FR-7.7**: Support graduated attribution levels (Suspected, Credible, Confirmed, Refuted)

### 8. Human Review and Investigation Subsystem
- **FR-8.1**: Provide investigator interface for reviewing attribution hypotheses
- **FR-8.2**: Enable evidence traceability from conclusions back to raw data (≥90% traceability)
- **FR-8.3**: Support hypothesis tracking, updating, and annotation
- **FR-8.4**: Allow investigator feedback to refine automated attribution
- **FR-8.5**: Provide evidence presentation and explanation tools (trails, contributions)

### 9. Reporting and Export Subsystem
- **FR-9.1**: Generate attribution reports in multiple formats (CSV, JSON, formatted reports)
- **FR-9.2**: Support export of investigation results, evidence trails, and analytics
- **FR-9.3**: Enable scheduled and on-demand report generation
- **FR-9.4**: Provide configurable report templates and content

### 10. System Integration and Orchestration
- **FR-10.1**: Implement end-to-end pipeline: Collection → Normalization → Extraction → Resolution → Correlation → Graph → Scoring → Reporting
- **FR-10.2**: Enable asynchronous processing between subsystems (message queues)
- **FR-10.3**: Provide synchronous APIs for request/response interactions
- **FR-10.4**: Use shared graph database as central storage for all subsystems
- **FR-10.5**: Implement centralized configuration management
- **FR-10.6**: Provide unified logging, metrics, and alerting system

## Non-Functional Requirements

### Performance
- **NFR-1.1**: System responds to investigator actions within <2s for 95% of cases
- **NFR-1.2**: End-to-end investigation workflow completes in <30 minutes for guided synthetic lab scenario
- **NFR-1.3**: System handles expected data volume with <2s latency for 95% of queries
- **NFR-1.4**: Graph database query response time <2s for attribution path queries (<3 hops)

### Scalability
- **NFR-2.1**: Design for horizontal scaling capabilities (post-MVP)
- **NFR-2.2**: Support increasing data volumes with predictable performance degradation
- **NFR-2.3**: Enable concurrent investigator access (≥50 investigators with <3s response times - post-MVP)

### Reliability
- **NFR-3.1**: Implement backup and recovery procedures for critical data
- **NFR-3.2**: Provide monitoring, logging, and alerting for system health
- **NFR-3.3**: Achieve <5% collection error rate from authorized sources
- **NFR-3.4**: Handle source failures gracefully with appropriate retry logic

### Security
- **NFR-4.1**: Implement authentication and authorization system (RBAC)
- **NFR-4.2**: Encrypt data at rest and in transit (TLS)
- **NFR-4.3**: Maintain comprehensive audit trail for all user actions
- **NFR-4.4**: Apply input validation and sanitization to prevent injection attacks
- **NFR-4.5**: Implement rate limiting and abuse prevention for public interfaces

### Privacy and Compliance
- **NFR-5.1**: Apply privacy by design principles in data handling
- **NFR-5.2**: Implement purpose limitation - data used only for authorized attribution purposes
- **NFR-5.3**: Practice data minimization - collect only necessary data for analysis
- **NFR-5.4**: Ensure legal and ethical compliance for authorized security testing contexts
- **NFR-5.5**: Prohibit covert third-party surveillance or destructive techniques

### Maintainability
- **NFR-6.1**: Follow consistent coding standards and documentation practices
- **NFR-6.2**: Implement modular, loosely-coupled architecture
- **NFR-6.3**: Provide comprehensive API documentation and SDKs
- **NFR-6.4**: Implement code review and testing processes
- **NFR-6.5**: Maintain living documentation updated with features

### Usability
- **NFR-7.1**: Provide intuitive investigator dashboard with multiple views (entity, hypothesis, evidence)
- **NFR-7.2**: Enable interactive graph visualization and exploration
- **NFR-7.3**: Support hypothesis management and tracking systems
- **NFR-7.4**: Provide evidence presentation and explanation system
- **NFR-7.5**: Maintain responsive interface (<2s response time for 95% of actions)
- **NFR-7.6**: Provide comprehensive user documentation and help system

### Portability
- **NFR-8.1**: Design for containerized deployment (Docker)
- **NFR-8.2**: Provide documented deployment, configuration, and operational procedures
- **NFR-8.3**: Support deployment in varied infrastructure environments
