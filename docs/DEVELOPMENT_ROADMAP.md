# Development Roadmap and Scopes
## SIH26151 — Dark web threat actor de-anonymization

### Overview
This document outlines the development roadmap for the SIH26151 project, defining three distinct scopes: a 48-hour proof of concept, an SIH-ready minimum viable product, and an ambitious production architecture. Each scope builds upon the previous one with clearly defined milestones, dependencies, and resource allocations.

## Scope Definitions

### SCOPE 1: 48-Hour Proof of Concept
**Objective**: Demonstrate core attribution pipeline with synthetic data in a limited timeframe
**Duration**: 48 hours of concentrated development effort
**Success Criteria**: 
- End-to-end pipeline from data collection to attribution hypothesis
- Successfully resolves at least 3 known relationships in synthetic lab
- Generates explainable attribution report with evidence trail
- Deployable and demonstrable in containerized environment

### SCOPE 2: SIH-Ready Minimum Viable Product
**Objective**: Fully functional platform meeting all SIH requirements for evaluation
**Duration**: 12-14 weeks of part-time student effort
**Success Criteria**: 
- Meets or exceeds all MVP thresholds in EVALUATION_PLAN.md
- Successfully handles all evaluation scenarios in GROUND_TRUTH.md
- Provides actionable investigative workflow with human review
- Generates exports in CSV, JSON, and report formats
- Deployable with documented procedures

### SCOPE 3: Ambitious Production Architecture
**Objective**: Production-scale platform with advanced capabilities
**Duration**: Additional 8-12 weeks beyond MVP (post-SIH)
**Success Criteria**: 
- Horizontal scaling capabilities for increased data volumes
- Advanced ML models for stylometry and behavior analysis
- Real-time streaming processing capabilities
- Enhanced visualization and collaboration features
- Integration with authorized public threat intelligence feeds

## Detailed Roadmap

### Phase 0: Preparation and Planning (Week 0)
**Objectives**: 
- Finalize project requirements and architecture
- Set up development environment and tooling
- Establish team roles and communication protocols
- Create initial backlog and sprint planning

**Activities**:
- Complete architecture and data model documentation
- Set up repositories, CI/CD pipelines, development environments
- Establish coding standards, documentation practices, and review processes
- Initial team knowledge sharing on relevant technologies
- Sprint 0 planning: backlog grooming, estimation, task breakdown

**Deliverables**:
- Finalized README, CONTRIBUTING.md, and development guidelines
- Configured development environment (Docker, IDEs, etc.)
- Established team communication channels and meeting rhythms
- Initial product backlog with prioritized features
- Definition of Done and acceptance criteria templates

**Dependencies**: None (foundational)

### Phase 1: Foundation Development (Weeks 1-4)
**Objectives**:
- Build core data pipeline (collection → normalization → extraction)
- Establish backend services and data storage
- Create basic entity resolution capabilities
- Initialize frontend dashboard framework

**Team Member Focus**:
- **Member 1**: Collector framework, web/API collectors
- **Member 2**: API gateway, Neo4j integration, basic CRUD operations
- **Member 3**: Basic entity resolution framework, initial resolution algorithms
- **Member 4**: Text preprocessing, basic stylometric feature extraction
- **Member 5**: Certificate and domain analysis basics
- **Member 6**: Basic dashboard layout, navigation, and placeholder views

**Milestones**:
- **M1.1 (End Week 2)**: Collector framework basic implementation
- **M2.1 (End Week 2)**: API gateway and basic database schema
- **M3.1 (End Week 2)**: Basic resolution framework implementation
- **M4.1 (End Week 2)**: Text preprocessing and basic feature extraction
- **M5.1 (End Week 2)**: Certificate and domain analysis basics
- **M6.1 (End Week 2)**: Basic dashboard layout and navigation
- **I1 (End Week 4)**: Collector → Normalizer pipeline functional

**Integration Point**: End-to-end data flow from collection through normalization

### Phase 2: Core Analysis Development (Weeks 5-8)
**Objectives**:
- Complete entity resolution with Fellegi-Sunter framework
- Develop stylometric and behavioral analysis capabilities
- Implement infrastructure and cryptocurrency analysis
- Build correlation engine for combining evidence
- Advance frontend visualization and hypothesis management

