# Team Work Breakdown and Responsibilities
## SIH26151 — Dark web threat actor de-anonymization

### Overview
This document outlines the division of responsibilities among the six-person student team for the SIH26151 project. Each team member has primary ownership of a functional area with clearly defined interfaces, deliverables, dependencies, and milestones. The structure enables parallel development while ensuring integration compatibility.

### Team Structure and Roles

| Team Member | Primary Role | Secondary Support Areas |
|-------------|--------------|-------------------------|
| Member 1 | Collection + Ingestion | Normalization, Data Validation |
| Member 2 | Backend + Data Engineering | Graph Database, API Design |
| Member 3 | Graph + Entity Resolution | Resolution Algorithms, Conflict Handling |
| Member 4 | NLP + Stylometry + Behaviour | Feature Extraction, Model Training |
| Member 5 | Infrastructure + Crypto Intelligence | Certificate Analysis, Blockchain |
| Member 6 | Frontend + Visualization + Integration | Investigator Dashboard, Reporting |

### Detailed Responsibilities

## 1. Collection + Ingestion (Team Member 1)

**Objective**: Build robust, extensible data acquisition system capable of gathering information from diverse sources while maintaining ethical and legal compliance.

### Core Responsibilities
- Design and implement plugin-based collector architecture
- Create collectors for: Web scraping, API ingestion, Tor data, synthetic data generation
- Implement source reliability tracking and validation
- Develop rate limiting and etiquette mechanisms
- Build error handling and retry logic
- Create data quarantine and validation systems
- Implement-provenance tracking from point of collection

### Interfaces
- **Output to Normalizer**: Raw data objects with provenance metadata (JSON format)
- **Input from Configuration**: Source lists, collection schedules, rate limits
- **Input from Monitoring System**: Health status, performance metrics
- **Output to Alerting System**: Collection failures, anomalies, performance issues

### Deliverables
- Collector framework with plugin interface
- Web scraper collector (respecting robots.txt, rate limits)
- API collector for authorized sources (Reddit, Twitter APIs, etc.)
- Tor data collector (consensus, descriptors from public mirrors)
- Synthetic data generator for lab environments
- Source reliability scoring system
- Collector health monitoring and reporting
- Data validation and quarantine system
- Collection scheduler and orchestrator

### Dependencies
- **Depends On**: None (foundational layer)
- **Blocking**: Normalizer cannot function without collector output
- **External Dependencies**: Target data sources, public APIs, Tor network (public aspects only)

### Milestones
- **M1.1 (Week 2)**: Collector framework basic implementation
- **M1.2 (Week 4)**: Web scraper and API collectors functional
- **M1.3 (Week 6)**: Tor data and synthetic data collectors complete
- **M1.4 (Week 8)**: Source reliability and health monitoring implemented
- **M1.5 (Week 10)**: Integration testing with normalizer
- **M1.6 (Week 12)**: Performance optimization and error handling refinement

### Success Criteria
- Collect data from ≥3 different source types
- Maintain <5% collection error rate
- Implement proper rate limiting and source etiquette
- Provide complete provenance metadata with all collected data
- Handle source failures gracefully with appropriate retry logic

## 2. Backend + Data Engineering (Team Member 2)

**Objective**: Build scalable backend services and data infrastructure to support the platform's analytical components.

### Core Responsibilities
- Design and implement RESTful APIs for inter-service communication
- Implement data storage solutions (primary: Neo4j graph database)
- Create data modeling and schema management systems
- Implement caching layers for performance optimization
- Build data pipeline orchestration and workflow management
- Develop backup, recovery, and data retention systems
- Implement security controls (authentication, authorization, encryption)
- Create monitoring, logging, and alerting systems

