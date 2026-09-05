# Use Cases
## SIH26151 — Dark web threat actor de-anonymization

## Primary Actors
- **Investigator**: Law enforcement or cybersecurity analyst using the platform
- **System**: DRISHTI threat actor attribution platform
- **Data Source**: Websites, APIs, Tor services, synthetic data generators
- **Synthetic Lab**: Controlled dark web environment with known ground truth

## Use Case Diagrams (Textual Descriptions)

### UC-1: Collect Intelligence Data
**Goal**: Gather data from diverse sources for analysis  
**Primary Actor**: Investigator (via configured collection jobs)  
**Preconditions**: Collection sources configured, scheduler active  
**Postconditions**: Raw data collected with provenance metadata stored in system  

**Main Success Scenario**:
1. Investigator configures collection sources (web scrapers, API collectors, Tor/synthetic data)
2. Investigator sets collection schedules and rate limits
3. System activates collectors according to schedule
4. Collectors gather data from target sources
5. Collectors apply rate limiting and etiquette protocols
6. System validates collected data and applies source reliability scoring
7. System stores raw data objects with complete provenance metadata
8. System notifies investigator of collection completion or failures  

**Extensions**:
- 3a. Source unavailable: System applies retry logic with exponential backoff
- 3b. Rate limit exceeded: System pauses collection and resumes after wait period
- 3c. Malformed data received: System quarantines invalid data for investigation
- 6a. Low reliability source detected: System reduces weight of data in subsequent analysis  

### UC-2: Normalize and Validate Data
**Goal**: Standardize collected data to common schema and validate integrity  
**Primary Actor**: System (automated process)  
**Preconditions**: Raw data stored in system from collection phase  
**Postconditions**: Normalized data stored in canonical intelligence schema  

**Main Success Scenario**:
1. System retrieves raw data objects from storage
2. System identifies data format and source type
3. System applies appropriate normalization transforms for source/format
4. System validates data integrity and completeness against schema
5. System detects and marks duplicate records
6. System identifies and flags malformed/invalid data entries
7. System converts data to canonical intelligence schema format
8. System preserves provenance metadata throughout normalization
9. System stores normalized data and updates processing metrics  

**Extensions**:
- 4a. Validation fails: System routes data to quarantine for manual review
- 5a. Duplicates detected: System links duplicates and maintains single canonical record
- 6a. Malformed data: System attempts repair if possible, otherwise flags for review  

### UC-3: Extract Entities and Relationships
**Goal**: Identify mentions of actors, aliases, infrastructure, and relationships in text  
**Primary Actor**: System (automated process)  
**Preconditions**: Normalized text data available in system  
**Postconditions**: Entity mentions and relationship candidates extracted with confidence scores  

**Main Success Scenario**:
1. System retrieves normalized text data (posts, messages, descriptions)
2. System applies text preprocessing (cleaning, normalization, tokenization)
3. System extracts entity mentions using pattern matching and NLP techniques
4. System identifies relationship candidates based on co-mention, proximity, etc.
5. System calculates confidence scores for extractions
6. System applies confidence calibration to align scores with empirical accuracy
7. System stores entity mentions and relationship candidates with provenance  
8. System updates extraction performance metrics  

**Extensions**:
- 3a. Low confidence extraction: System flags for investigator review
- 3b. Ambiguous entity type: System provides multiple candidate types with scores
- 3c. New entity pattern detected: System logs pattern for potential rule addition  

### UC-4: Resolve Entity Identities
**Goal**: Disambiguate and link entity mentions to resolved entities  
**Primary Actor**: System (automated process)  
**Preconditions**: Entity mentions and relationship candidates extracted  
**Postconditions**: Resolved entities with confidence scores and version history  