**Team Member Focus**:
- **Member 1**: Tor data collector, synthetic data generator, health monitoring
- **Member 2**: Caching layer, message queue integration, security controls
- **Member 3**: Fellegi-Sunter algorithm, temporal graph handling, versioning
- **Member 4**: Stylometric feature extraction, behavioral feature extraction
- **Member 5**: IP/ASN/network analysis, service analysis, crypto basics
- **Member 6**: Graph visualization, hypothesis management, evidence presentation

**Milestones**:
- **M1.2 (End Week 4)**: Web scraper and API collectors functional
- **M2.2 (End Week 4)**: CRUD operations for core entities (Actor, Alias, Post)
- **M3.2 (End Week 4)**: Fellegi-Sunter algorithm for core entity types
- **M4.2 (End Week 4)**: Stylometric feature extraction and similarity measurement
- **M5.2 (End Week 4)**: IP/ASN/network analysis implementation
- **M6.2 (End Week 4)**: Graph visualization and exploration tools
- **I2 (End Week 6)**: Normalizer → Extractor pipeline functional
- **I3 (End Week 8)**: Extractor → Resolver pipeline functional

**Integration Point**: Complete pipeline from collection through resolution

### Phase 3: Attribution and Reporting (Weeks 9-12)
**Objectives**:
- Complete scoring engine for evidence combination and attribution
- Finalize human review interface and investigator workflow
- Implement report generation and export capabilities
- Conduct integration testing and performance optimization
- Prepare for synthetic lab validation and expert review

**Team Member Focus**:
- **Member 1**: Source reliability scoring, collector optimization, final QA
- **Member 2**: Backup/recovery systems, monitoring, logging, final performance tuning
- **Member 3**: Conflict detection/resolution, query optimization, resolution validation
- **Member 4**: Classification models, uncertainty quantification, model training/evaluation systems
- **Member 5**: Address clustering, transaction analysis, wallet behavior analysis
- **Member 6**: Report generation, export functionality, authentication/authorization, audit logging, system health monitoring

**Milestones**:
- **M1.3 (End Week 6)**: Tor data and synthetic data collectors complete
- **M2.3 (End Week 6)**: Caching layer and message queue integration
- **M3.3 (End Week 6)**: Temporal graph handling and versioning
- **M4.3 (End Week 6)**: Behavioral feature extraction and analysis
- **M5.3 (End Week 6)**: Service analysis and cryptocurrency basics
- **M6.3 (End Week 6)**: Hypothesis management and evidence presentation
- **M1.4 (End Week 8)**: Source reliability and health monitoring implemented
- **M2.4 (End Week 8)**: Authentication, authorization, and security controls
- **M3.4 (End Week 8)**: Conflict detection and resolution mechanisms
- **M4.4 (End Week 8)**: Classification models and uncertainty quantification
- **M5.4 (End Week 8)**: Address clustering and transaction analysis
- **M6.4 (End Week 8)**: Report generation and export functionality
- **I4 (End Week 10)**: Correlator → Scorer pipeline functional
- **I5 (End Week 12)**: Full pipeline integration testing

**Integration Point**: Complete attribution pipeline with scoring and reporting

### Phase 4: Validation and Refinement (Weeks 13-16)
**Objectives**:
- Conduct comprehensive evaluation against synthetic lab ground truth
- Incorporate expert feedback and implement improvements
- Optimize performance and resolve critical issues
- Finalize documentation and prepare for demonstration
- Achieve SIH-ready MVP thresholds

**Team Member Focus**:
- **All Members**: Participate in evaluation, bug fixing, and optimization
- **Member 1**: Evaluation of collection effectiveness, false positive rates
- **Member 2**: Backend performance optimization, scaling preparations
- **Member 3**: Resolution accuracy tuning, false link rate reduction
- **Member 4**: Model performance optimization, explainability improvements
- **Member 5**: Infrastructure/crypto analysis tuning, precision improvements
- **Member 6**: Usability improvements, reporting clarity, investigator workflow refinement

**Milestones**:
- **M1.5 (End Week 10)**: Integration testing with normalizer (continued from Phase 1)
- **M2.5 (End Week 10)**: Backup, recovery, and monitoring systems
- **M3.5 (End Week 10)**: Graph indexing and query optimization
- **M4.5 (End Week 10)**: Model training, evaluation, and versioning systems
- **M5.5 (End Week 10)**: Wallet behavior analysis and cross-chain basics
- **M6.5 (End Week 10)**: Authentication, authorization, and audit logging
- **M1.6 (End Week 12)**: Performance optimization and error handling refinement
- **M2.6 (End Week 12)**: Performance optimization and stress testing
- **M3.6 (End Week 12)**: Performance optimization and validation testing
- **M4.6 (End Week 12)**: Performance optimization and explainability features
- **M5.6 (End Week 12)**: Performance optimization and evidence combination
- **M6.6 (End Week 12)**: System health monitoring, user feedback, and polishing
- **I6 (End Week 14)**: End-to-end scenario validation with synthetic lab
- **I7 (End Week 16)**: Expert review and feedback incorporation

