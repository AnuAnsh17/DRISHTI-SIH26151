# System Architecture
## SIH26151 — Dark web threat actor attribution platform

## Overview
This document describes the high-level architecture of the DRISHTI platform, including logical components, physical deployment, data flows, and integration patterns. The architecture follows a modular, layered approach designed for extensibility, maintainability, and clear separation of concerns.

## Architectural Goals
- **Evidence-Driven**: All attribution decisions traceable to specific evidence elements
- **Modular**: Loosely-coupled components with well-defined interfaces
- **Scalable**: Designed for horizontal scaling (post-MVP)
- **Explainable**: Evidence preservation and traceability throughout pipeline
- **Secure**: Authentication, authorization, and audit logging
- **Extensible**: Plugin-based architecture for collectors and analyzers
- **Observable**: Comprehensive monitoring, logging, and metrics

## Logical Architecture

### Layered Component Model
The system is organized into horizontal layers with vertical feature slices:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Presentation Layer                           │
├─────────────────────────────────────────────────────────────────────┤
│                        Application Layer                            │
├─────────────────────────────────────────────────────────────────────┤
│                        Domain Layer                                 │
├─────────────────────────────────────────────────────────────────────┤
│                        Infrastructure Layer                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Vertical Feature Slices (End-to-End Pipeline)
Each slice represents a complete flow from data intake to attribution output:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Evidence Pipeline                                │
├─────────────┬─────────────┬─────────────┬─────────────┬─────────────┤
│ Collection  │ Normalization│ Extraction  │ Resolution  │ Correlation │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │             │
│    Graph Storage and Query Layer (Shared Across All Slices)        │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│    Scoring  │   Review    │   Reporting │    Ops      │             │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

### Detailed Component Breakdown

#### 1. Collection Layer
**Responsibility**: Acquire data from diverse sources while maintaining provenance and etiquette

**Components**:
- **Collector Framework**: Plugin interface for adding new collection types
- **Web Scrapers**: HTTP-based collectors respecting robots.txt and rate limits
- **API Collectors**: Secure ingestion from authorized APIs (OAuth, API keys)
- **Tor/Synthetic Data Collectors**: Specialized collectors for dark web and lab data
- **Scheduler/Orchestrator**: Manages collection jobs, frequency, and resource allocation
- **Source Reliability Service**: Tracks and scores source quality over time
- **Quarantine/Validation**: Isolates suspicious or malformed collected data

**Interfaces**:
- Output: Raw data objects with provenance metadata (JSON format)
- Input: Configuration (source lists, schedules, rate limits)
- Input: Health signals from monitoring system
- Output: Alerts for collection failures/anomalies

#### 2. Normalization Layer
**Responsibility**: Standardize data formats and validate integrity

**Components**:
- **Format Detector**: Identifies source/format of incoming data
- **Schema Mapper**: Converts source-specific formats to canonical schema
- **Validator**: Checks data integrity, completeness, and correctness
- **Deduplicator**: Identifies and links duplicate records
- **Quarantine Manager**: Routes invalid data for manual review
- **Provenance Preserver**: Maintains metadata throughout normalization

**Interfaces**:
- Input: Raw data objects from collection layer
- Output: Normalized data objects in canonical intelligence schema
- Output: Validation metrics and quality indicators
- Output: Quarantined items for investigation

#### 3. Extraction Layer
**Responsibility**: Identify entities and relationships in normalized text

**Components**:
- **Text Preprocessor**: Cleans, normalizes, and tokenizes text
- **Entity Recognizer**: Identifies mentions of actors, aliases, infrastructure, etc.
- **Relationship Extractor**: Finds potential connections between entities
- **Confidence Calibrator**: Aligns extraction scores with empirical accuracy
- **Type-Specific Analyzers**: Specialized extractors for different entity types
- **Feature Generator**: Creates feature vectors for downstream analysis

**Interfaces**:
- Input: Normalized text data from normalization layer
- Output: Entity mentions with types, locations, confidence scores
- Output: Relationship candidates with evidence and confidence
- Output: Feature vectors for stylometric/behavioral analysis
- Output: Extraction performance metrics