### Interfaces
- **Input from Collector**: Raw data via message queue or direct API
- **Output to Normalizer**: Normalized data storage and retrieval
- **Input/Output to Extractor**: Entity mention storage and retrieval
- **Input/Output to Resolver**: Resolved entity storage and retrieval
- **Input/Output to Correlator**: Correlation result storage and retrieval
- **Input/Output to Scorer**: Attribution hypothesis storage and retrieval
- **Output to Frontend**: API endpoints for dashboard and reporting
- **Input from DevOps**: Deployment configuration, scaling parameters

### Deliverables
- RESTful API gateway with versioning
- Neo4j graph database integration and schema design
- Data access layer with CRUD operations for all entity types
- Caching layer (Redis) for frequent queries
- Message queue system (RabbitMQ/RMQ) for asynchronous processing
- Pipeline orchestrator for data flow management
- Authentication and authorization system (RBAC)
- Encryption-at-rest and TLS-in-transit implementation
- Backup and disaster recovery procedures
- Monitoring, logging, and alerting system (ELK stack or similar)
- API documentation and SDK for internal services

### Dependencies
- **Depends On**: Collector output (for data to store)
- **Blocking**: All other components depend on backend for data persistence
- **External Dependencies**: Neo4j, Redis, RabbitMQ, monitoring tools

### Milestones
- **M2.1 (Week 2)**: API gateway and basic database schema
- **M2.2 (Week 4)**: CRUD operations for core entities (Actor, Alias, Post)
- **M2.3 (Week 6)**: Caching layer and message queue integration
- **M2.4 (Week 8)**: Authentication, authorization, and security controls
- **M2.5 (Week 10)**: Backup, recovery, and monitoring systems
- **M2.6 (Week 12)**: Performance optimization and stress testing

### Success Criteria
- All entities and relationships persist correctly in graph database
- API responds to requests within <200ms for 95% of cases
- System handles expected data volume with <2s latency
- Security controls prevent unauthorized access
- Backup and recovery procedures tested and functional
- Monitoring system provides actionable alerts

## 3. Graph + Entity Resolution (Team Member 3)

**Objective**: Build accurate entity disambiguation system and efficient graph storage/querying capabilities.

### Core Responsibilities
- Implement probabilistic entity resolution (Fellegi-Sunter framework)
- Develop relationship resolution and confidence scoring
- Design graph schema optimization for CTI queries
- Implement graph algorithms for path finding and pattern detection
- Create temporal graph handling capabilities
- Develop entity versioning and history tracking
- Build conflict detection and resolution mechanisms
- Implement graph indexing and query optimization strategies

### Interfaces
- **Input from Extractor**: Entity mentions and relationship candidates
- **Output to Correlator**: Resolved entities with confidence scores
- **Input/Output to Backend**: Graph storage and retrieval operations
- **Input from Config**: Resolution parameters, confidence thresholds
- **Output to Monitoring**: Resolution metrics, performance data
- **Input from Human Review**: Manual resolution corrections and feedback

### Deliverables
- Probabilistic resolution engine (Fellegi-Sunter implementation)
- Confidence scoring system for entity relationships
- Graph schema optimized for CTI query patterns
- Temporal graph handling (valid time intervals)
- Entity versioning and history tracking system
- Conflict detection and resolution mechanisms
- Graph indexing strategy for common query patterns
- Query optimization and performance tuning
- Resolution validation and testing framework
- Integration layer with backend data services

### Dependencies
- **Depends On**: Extractor output (entity mentions to resolve)
- **Blocking**: Correlator and Scorer depend on resolved entities
- **External Dependencies**: Graph database (Neo4j), resolution libraries

### Milestones
- **M3.1 (Week 2)**: Basic resolution framework implementation
- **M3.2 (Week 4)**: Fellegi-Sunter algorithm for core entity types
- **M3.3 (Week 6)**: Temporal graph handling and versioning
- **M3.4 (Week 8)**: Conflict detection and resolution mechanisms
- **M3.5 (Week 10)**: Graph indexing and query optimization
- **M3.6 (Week 12)**: Performance optimization and validation testing