**Integration Point**: Full system validation and performance optimization

### Phase 5: Preparation for Demonstration (Weeks 17-20)
**Objectives**:
- Finalize all demonstration materials and scripts
- Conduct dry runs and rehearsals
- Prepare final documentation and presentations
- Ensure all success criteria are met and documented
- Prepare for final SIH submission and presentation

**Team Member Focus**:
- **All Members**: Final preparation, documentation, and rehearsal
- **Member 1**: Synthetic lab data preparation and collection scripts
- **Member 2**: Deployment scripts, environment preparation, configuration
- **Member 3**: Resolution validation scenarios, performance benchmarks
- **Member 4**: Analysis demonstration cases, explanation scripts
- **Member 5**: Infrastructure/crypto demonstration cases, evidence trails
- **Member 6**: Dashboard demonstration scenarios, report generation, narration scripts

**Milestones**:
- **I8 (End Week 18)**: Performance optimization and stress testing
- **I9 (End Week 20)**: Expert review and feedback incorporation
- **I10 (End Week 22)**: Final preparation for demonstration
- **Final Review (Week 20)**: Comprehensive verification against SIH-ready criteria
- **Demonstration Readiness (Week 22)**: System ready for final presentation

**Integration Point**: Complete system ready for demonstration and evaluation

## Scope-Specific Milestones

### Scope 1: 48-Hour Proof of Concept Milestones
**To be completed within 48 hours of concentrated effort**:
- **SC1.1**: Basic collector fetching synthetic data
- **SC1.2**: Normalizer processing collected data
- **SC1.3**: Extractor identifying entities in normalized data
- **SC1.4**: Basic entity resolution linking related mentions
- **SC1.5**: Correlator finding basic relationships between resolved entities
- **SC1.6**: Scorer generating attribution hypothesis with confidence
- **SC1.7**: Frontend displaying hypothesis and evidence trail
- **SC1.8**: Exported attribution report in JSON format

**Success Criteria for SCOPE 1**:
- Complete pipeline from data ingestion to attribution hypothesis
- At least 3 known relationships correctly identified in synthetic data
- Explainable attribution report showing evidence trail
- Deployable using provided docker-compose configuration

### Scope 2: SIH-Ready MVP Milestones
**To be completed by end of Phase 4 (Week 16)**:
- **SC2.1**: All collection, normalization, extraction, resolution, correlation, scoring components functional
- **SC2.2**: Complete backend services with data persistence and retrieval
- **SC2.3**: Fully functional investigator dashboard with hypothesis management
- **SC2.4**: Report generation supporting CSV, JSON, and formatted reports
- **SC2.5**: Successful validation against synthetic lab ground truth meeting MVP thresholds
- **SC2.6**: Documented deployment, configuration, and operational procedures
- **SC2.7**: Comprehensive test suite covering unit, integration, and scenario tests

**MVP Success Criteria** (from EVALUATION_PLAN.md):
- Attribution Precision: ≥75% at ≥60% recall operating point
- False Attribution Rate: ≤5%
- False Link Rate: ≤10% in entity resolution
- Explainability: ≥70% of confidence traceable to evidence
- End-to-End Functionality: Complete workflow from collection to report
- Synthetic Lab Performance: Successfully resolve ≥60% of ground truth linkages

### Scope 3: Ambitious Production Architecture Milestones
**To be completed after MVP (additional 8-12 weeks)**:
- **SC3.1**: Horizontal scaling capabilities for backend services
- **SC3.2**: Advanced ML models (deep learning, ensemble methods) for stylometry/behavior
- **SC3.3**: Real-time streaming processing capabilities (Apache Kafka/Pulsar)
- **SC3.4**: Enhanced visualization with temporal playback and collaborative features
- **SC3.5**: Integration with authorized public threat intelligence feeds
- **SC3.6**: Automated hypothesis generation and testing capabilities
- **SC3.7**: Advanced performance optimization and resource management
- **SC3.8**: Comprehensive security hardening and compliance automation