#### 4. Resolution Layer
**Responsibility**: Disambiguate entity mentions and link to resolved entities

**Components**:
- **Candidate Generator**: Creates potential resolved entities for mentions
- **Evidence Comparator**: Compares feature vectors between mentions and candidates
- **Fellegi-Sunter Engine**: Probabilistic matching algorithm implementation
- **Conflict Detector**: Identifies contradictory evidence for same mentions
- **Version Manager**: Handles temporal entity evolution and history
- **Resolution Explainer**: Provides evidence tracing for resolution decisions

**Interfaces**:
- Input: Entity mentions from extraction layer
- Output: Resolved entities with confidence scores and version history
- Output: Conflict reports for investigator review
- Output: Resolution performance metrics (precision, recall, etc.)

#### 5. Correlation Layer
**Responsibility**: Analyze multi-evidence patterns and relationships

**Components**:
- **Infrastructure Correlator**: Analyzes certificates, domains, IPs, ASNs, services
- **Stylometry Correlator**: Compares writing style, n-grams, syntactic features
- **Behavior Correlator**: Analyzes temporal patterns, activity cycles, timing
- **Crypto Correlator**: Analyzes wallet addresses, transaction patterns, clustering
- **Evidence Combiner**: Integrates multi-evidence scores using principled methods
- **Novelty Detector**: Identifies unusual patterns for investigation

**Interfaces**:
- Input: Resolved entities and their evidence from resolution layer
- Output: Correlation scores between entities by evidence type
- Output: Combined relationship evidence with confidence scores
- Output: Correlation performance metrics and detection rates

#### 6. Graph Layer
**Responsibility**: Store and query entities and relationships as a knowledge graph

**Components**:
- **Graph Database**: Neo4j instance for relationship traversal
- **Graph Modeler**: Defines node/relationship schemas and properties
- **Index Manager**: Creates and maintains indexes for query performance
- **Temporal Handler**: Manages valid time intervals for entities/relationships
- **Query Optimizer**: Optimizes common traversal and path-finding queries
- **Backup/Recovery**: Manages graph database snapshots and restore

**Interfaces**:
- Input: Resolved entities and relationships from correlation layer
- Output: Graph traversal results and path queries
- Output: Graph storage and indexing metrics
- Output: Update latency and query response times

#### 7. Scoring Layer
**Responsibility**: Generate evidence-weighted attribution hypotheses

**Components**:
- **Evidence Aggregator**: Collects evidence from multiple sources for candidates
- **Confidence Model**: Implements Dempster-Shafer or Bayesian evidence combination
- **Hypothesis Generator**: Creates attribution hypotheses from evidence
- **Explainability Engine**: Traces confidence contributions to specific evidence
- **Alternative Generator**: Produces competing hypotheses for consideration
- **Calibration Monitor**: Tracks alignment of predicted vs. empirical accuracy

**Interfaces**:
- Input: Graph query results and correlation data
- Output: Attribution hypotheses with confidence scores and evidence trails
- Output: Supporting and contradictory evidence for each hypothesis
- Output: Attribution performance metrics (precision, recall, calibration)

#### 8. Review Layer
**Responsibility**: Enable investigator examination and validation of hypotheses

**Components**:
- **Hypothesis Viewer**: Displays attribution hypotheses with evidence trails
- **Evidence Navigator**: Allows tracing evidence back to raw data sources
- **Annotation System**: Enables investigator notes and tags on evidence/hypotheses
- **Feedback Collector**: Records investigator validations, refutations, and suggestions
- **Hypothesis Manager**: Tracks hypothesis status (pending, reviewed, confirmed, etc.)
- **Conflict Resolver**: Helps investigators resolve contradictory evidence

**Interfaces**:
- Input: Attribution hypotheses from scoring layer
- Output: Investigator actions, annotations, and feedback
- Output: Updated hypothesis status and investigator notes
- Output: Review performance metrics and investigator satisfaction