### Success Criteria
- Achieve ≥80% precision and ≥75% recall on synthetic lab resolution tasks
- Maintain false link rate <5%
- Handle temporal entity evolution correctly
- Provide explainable resolution decisions with evidence tracing
- Scale to handle expected entity volumes with acceptable performance

## 4. NLP + Stylometry + Behaviour (Team Member 4)

**Objective**: Implement natural language processing, stylometric analysis, and behavioral analysis capabilities for author identification and pattern detection.

### Core Responsibilities
- Implement text preprocessing and normalization pipelines
- Develop stylometric feature extraction (character n-grams, word n-grams, etc.)
- Create behavioral feature extraction from activity data
- Implement similarity measurement and classification algorithms
- Develop model training, evaluation, and updating capabilities
- Create uncertainty quantification and confidence scoring
- Implement feature importance and explainability mechanisms
- Build model versioning and A/B testing capabilities

### Interfaces
- **Input from Normalizer**: Text content (posts, messages, etc.)
- **Input from Extractor**: Entity mentions requiring analysis
- **Output to Correlator**: Stylistic and behavioral similarity scores
- **Input from Config**: Model parameters, feature selections, thresholds
- **Output to Monitoring**: Model performance, training metrics
- **Input from Human Review**: Feedback on analysis results
- **Output to Scorer**: Feature vectors and similarity scores for attribution

### Deliverables
- Text preprocessing pipeline (cleaning, normalization, tokenization)
- Stylometric feature extraction library (n-grams, TF-IDF, etc.)
- Behavioral feature extraction module (temporal patterns, activity cycles)
- Similarity measurement algorithms (cosine, euclidean, custom metrics)
- Classification and clustering models for authorship detection
- Uncertainty quantification system (confidence intervals, calibration)
- Feature importance and explainability tools
- Model training and evaluation framework
- Model versioning and update system
- Integration layer with correlation and scoring components

### Dependencies
- **Depends On**: Normalizer output (text content to analyze)
- **Blocking**: Correlator depends on stylistic/behavioral similarity scores
- **External Dependencies**: NLP libraries (spaCy, NLTK, scikit-learn), ML frameworks

### Milestones
- **M4.1 (Week 2)**: Text preprocessing and basic feature extraction
- **M4.2 (Week 4)**: Stylometric feature extraction and similarity measurement
- **M4.3 (Week 6)**: Behavioral feature extraction and analysis
- **M4.4 (Week 8)**: Classification models and uncertainty quantification
- **M4.5 (Week 10)**: Model training, evaluation, and versioning systems
- **M4.6 (Week 12)**: Performance optimization and explainability features

### Success Criteria
- Achieve ≥70% precision and ≥60% recall on stylometry tasks (adjusted for short text)
- Achieve ≥65% precision and ≥55% recall on behavioral analysis tasks
- Provide explainable analysis results with feature contribution tracking
- Maintain model uncertainty quantification and calibration
- Handle concept drift and style evolution appropriately

## 5. Infrastructure + Crypto Intelligence (Team Member 5)

**Objective**: Implement infrastructure analysis and cryptocurrency intelligence capabilities for correlation and attribution.

### Core Responsibilities
- Implement SSL/TLS certificate analysis and correlation
- Develop domain and DNS analysis capabilities
- Create IP address, ASN, and hosting provider analysis
- Implement service banner and header analysis
- Develop cryptocurrency address clustering and transaction analysis
- Implement blockchain heuristics (co-spend, change address, etc.)
- Create wallet behavior and temporal pattern analysis
- Implement cross-chain analysis capabilities (if applicable)
- Develop infrastructure evidence combination and scoring