**Production Success Criteria**:
- Handle 10x MVP data volume with <2x latency increase
- Support ≥50 concurrent investigators with <3s response times
- Demonstrate improved accuracy over MVP (≥10% relative improvement)
- Provide real-time processing options for streaming data sources
- Meet relevant compliance standards (GDPR, CCPA where applicable)
- Maintain or improve explainability despite increased complexity

## Resource Allocation and Timeline Visualization

### Weekly Effort Distribution (Average)
```
Week:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
M1:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
M2:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
M3:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
M4:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
M5:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
M6:    █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █   █
```

### Critical Path Dependencies
```
Collection → Normalization → Extraction → Resolution → Correlation → Scoring → Frontend/Reporting
            ↑           ↑           ↑           ↑           ↑           ↑
        Backend   Backend   Backend   Backend   Backend   Backend   Backend
```

### Parallel Work Streams
- **Weeks 1-4**: All teams work on foundational components with minimal integration dependencies
- **Weeks 5-8**: Increased integration dependencies as pipelines begin to connect
- **Weeks 9-12**: High integration dependencies as core functionality completes
- **Weeks 13-16**: Validation, optimization, and refinement with cross-team collaboration
- **Weeks 17-20**: Preparation, documentation, and demonstration readiness

## Risk Management and Mitigation

### Technical Risks and Mitigations

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Integration Delays | Medium | High | Early interface definition, bi-weekly integration tests, mock implementations |
| Performance Bottlenecks | Medium | Medium | Early benchmarking, optimization milestones, profiling sessions |
| Scope Creep | Low | High | Strict responsibility adherence, change control process, MVP focus |
| Skill Gaps | Medium | Medium | Knowledge sharing, documentation, pair programming, external resources |
| Data Quality Issues | Medium | Medium | Synthetic data validation, ground truth verification, multiple test scenarios |
| Demonstration Failure | Low | High | Dry runs, redundant systems, fallback scenarios, extensive testing |

### Dependency Management
- **Blocking Dependencies**: Clearly identified in milestone definitions
- **External Dependencies**: Documented with version requirements and fallback plans
- **Internal Dependencies**: Tracked via integration points and interface contracts
- **Risk Sharing**: Cross-team awareness of how delays impact others

### Quality Assurance
- **Continuous Integration**: Automated testing on every commit
- **Code Reviews**: Mandatory pull request reviews for all changes
- **Testing Levels**: Unit (≥80% coverage), integration, scenario, and performance testing
- **Documentation**: Living documentation updated with features
- **Retrospectives**: Bi-weekly team retrospectives for process improvement

## Success Metrics and Go/No-Go Criteria

### Scope 1 (48h PoC) Go/No-Go
**Go if**:
- Complete end-to-end pipeline demonstrated
- At least 3 synthetic relationships correctly identified
- Attribution report generated with evidence trail
- System deployable via provided instructions

**No-Go if**:
- Pipeline broken at any stage
- Cannot identify basic relationships in synthetic data
- No explainable output generated
- Deployment fails due to fundamental architecture issues

### Scope 2 (SIH-Ready MVP) Go/No-Go
**Go if**:
- Meets all MVP thresholds in EVALUATION_PLAN.md
- Successfully handles GROUND_TRUTH.md scenarios
- Provides actionable investigative workflow
- Generates required export formats (CSV, JSON, report)
- Documented deployment and operational procedures

**No-Go if**:
- Attribution precision below 75% at 60% recall
- False attribution rate above 5%
- Missing core functionality (collection through reporting)
- Unable to deploy or operate as documented
- Fundamental ethical/legal compliance issues

### Scope 3 (Production) Considerations
**Consider undertaking if**:
- MVP successfully demonstrated and evaluated
- Clear path to scaling and performance improvements
- Available resources and time beyond SIH requirements
- Defined use cases justifying increased complexity
- Stakeholder agreement on extended development scope

## Conclusion
This roadmap provides a structured approach to developing the SIH26151 platform, breaking the work into manageable phases with clear milestones and success criteria. By defining three distinct scopes (48-hour PoC, SIH-ready MVP, and ambitious production architecture), the team can focus on delivering incremental value while maintaining flexibility to adapt based on progress and feedback. The emphasis on integration points, validation against synthetic ground truth, and preparation for demonstration ensures that the team will deliver a technically credible platform capable of evidence-driven threat actor attribution.