#### 9. Reporting Layer
**Responsibility**: Generate actionable intelligence reports

**Components**:
- **Report Templating**: Defines formats for different report types
- **Data Formatter**: Structures hypothesis and evidence data for output
- **Export Engine**: Generates reports in CSV, JSON, and formatted documents
- **Scheduled Reporting**: Automates report generation on defined schedules
- **Alert Integration**: Triggers report generation based on thresholds/events
- **Audit Logger**: Records report generation for compliance and tracking

**Interfaces**:
- Input: Attribution hypotheses (reviewed or raw) from review layer
- Input: Evidence trails and provenance metadata
- Output: Reports in multiple formats (CSV, JSON, PDF/HTML)
- Output: Scheduled and alert-triggered reports
- Output: Report generation metrics and audit logs

#### 10. Operations Layer
**Responsibility**: Ensure system health, security, and operability

**Components**:
- **Authentication Service**: Manages user identities and access control (RBAC)
- **Authorization Engine**: Enforces permission checks on resources and actions
- **Audit Logging**: Records all system access and user actions
- **Encryption Manager**: Handles data encryption at rest and in transit
- **Monitoring & Alerting**: Tracks system health, performance, and anomalies
- **Backup/Recovery**: Manages system-wide backup and disaster recovery
- **Configuration Service**: Centralized management of system settings
- **Rate Limiter**: Prevents abuse and ensures fair resource usage

**Interfaces**:
- Cross-cutting: Provides security, monitoring, and operational services to all layers
- Input: Security events and performance metrics from all components
- Output: Security alerts, health notifications, and operational reports
- Output: Compliance audit trails and access logs

## Physical Architecture

### Deployment Model
The platform is designed for containerized deployment using Docker and orchestration with Docker Compose (MVP) or Kubernetes (production):

```
┌─────────────────────────────────────────────────────┐
│            Host Infrastructure                      │
├─────────────────────────────────────────────────────┤
│  Container Runtime (Docker)  │  Orchestration Layer │
├─────────────────────────────────────────────────────┤
│  Collection   │ Normalization  │ Extraction       │
│  Services     │ Services       │ Services         │
├─────────────────────────────────────────────────────┤
│  Resolution   │ Correlation    │ Graph Database   │
│  Services     │ Services       │ (Neo4j)          │
├─────────────────────────────────────────────────────┤
│  Scoring      │ Review         │ Reporting        │
│  Services     │ Services       │ Services         │
├─────────────────────────────────────────────────────┤
│  Auth         │ Monitoring     │ Config Service   │
│  Services     │ Services       │                  │
└─────────────────────────────────────────────────────┘
```

### Service Communication
- **Async Communication**: Message queues (RabbitMQ/RMQ) for data flow between layers
- **Sync Communication**: REST APIs for request/response interactions (investigator UI ↔ services)
- **Shared Database**: Graph database (Neo4j) as central storage for entity/relationship data
- **Configuration Service**: Centralized configuration management for all services
- **Unified Logging**: ELK stack or similar for logs, metrics, and alerting

### Data Flow
1. Collection services → Message queue → Normalization services
2. Normalization services → Message queue → Extraction services
3. Extraction services → Message queue → Resolution services
4. Resolution services → Message queue → Correlation services
5. Correlation services → Graph database (Neo4j)
6. Scoring services ← Graph database → Review services
7. Reporting services ← Scoring/Review services ← Graph database
8. Operations services ↔ All services (cross-cutting concerns)

## Technology Stack

### Core Technologies
- **Language**: Python 3.9+ (primary), JavaScript/TypeScript (frontend)
- **Framework**: FastAPI/Flask (backend services), React/Vue.js (frontend)
- **Graph Database**: Neo4j Community Edition (recommended for MVP)
- **Message Queue**: RabbitMQ or Redis Pub/Sub
- **Cache**: Redis (for frequent queries and session storage)
- **Database**: PostgreSQL (for user management, configs, audit logs)
- **Search**: Elasticsearch (optional, for text search capabilities)
- **Frontend**: React.js with Material-UI or Vue.js with Vuetify
- **Visualization**: D3.js, vis.js, or Neo4j Bloom for graph exploration
- **Containerization**: Docker and Docker Compose (MVP), Kubernetes (production)
- **CI/CD**: GitHub Actions for automated testing and deployment