### Interfaces
- **Input from Normalizer**: Infrastructure data (certificates, DNS records, etc.)
- **Input from Extractor**: Infrastructure entity mentions
- **Output to Correlator**: Infrastructure and crypto correlation scores
- **Input from Config**: Analysis parameters, heuristics, thresholds
- **Output to Monitoring**: Analysis performance, detection rates
- **Input from Human Review**: Feedback on infrastructure/crypto analysis
- **Output to Scorer**: Feature vectors and correlation scores for attribution

### Deliverables
- SSL/TLS certificate analysis and correlation module
- Domain and DNS analysis and correlation module
- IP address, ASN, and hosting provider analysis module
- Service banner and header analysis module
- Cryptocurrency address clustering engine (țineur, change address heuristics)
- Transaction graph analysis and pathfinding module
- Wallet behavior and temporal pattern analysis
- Cross-chain analysis capabilities (basic implementation)
- Infrastructure evidence scoring and combination system
- Integration layer with correlation and scoring components

### Dependencies
- **Depends On**: Normalizer output (infrastructure data to analyze)
- **Blocking**: Correlator depends on infrastructure and crypto correlation scores
- **External Dependencies**: Cryptocurrency libraries (bitcoinlib, web3.py), SSL/DNS libraries

### Milestones
- **M5.1 (Week 2)**: Certificate and domain analysis basics
- **M5.2 (Week 4)**: IP/ASN/network analysis implementation
- **M5.3 (Week 6)**: Service analysis and cryptocurrency basics
- **M5.4 (Week 8)**: Address clustering and transaction analysis
- **M5.5 (Week 10)**: Wallet behavior analysis and cross-chain basics
- **M5.6 (Week 12)**: Performance optimization and evidence combination

### Success Criteria
- Achieve ≥75% precision and ≥65% recall on infrastructure correlation tasks
- Achieve ≥80% precision on wallet address linkage tasks (strong evidence)
- Provide explainable infrastructure and crypto analysis results
- Handle privacy techniques and obfuscation appropriately
- Scale to handle expected infrastructure data volumes

## 6. Frontend + Visualization + Integration (Team Member 6)

**Objective**: Build intuitive investigator dashboard and visualization capabilities for interacting with the platform's analytical outputs.

### Core Responsibilities
- Design and implement investigator dashboard interface
- Create graph visualization and exploration capabilities
- Implement hypothesis management and tracking systems
- Develop evidence presentation and explanation tools
- Build report generation and export functionality (CSV, JSON, reports)
- Implement user authentication, authorization, and audit logging
- Develop system health monitoring and status displays
- Create user feedback and annotation mechanisms
- Implement integration testing and validation frameworks

### Interfaces
- **Input from Scorer**: Attribution hypotheses and confidence scores
- **Input from Graph**: Entity and relationship data for visualization
- **Input from Human Review**: User actions, feedback, annotations
- **Output to Human Review**: Investigation results, evidence trails, visualizations
- **Input from Config**: UI preferences, display options, feature flags
- **Output to Monitoring**: Usage metrics, performance data, error reports
- **Input from DevOps**: Deployment configuration, scaling parameters

### Deliverables
- Investigator dashboard with multiple views (entity, hypothesis, evidence)
- Interactive graph visualization and exploration tool
- Hypothesis management system (creation, tracking, updating)
- Evidence presentation and explanation system (trails, contributions)
- Report generation engine (CSV, JSON, formatted reports)
- User authentication and authorization system (RBAC)
- Comprehensive audit logging system
- System health monitoring and status displays
- User feedback, annotation, and collaboration mechanisms
- Integration testing framework (end-to-end scenario validation)
- User documentation and help system

### Dependencies
- **Depends On**: Scorer output (attribution hypotheses to display)
- **Blocking**: Human review and reporting depend on frontend output
- **External Dependencies**: Frontend framework (React/Vue.js), visualization libraries (D3.js, vis.js, etc.)