**Main Success Scenario**:
1. System retrieves entity mentions requiring resolution
2. System generates candidate resolved entities for each mention
3. System compares evidence vectors between mentions and candidates
4. System applies Fellegi-Sunter probabilistic matching algorithm
5. System calculates match weights and resolves entities above threshold
6. System detects and flags conflicting evidence for investigation
7. System creates/maintains resolved entities with version history
8. System stores resolution decisions with evidence tracing
9. System updates resolution performance metrics and logs  

**Extensions**:
- 4a. Low confidence match: System creates tentative resolved entity for review
- 4b. Conflicting evidence: System flags for investigator conflict resolution
- 4c. Temporal evidence: System handles entity evolution and versioning correctly  

### UC-5: Correlate Multi-Source Evidence
**Goal**: Analyze patterns and relationships between resolved entities across evidence types  
**Primary Actor**: System (automated process)  
**Preconditions**: Resolved entities available from resolution phase  
**Postconditions**: Correlation scores and relationship evidence stored  

**Main Success Scenario**:
1. System retrieves resolved entities and their associated evidence
2. System analyzes infrastructure evidence (certificates, domains, IPs, ASNs)
3. System analyzes stylometric evidence (writing style, n-grams, TF-IDF)
4. System analyzes behavioral evidence (temporal patterns, activity cycles)
5. System analyzes cryptocurrency evidence (wallet transactions, clustering)
6. System combines evidence to calculate correlation scores between entities
7. System identifies strengthened, weakened, or new relationships
8. System stores correlation results with evidence provenance
9. System updates correlation performance metrics  

**Extensions**:
- 2a-5a. Evidence type missing: System uses available evidence types with reduced confidence
- 6a. Conflicting correlations: System flags relationships with contradictory evidence
- 6a. Novel pattern detected: System logs pattern for potential rule addition  

### UC-6: Build and Query Knowledge Graph
**Goal**: Store resolved entities and relationships in graph for traversal and analysis  
**Primary Actor**: System (automated process)  
**Preconditions**: Resolved entities and correlation data available  
**Postconditions**: Entities and relationships stored in graph database  

**Main Success Scenario**:
1. System retrieves resolved entities and correlation data
2. System maps entities to graph nodes with properties and provenance
3. System maps relationships to graph edges with types, confidence, and evidence
4. System stores temporal validity intervals for entities and relationships
5. System creates graph indexes for common query patterns
6. System stores graph and enables traversal/path finding operations
7. System updates graph storage and indexing metrics  

**Extensions**:
- 2a. New entity type: System extends graph schema dynamically
- 3a. New relationship type: System extends relationship catalog
- 4a. Temporal data: System manages valid time intervals for entities/relationships  

### UC-7: Generate Attribution Hypotheses
**Goal**: Combine evidence to create confidence-weighted attribution hypotheses  
**Primary Actor**: System (automated process)  
**Preconditions**: Graph contains resolved entities, relationships, and evidence  
**Postconditions**: Attribution hypotheses generated with evidence trails  

**Main Success Scenario**:
1. System receives attribution query (entity, alias, infrastructure, etc.)
2. System retrieves relevant subgraph from knowledge graph
3. System collects evidence from all available types for candidates
4. System aggregates evidence using principled confidence model (Dempster-Shafer/Bayesian)
5. System calculates confidence scores for each attribution hypothesis
6. System preserves evidence trails showing contribution of each evidence type
7. System identifies supporting and contradictory evidence for each hypothesis
8. System ranks hypotheses by confidence and stores with full evidence traceability
9. System updates attribution performance and calibration metrics  

**Extensions**:
- 4a. Missing evidence type: System adjusts confidence model accordingly
- 5a. Low confidence: System flags hypothesis for investigator review
- 5a. High uncertainty: System provides uncertainty quantification with hypothesis
- 7a. Conflicting evidence: System highlights contradictions in evidence trail  

### UC-8: Investigator Review and Validation
**Goal**: Enable investigators to review, validate, and refine attribution hypotheses  
**Primary Actor**: Investigator  
**Preconditions**: Attribution hypotheses generated and available for review  
**Postconditions**: Investigator feedback recorded, hypotheses updated as needed  