### Development & Operations
- **Version Control**: Git with GitHub hosting
- **Testing**: PyTest, Jest, Selenium/Cypress for end-to-end testing
- **Code Quality**: SonarQube, pylint, eslint
- **Documentation**: Swagger/OpenAPI for API docs, MkDocs for user docs
- **Monitoring**: Prometheus + Grafana for metrics, ELK for logs
- **Security**: OWASP ZAP, Bandit for security scanning

## Security Architecture

### Authentication & Authorization
- **Role-Based Access Control (RBAC)**: Investigator, Analyst, Admin roles
- **Secure Authentication**: JWT tokens or session-based authentication
- **Permission Granularity**: Resource-based and action-based permissions
- **Multi-Factor Authentication**: Supported for sensitive operations
- **Session Management**: Secure session handling with timeout and renewal

### Data Protection
- **Encryption-at-rest**: AES-256 for sensitive data in databases
- **Encryption-in-transit**: TLS 1.3 for all service communications
- **Key Management**: Secure key storage and rotation mechanisms
- **Data Minimization**: Collect and retain only necessary data for analysis
- **Purpose Limitation**: Strict enforcement of data usage policies

### Audit & Compliance
- **Comprehensive Logging**: All access, actions, and data modifications logged
- **Log Integrity**: Cryptographic hashing or write-once storage for logs
- **Access Reviews**: Regular review of user permissions and access patterns
- **Data Retention**: Configurable retention policies with secure deletion
- **Privacy Controls**: Anonymization/pseudonymization capabilities where needed

### Network Security
- **Service Segmentation**: Network policies limiting inter-service communication
- **Input Validation**: Strict validation of all external inputs
- **Rate Limiting**: Protection against abuse and denial-of-service
- **Secure Configuration**: Hardened service configurations and defaults
- **Vulnerability Scanning**: Regular automated security assessments

## Data Architecture

### Canonical Intelligence Schema
All data flowing through the system conforms to a canonical schema:

#### Core Entities
- **Actor**: Real-world entity being attributed (with confidence levels)
- **Alias**: Pseudonym, handle, or identifier used by an actor
- **Post**: Content item (forum post, marketplace listing, etc.)
- **OnionService**: Tor hidden service
- **ClearnetDomain**: Surface web domain
- **IPAddress**: Internet Protocol address
- **ASN**: Autonomous System Number
- **SSLCertificate**: SSL/TLS certificate
- **PGPKey**: Pretty Good Privacy encryption key
- **Wallet**: Cryptocurrency wallet address
- **Transaction**: Blockchain transaction
- **Infrastructure**: Hosting or service provider
- **BehaviourProfile**: Observed activity patterns
- **StylometricProfile**: Writing style characteristics
- **Evidence**: Raw data item with provenance and reliability
- **AttributionHypothesis**: Proposed linkage with confidence and evidence
- **Investigation**: Ongoing investigative work with timeline and notes

### Key Relationships
- Actor HAS_ALIAS Alias
- Actor AUTHORED Post
- Post MENTIONS Actor/Alias/Infrastructure/etc.
- OnionService HOSTED_AT IPAddress
- ClearnetDomain RESOLVES_TO IPAddress
- IPAddress BELONGS_TO ASN
- SSLCertificate USED_BY OnionService/ClearnetDomain
- PGPKey USED_BY Actor (for signing/posts)
- Wallet OWNED_BY Actor (with confidence)
- Transaction INVOLVES Wallet
- Infrastructure PROVIDES Hosting/Service
- BehaviourProfile DESCRIBES Actor activity patterns
- StylometricProfile DESCRIBES Actor writing style
- Evidence SUPPORTS/CONTRADICTS AttributionHypothesis
- AttributionHypothesis LINKS Actor to Evidence/Alias/etc.