### Milestones
- **M6.1 (Week 2)**: Basic dashboard layout and navigation
- **M6.2 (Week 4)**: Graph visualization and exploration tools
- **M6.3 (Week 6)**: Hypothesis management and evidence presentation
- **M6.4 (Week 8)**: Report generation and export functionality
- **M6.5 (Week 10)**: Authentication, authorization, and audit logging
- **M6.6 (Week 12)**: System health monitoring, user feedback, and polishing

### Success Criteria
- Enable investigators to complete typical workflows in <30 minutes
- Provide clear visualization of attribution evidence and confidence
- Support hypothesis tracking and evidence annotation
- Generate actionable reports in multiple formats
- Maintain responsive interface (<2s response time for 95% of actions)
- Provide comprehensive audit trail for all user actions

### Cross-Team Integration Points

#### Integration Milestones
- **I1 (Week 4)**: Collector → Normalizer pipeline functional
- **I2 (Week 6)**: Normalizer → Extractor pipeline functional
- **I3 (Week 8)**: Extractor → Resolver pipeline functional
- **I4 (Week 10)**: Resolver → Correlator pipeline functional
- **I5 (Week 12)**: Correlator → Scorer pipeline functional
- **I6 (Week 14)**: Full pipeline integration testing
- **I7 (Week 16)**: End-to-end scenario validation with synthetic lab
- **I8 (Week 18)**: Performance optimization and stress testing
- **I9 (Week 20)**: Expert review and feedback incorporation
- **I10 (Week 22)**: Final preparation for demonstration

#### Communication Protocols
- **Async Communication**: Message queues (RabbitMQ/RMQ) for data flow between teams
- **Sync Communication**: REST APIs for request/response interactions
- **Shared Database**: Graph database as central storage for all teams
- **Configuration Service**: Centralized configuration management
- **Monitoring System**: Unified logging, metrics, and alerting
- **Documentation**: Shared API contracts and data models

### Risk Management and Dependencies

#### Risk: Integration Delays
- **Mitigation**: Early definition of interfaces and contracts
- **Mitigation**: Regular integration testing (bi-weekly)
- **Mitigation**: Use of mock implementations for early development
- **Mitigation**: Clear escalation path for blocking dependencies

#### Risk: Scope Creep
- **Mitigation**: Strict adherence to defined responsibilities
- **Mitigation**: Change control process for responsibility adjustments
- **Mitigation**: Regular review of deliverables against milestones
- **Mitigation**: Focus on MVP before stretch goals

#### Risk: Skill Gaps
- **Mitigation**: Peer knowledge sharing sessions
- **Mitigation**: Documentation and code standards enforcement
- **Mitigation**: External learning resources and tutorials
- **Mitigation**: Pair programming and code reviews for knowledge transfer

#### Risk: Performance Bottlenecks
- **Mitigation**: Early performance benchmarking
- **Mitigation**: Optimization built into milestones rather than afterthought
- **Mitigation**: Regular profiling and optimization sessions
- **Mitigation**: Clear performance budgets for each component

### Decision Making and Conflict Resolution

#### Technical Disagreements
- **Process**: Data-driven decision making (benchmarks, prototypes)
- **Escalation Path**: Team discussion → Expert consultation → Vote
- **Documentation**: Record decisions and rationale in project wiki
- **Timeboxing**: Limit discussion time to prevent stagnation

#### Priority Conflicts
- **Process**: Impact vs Effort analysis (value delivery focus)
- **Escalation Path**: Team discussion → Stakeholder input → Democratic decision
- **Documentation**: Maintain transparent priority backlog
- **Review Frequency**: Bi-weekly priority review and adjustment

### Conclusion
This team structure enables parallel development while ensuring integration compatibility through clearly defined responsibilities, interfaces, and milestones. Each team member has ownership of a critical functional area with explicit deliverables and success criteria. The emphasis on integration points and regular synchronization ensures that the six components work together cohesively to achieve the SIH26151 objectives of a technically credible, evidence-driven threat actor attribution platform.