**Main Success Scenario**:
1. Investigator accesses attribution hypothesis dashboard
2. Investigator selects hypothesis for review
3. System displays hypothesis with confidence score and evidence trail
4. Investigator examines supporting and contradictory evidence
5. Investigator traces evidence back to raw data sources
6. Investigator validates or refutes hypothesis based on evidence examination
7. Investigator provides feedback, annotations, or alternative hypotheses
8. System records investigator actions and updates hypothesis status
9. System uses feedback to adjust confidence models or evidence weights (if configured)  
10. System updates investigation workflow metrics  

**Extensions**:
- 4a. Insufficient evidence: Investigator requests additional collection or analysis
- 4a. Ambiguous evidence: Investigator requests clarification or additional sources
- 7a. Feedback indicates model issue: System flags for potential confidence model adjustment  
- 7a. Feedback indicates missing evidence: System identifies gaps for future collection  

### UC-9: Generate Intelligence Reports
**Goal**: Create actionable intelligence reports in multiple formats  
**Primary Actor**: Investigator  
**Preconditions**: Attribution hypotheses reviewed and validated (optional)  
**Postconditions**: Intelligence reports generated and available for export  

**Main Success Scenario**:
1. Investigator selects attribution hypothesis or investigation for reporting
2. Investigator chooses report format (CSV, JSON, formatted report)
3. Investigator configures report content and detail level
4. System collects hypothesis data, evidence trails, and metadata
5. System formats report according to selected template and format
6. System includes provenance, timestamps, and investigator annotations
7. System generates report and makes available for download/export
8. System logs report generation for audit trail  
9. System updates reporting metrics  

**Extensions**:
- 2a. Custom report: Investigator specifies custom fields and layout
- 3a. Scheduled report: System generates report automatically per schedule
- 3a. Alert-based report: System generates report when threshold conditions met  
- 5a. Large dataset: System provides pagination or incremental generation  

### UC-10: Evaluate Against Synthetic Lab
**Goal**: Validate system performance against known ground truth  
**Primary Actor**: System/Evaluation Framework  
**Preconditions**: Synthetic dark web lab data available with ground truth  
**Postconditions**: Performance metrics calculated and documented  

**Main Success Scenario**:
1. Evaluation framework loads synthetic data with known ground truth
2. System processes synthetic data through full attribution pipeline
3. System generates attribution hypotheses and investigation results
4. Evaluation framework compares system outputs to ground truth
5. System calculates metrics: precision, recall, F1-score, false positive rates
6. System evaluates explainability and evidence traceability
7. System measures temporal analysis and concept drift handling
8. System documents performance against MVP thresholds and stretch goals
9. Evaluation framework provides recommendations for improvement  

**Extensions**:
- 2a. Component evaluation: Individual subsystems tested in isolation
- 2a. Ablation studies: Specific evidence types or components withheld
- 2a. Hold-out validation: Portion of synthetic data reserved for final testing
- 2a. Temporal validation: Train on earlier data, test on later data  

## Use Case Summary

The SIH26151 platform supports the complete threat actor attribution lifecycle:
1. **Data Acquisition**: Collection from diverse sources with provenance tracking
2. **Data Preparation**: Normalization, validation, and standardization
3. **Evidence Extraction**: Entity and relationship identification from text
4. **Identity Resolution**: Probabilistic disambiguation of entity mentions
5. **Multi-Source Correlation**: Pattern detection across evidence types
6. **Knowledge Representation**: Graph storage for relationship traversal
7. **Attribution Generation**: Evidence-weighted hypothesis creation with explainability
8. **Human Review**: Investigator validation and feedback loop
9. **Intelligence Production**: Actionable reporting in multiple formats
10. **Validation & Improvement**: Performance measurement against ground truth

Each use case emphasizes evidence-driven, explainable approaches rather than opaque automated decisions, ensuring investigators can trace conclusions back to verifiable evidence elements.