### Temporal Modeling
- **Valid Time Intervals**: All entities and relationships have effective timestamps
- **Version History**: Track changes to entities over time
- **Event Sourcing**: Optional: store state changes as sequence of events
- **Snapshotting**: Periodic snapshots for performance and audit

### Provenance & Reliability
- **Source Tracking**: Every data element traces back to original source
- **Collection Method**: How data was obtained (scraped, API, etc.)
- **Timestamp**: When data was collected and when it refers to
- **Reliability Score**: Dynamic scoring based on historical accuracy
- **Confidence Intervals**: Statistical confidence where applicable
- **Evidence Grading**: Classification of evidence strength and type

## Integration Points & Contracts

### Inter-Layer APIs
Each layer exposes well-defined interfaces for interaction with adjacent layers:

#### Collection → Normalization
```
POST /normalize
{
  "raw_data": {...},
  "provenance": {
    "source": "string",
    "timestamp": "ISO datetime",
    "method": "scrape|api|tor|synthetic",
    "collector_id": "string"
  }
}
```

#### Normalization → Extraction
```
POST /extract
{
  "normalized_data": {...},
  "schema_version": "string",
  "provenance": { ... }
}
```

#### Extraction → Resolution
```
POST /resolve
{
  "entity_mentions": [...],
  "relationship_candidates": [...],
  "confidence_scores": { ... }
}
```

#### Resolution → Correlation
```
POST /correlate
{
  "resolved_entities": [...],
  "evidence": {
    "infrastructure": [...],
    "stylometric": [...],
    "behavioral": [...],
    "crypto": [...]
  }
}
```

#### Correlation → Graph
```
POST /graph/update
{
  "entities": [...],
  "relationships": [...],
  "temporal_validity": { ... }
}
```

#### Graph ←→ Scoring
```
POST /score/query
{
  "query_entity": "...",
  "evidence_types": ["infrastructure", "stylometric", ...],
  "depth": integer
}
```

```
POST /score/result
{
  "hypotheses": [...],
  "confidence_scores": { ... },
  "evidence_trails": { ... }
}
```

#### Scoring → Review
```
GET /review/hypotheses/{id}
{
  "hypothesis": {...},
  "evidence_trail": { ... },
  "confidence_breakdown": { ... },
  "alternatives": [...]
}
```

### External Integrations
- **Data Sources**: Public APIs, web scraping targets, Tor mirrors, synthetic generators
- **Threat Intelligence Feeds**: Optional integration with authorized feeds (STIX/TAXII)
- **Notification Systems**: Email, Slack, webhook alerts for anomalies and thresholds
- **DevOps Tools**: CI/CD pipelines, container registries, monitoring systems
- **Identity Providers**: LDAP/OAuth integration for enterprise authentication

## Architectural Patterns

### Modularity & Extensibility
- **Plugin Architecture**: Collectors and analyzers implemented as plugins
- **Dependency Injection**: Services depend on abstractions, not concretions
- **Configuration-Driven**: Behavior modified through configuration, not code changes
- **Feature Toggles**: Runtime enabling/disabling of features
- **Versioned APIs**: Backward compatibility through API versioning

### Reliability & Fault Tolerance
- **Circuit Breaker**: Prevents cascading failures from dependent services
- **Retry Logic**: Exponential backoff for transient failures
- **Bulkheading**: Resource isolation to prevent resource exhaustion
- **Graceful Degradation**: Reduced functionality when non-critical services fail
- **Health Checks**: Active monitoring of service availability and performance

### Scalability & Performance
- **Asynchronous Processing**: Message queues decouple service execution
- **Caching**: Redis for frequently accessed data and computations
- **Database Sharding**: Horizontal partitioning for graph database (future)
- **Read Replicas**: Separate read/write paths for scaling queries
- **Load Balancing**: Distribution of requests across service instances

### Observability
- **Structured Logging**: Consistent log format with correlation IDs
- **Distributed Tracing**: Request tracing across service boundaries
- **Metrics Collection**: Prometheus-style metrics for all services
- **Health Endpoints**: Liveness and readiness probes for each service
- **Dashboard**: Unified view of system health, performance, and business metrics

## Deployment Considerations

### Environment Parity
- **Identical Artifacts**: Same containers/images used across all environments
- **Environment Configuration**: Externalized configuration for environment-specific values
- **Database Separation**: Isolated databases for dev, test, and prod
- **Service Discovery**: Consistent mechanisms for inter-service communication

### Resource Requirements (MVP)
- **Compute**: 2-4 CPU cores, 8GB RAM
- **Storage**: 50GB SSD (database, logs, temporary files)
- **Network**: 100Mbps+ for data collection and external communication
- **Services**: 8-12 containers (collection, normalization, extraction, resolution, correlation, graph, scoring, review, reporting, auth, monitoring, config)

### Scaling Considerations
- **Horizontal Pod Autoscaling**: CPU/memory-based scaling for stateless services
- **Database Read Replicas**: For scaling graph query loads
- **Message Queue Clustering**: For high-throughput collection scenarios
- **Cache Tiering**: Local (Caffeine) + distributed (Redis) caching layers
- **CDN Integration**: For serving static assets and report files

## Evolution Path

### MVP to Production Enhancements
1. **Scaling**: Horizontal pod autoscaling, database clustering, message queue sharding
2. **Performance**: Advanced caching, query optimization, compute acceleration (GPU for ML)
3. **Security**: Hardware security modules, advanced threat detection, zero-trust networking
4. **Features**: Real-time streaming, ML model automation, collaborative investigation workspaces
5. **Integrations**: Standard threat intelligence feeds, case management systems, SIEM tools
6. **Automation**: Auto-scaling, self-healing, predictive maintenance, chaos engineering

## Decision Records

### ADR-001: Graph Database Selection
**Status**: Accepted  
**Context**: Need efficient relationship traversal for attribution analysis  
**Decision**: Selected Neo4j for its native graph storage, Cypher query language, and mature ecosystem  
**Consequences**: 
- + Excellent relationship traversal performance
- + Mature tooling and visualization options
- - Licensing considerations for enterprise features
- - Memory overhead compared to relational alternatives  

### ADR-002: Evidence Combination Framework
**Status**: Accepted  
**Context**: Need principled approach to combine multi-evidence attribution  
**Decision**: Implement Dempster-Shafer theory for evidence combination  
**Consequences**: 
- + Mathematically sound handling of uncertainty and conflicting evidence
- + Natural support for evidence weighting and reliability
- + Compatible with explainability requirements
- - Computational complexity increases with evidence sources
- - Requires careful calibration of mass functions  

### ADR-003: Communication Mechanism
**Status**: Accepted  
**Context**: Need efficient inter-service communication  
**Decision**: Hybrid approach: message queues for data flow, REST APIs for request/response  
**Consequences**: 
- + Asynchronous processing prevents blocking and builds resilience
- + REST APIs provide familiar interaction patterns for investigators
- + Clear separation of concerns between data flow and control flow
- - Increased operational complexity (managing both systems)
- - Potential latency for synchronous requests  

### ADR-004: Frontend Technology
**Status**: Accepted  
**Context**: Need responsive, maintainable investigator interface  
**Decision**: React.js with Material-UI component library  
**Consequences**: 
- + Large ecosystem and community support
- + Excellent performance and developer experience
- + Mature state management options (Redux, Context)
- - Bundle size considerations for initial load
- - Learning curve for team members unfamiliar with React  

## Conclusion
This architecture provides a solid foundation for building an evidence-driven threat actor attribution platform that meets the SIH26151 requirements. The modular, layered approach ensures separation of concerns while the end-to-end pipeline slices maintain focus on the core attribution workflow. The emphasis on explainability, provenance tracking, and evidence-based decision-making aligns with the project's goal of transparent, verifiable attribution rather than opaque automated decisions.
