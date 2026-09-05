# Technical Methodologies
## SIH26151 — Dark web threat actor de-anonymization

### Data Collection Methodologies

#### Passive Tor Hidden Service Enumeration
- **APPROACH": Collect hidden service descriptors from public sources without direct interaction
- **TECHNIQUES": 
  - Consensus and descriptor downloads from Tor directory authorities (public mirrors)
  - Certificate Transparency logs for .onion domain certificates
  - Passive DNS monitoring for onion service-related clearnet domains
  - Web crawling of surface web sites that reference .onion addresses
- **TOOLS": 
  - OnionScan for service analysis once discovered
  - Custom scripts for consensus parsing and descriptor extraction
  - ctfr (Certificate Transparency Feed Reader) for CT log monitoring
- **VALIDATION": 
  - Compare discovered services against known public indexes (Ahmia, etc.)
  - Measure rediscovery rate of established services
  - Validate with synthetic service deployment in controlled environment

#### Authorized Web Scraping for Surface Web References
- **APPROACH": Collect public discussions and references to dark web activities on surface web platforms
- **TECHNIQUES": 
  - Forum scraping (Reddit, specialized forums) with rate limiting and respect for robots.txt
 
  - Social media monitoring (Twitter/X, Mastodon) using public APIs
  - Paste site monitoring (Pastebin, GitHub Gists) for leaked credentials or configurations
  - Security blog and news article aggregation
- **TOOLS": 
  - Custom scrapers with session management and user-agent rotation
  - Official APIs where available (Reddit API, Twitter API v2)
  - HTML parsing libraries (BeautifulSoup, lxml, cheerio)
  - Natural language processing for entity extraction from text
- **VALIDATION": 
  - Cross-reference with known threat intelligence reports
  - Manual sampling to verify relevance and accuracy
  - Compare volume and timing with established intelligence feeds

#### Synthetic Data Generation for Controlled Evaluation
- **APPROACH": Create artificial dark web ecosystem with known ground truth for system validation
- **TECHNIQUES": 
  - Markov chain and LLM-assisted text generation for forum/marketplace posts
  - Network graph generators for vendor-buyer and service relationships
  - Cryptocurrency transaction simulators for blockchain activity
  - Template-based service generation with configurable characteristics
- **TOOLS": 
  - Python libraries: numpy, pandas, networkx, faker, markovify
  - Custom generators for specific data types (posts, transactions, service descriptors)
  - Docker containers for isolated service deployment (for advanced testing)
- **VALIDATION": 
  - Verify ground truth matches generated data
  - Test system's ability to recover known relationships
  - Measure false positive and false negative rates against synthetic baseline

### Data Normalization and Processing

#### Structured Data Extraction from Unstructured Sources
- **APPROACH": Parse heterogeneous data formats into common schema
- **TECHNIQUES": 
  - Regular expressions and pattern matching for structured fields (emails, wallet addresses, etc.)
  - Named Entity Recognition (NER) for extracting persons, organizations, locations
  - Template matching for known data formats (PGP keys, SSL certificates, etc.)
  - Machine learning classifiers for categorizing content types
- **TOOLS": 
  - spaCy, NLTK for NLP processing
  - regex libraries with performance optimization
  - Custom parsers for specific formats (JSON, XML, CSV, raw text)
  - Hashing algorithms for content deduplication (SHA-256, MD5 for non-security purposes)
- **VALIDATION": 
  - Precision and recall metrics against manually labeled samples
  - Consistency checks across multiple extraction methods
  - Downstream impact analysis on entity resolution accuracy

#### Temporal Normalization and Timezone Handling
- **APPROACH": Standardize timestamps for accurate temporal analysis
- **TECHNIQUES": 
  - Parse diverse timestamp formats (ISO 8601, Unix epoch, RFC 2822, etc.)
  - Convert to UTC for internal storage and comparison
  - Preserve original timezone information for display and context
  - Handle missing or ambiguous timestamps with uncertainty markers
- **TOOLS": 
  - Python datetime and dateutil libraries
  - Pandas for time series operations
  - Custom timezone handling with pytz/zoneinfo
- **VALIDATION": 
  - Verify chronological ordering preservation
  - Test timezone conversion accuracy
  - Validate temporal queries against known sequences

### Entity Extraction and Identification

#### Hard Identifier Extraction
- **APPROACH": Extract definitive, low-collision identifiers from collected data
- **IDENTIFIER TYPES": 
  - Cryptographic fingerprints (PGP keys, SSL certificate hashes)
  - Blockchain addresses (Bitcoin, Ethereum, etc. with format validation)
  - Unique usernames/handles with platform context
  - Email addresses with domain validation
  - Hardware identifiers (when legally and ethically permissible)
- **EXTRACTION METHODS": 
  - Format-specific validators (Base58Check for Bitcoin, bech32 for newer formats)
  - Cryptographic library verification (python-gnupg for PGP, cryptography for SSL/TLS)
  - Regex patterns with checksum validation where applicable
  - Contextual filtering (e.g., distinguishing payment addresses from transaction IDs)
- **CONFIDENCE": 
  - High confidence (0.9-1.0) for verified cryptographic identifiers
  - Medium confidence (0.7-0.9) for format-valid but unverified identifiers
  - Low confidence (<0.7) for identifiers requiring additional corroboration

#### Soft Signal Feature Extraction
- **APPROACH": Extract probabilistic indicators that require combination for significance
- **SIGNAL TYPES": 
  - Linguistic features (word choice, phrasing, typing patterns, language identifiers)
  - Behavioral patterns (posting timing, response latency, activity cycles)
  - Content preferences (topic interests, product categories, interaction patterns)
  - Network positions (centrality measures, bridge roles, community membership)
- **EXTRACTION METHODS": 
  - TF-IDF and embedding-based text representations
  - Time series analysis for activity patterns (Fourier transforms, autocorrelation)
  - Clustering algorithms for preference and behavior grouping
  - Graph analytics for network position calculations (using NetworkX or graph DB)
- **CONFIDENCE": 
  - Context-dependent; individual signals typically low confidence (0.3-0.6)
  - Confidence increases through signal combination and cross-source corroboration
  - Requires weighting based on signal stability and discriminative power

### Entity Resolution Methodologies

#### Probabilistic Record Linkage Framework
- **APPROACH": Implement Fellegi-Sunter theory for probabilistic entity resolution
- **COMPONENTS": 
  - Comparison vectors: field-by-field agreement/disagreement patterns
  - m-probabilities: probability of agreement given true match
  - u-probabilities: probability of agreement given non-match
  - Weight calculation: log2(m/u) for each field comparison
  - Classification thresholds: set based on desired precision/recall tradeoff
- **IMPLEMENTATION": 
  - Use dedupe library or custom implementation
  - Blocking strategies to reduce comparison space (sorted neighborhood, canopy clustering)
  - Active learning for parameter estimation with minimal labeled data
  - Iterative refinement with confidence-based convergence criteria
- **FIELD WEIGHTING EXAMPLES": 
  - PGP fingerprint match: high weight (strong evidence)
  - Exact wallet address match: high weight (strong evidence)
  - Similar username (80%+ string similarity): medium weight
  - Overlapping active hours (timezone-adjusted): low-medium weight
  - Similar writing style (stylometry score >0.8): medium weight (requires validation)
- **VALIDATION": 
  - Precision-recall curves against labeled ground truth
  - False link rate analysis (critical for attribution systems)
  - Sensitivity analysis to parameter variations
  - Bias assessment across different entity types

#### Iterative Resolution with Confidence Propagation
- **APPROACH": Use resolved entities to improve resolution of related records
- **TECHNIQUES": 
  - Transitive closure: if A≈B and B≈C with high confidence, increase A≈C confidence
  - Consistency checking: resolve conflicts through evidence weighting
  - Confidence propagation: update entity attributes based on linked records
  - Temporal consistency: enforce reasonable lifespan and activity patterns
- **IMPLEMENTATION": 
  - Graph-based resolution where entities are nodes and similarities are edges
  - Community detection algorithms for entity clustering
  - Label propagation algorithms for attribute inference
  - Temporal windowing to handle entity evolution over time
- **VALIDATION": 
  - Measure improvement in resolution accuracy over baseline
  - Verify consistency constraints are satisfied
  - Test robustness to noisy or misleading signals

### Stylometry Analysis Methodology

#### Multi-Layer Feature Extraction
- **APPROACH": Combine complementary feature sets for robust authorship attribution
- **FEATURE CATEGORIES": 
  - Lexical: word frequency, vocabulary richness, hapax legomena
  - Syntactic: sentence length, punctuation usage, part-of-speech patterns
  - Character-level: n-gram frequencies (especially effective for short texts)
  - Structural: paragraph organization, formatting preferences, markup usage
  - Semantic: topic modeling, semantic field preferences, lexical diversity
  - Application-specific: emoji usage, leetspeak patterns, community-specific terminology
- **EXTRACTION TECHNIQUES": 
  - Count vectorizers and TF-IDF transformers
  - POS tagging and syntactic parsing (spaCy, Stanza)
  - Character n-gram analysis with various n values (typically 2-5)
  - Readability metrics (Flesch-Kincaid, Gunning Fog, etc.)
  - Custom feature detectors for platform-specific patterns
- **DIMENSIONALITY REDUCTION": 
  - Feature selection based on discriminative power (chi-square, mutual information)
  - PCA or LDA for computational efficiency and noise reduction
  - Embedding-based approaches (sentence-transformers, USE) for semantic similarity

#### Model Selection and Validation Strategy
- **BASELINE MODELS": 
  - Character n-gram + TF-IDF + Linear SVM (strong baseline for text attribution)
  - Word n-gram + TF-IDF + Naive Bayes (computational efficiency baseline)
  - Ensemble of multiple lightweight models for diversity
- **ADVANCED MODELS (if justified)": 
  - Siamese networks for learning similarity functions directly
  - Transformer-based classifiers (BERT, RoBERTa) for contextual understanding
  - Hybrid models combining traditional features with neural representations
- **EVALUATION METRICS": 
  - Accuracy, precision, recall, F1-score (overall and per-class)
  - ROC-AUC for probability calibration assessment
  - False positive rate critical for attribution systems (prevent false accusations)
  - Confidence calibration analysis (do predicted probabilities match empirical rates?)
- **VALIDATION SETS": 
  - Cross-validation within datasets to prevent overfitting
  - Temporal holdout to test robustness to concept drift
  - Cross-topic evaluation to assess topic independence
  - Adversarial testing with known obfuscation techniques
- **UNCERTAINTY QUANTIFICATION": 
  - Probability thresholds for confident attribution decisions
  - Rejection option for low-confidence cases requiring human review
  - Confidence intervals or credible intervals for similarity scores
  - Ensemble variance as proxy for prediction uncertainty

### Behavioral Analysis Methodology

#### Feature Engineering for Behavioral Profiling
- **APPROACH": Extract quantifiable behavioral patterns from activity data
- **FEATURE CATEGORIES": 
  - Temporal: posting frequency, circadian rhythms, burstiness metrics, response latency
  - Communicative: message length distribution, reply patterns, conversation initiation
  - Network: centrality measures, clustering coefficient, tie strength, community participation
  - Economic: transaction frequency, average amounts, fee preferences, counter-party diversity
  - Content: topic distribution, language preferences, media sharing habits, sentiment trends
- **EXTRACTION METHODS": 
  - Time series decomposition for periodicity and trend analysis
  - Markov chains for state transition modeling (e.g., active/inactive states)
  - Graph metrics calculation using NetworkX or graph database analytics
  - Clustering algorithms for behavioral typology identification
  - Statistical moments (mean, variance, skew, kurtosis) for distribution characterization
- **NORMALIZATION": 
  - Z-score normalization within entity time windows for comparison
  - Min-max scaling for bounded feature interpretation
  - Robust scaling using percentiles for outlier resistance
  - Entity-baseline comparison for detecting deviations from normal behavior

#### Similarity and Anomaly Detection Approaches
- **APPROACH": Compare entities based on behavioral profiles and detect deviations
- **SIMILARITY MEASURES": 
  - Cosine similarity or Euclidean distance on normalized feature vectors
  - Dynamic Time Warping (DTW) for temporal pattern comparison with timing flexibility
  - Earth Mover's Distance (EMD) for histogram-based feature comparison
  - Mutual information for nonlinear dependency detection
  - Custom weighted combinations based on feature discriminative power
- **ANOMALY DETECTION": 
  - Isolation Forests or One-Class SVMs for outlier detection in feature space
  - Local Outlier Factor (LOF) for density-based anomaly detection
  - Reconstruction error from autoencoders or PCA for novelty detection
  - Statistical process control charts for temporal anomaly detection
  - Hybrid approaches combining multiple anomaly indicators
- **TEMPORAL MODELING": 
  - Hidden Markov Models for inferring latent behavioral states
  - Change point detection for identifying significant behavior shifts
  - Survival analysis for predicting time to next event or state change
  - Recurrent Neural Networks (LSTM/GRU) for sequence modeling (if data sufficient)
- **VALIDATION": 
  - Known behavior change events (market migrations, platform switches)
  - Synthetic behavior injection with controlled ground truth
  - Expert review of detected anomalies for plausibility
  - False positive rate analysis in stable behavioral periods

### Infrastructure Correlation Methodology

#### Passive Infrastructure Evidence Collection
- **APPROACH": Gather infrastructural indicators without active probing or interaction
- **EVIDENCE TYPES": 
  - SSL/TLS certificates: subject, issuer, validity period, SANs, key strength, protocol versions
  - DNS records: A, AAAA, CNAME, MX, TXT records and historical changes
  - HTTP headers: server tokens, powered-by indicators, caching policies, security headers
  - Service banners: version strings, protocol indicators, configuration snippets
  - Network artifacts: ASN information, geolocation (with accuracy disclaimers), hosting provider
  - Metadata: file metadata, template identifiers, framework fingerprints
- **COLLECTION TECHNIQUES": 
  - Passive SSL/TLS scanning of discovered services (when ethically permissible)
  - DNS query monitoring from public resolvers (when authorized)
  - Web scraping of service interfaces with minimal interaction
  - Certificate Transparency log monitoring for certificate issuance events
  - Passive collection of publicly available network information (RIPE, ARIN, etc.)
- **RATE LIMITING AND ETIQUETTE": 
  - Respectful scanning rates to avoid disruption
  - Clear identification and contact information when interaction occurs
  - Compliance with robots.txt and terms of service
  - Avoidance of techniques that could be interpreted as hostile

#### Correlation and Attribution Scoring
- **APPROACH": Measure similarity between infrastructure profiles with evidence weighting
- **CORRELATION FACTORS": 
  - Certificate sharing: identical or related certificates (same issuer, key, validity)
  - Domain similarity: typosquatting, related registration information, shared DNS infrastructure
  - Service similarity: identical or version-related software, configuration patterns
  - Network proximity: same ASN, hosting provider, or IP neighborhood (with caveats)
  - Header consistency: similar HTTP responses, security headers, or server behaviors
  - Temporal correlation: overlapping validity periods or concurrent changes
- **SCORING METHODOLOGY": 
  - Binary matches (exact certificate): high weight, high confidence
  - Fuzzy matches (similar domains, related ASNs): medium weight, context-dependent confidence
  - Negative evidence (contradicting infrastructure): reduces confidence in linkage
  - Temporal decay: older evidence weighted less unless recently re-confirmed
  - Source reliability weighting: evidence from authoritative sources weighted higher
- **CONFIDENCE CALIBRATION": 
  - Empirical false positive rate measurement against known unrelated services
  - Baseline correlation rate estimation in population of services
  - Bayesian updating with prior probability of random correlation
  - Threshold setting based on desired operational precision/recall targets
- **LIMITATIONS AND CAVEATS": 
  - Shared infrastructure ≠ common ownership (CDNs, hosting providers, shared services)
  - Dynamic IP allocation and cloud services complicate persistence-based correlation
  - Privacy services and proxies intentionally obscure infrastructure links
  - Requires combination with other evidence types for meaningful attribution
  - Must avoid creating false determinism from probabilistic infrastructure similarities

### Attribution Confidence Modeling

#### Evidence-Based Confidence Aggregation
- **APPROACH": Combine multiple evidence streams using principled uncertainty framework
- **MODEL FRAMEWORK": 
  - Dempster-Shafer Theory: handles uncertainty and ignorance explicitly
  - Bayesian Network: models dependencies between evidence and hypothesis
  - Weighted Voting: simple aggregation with evidence-based weights
  - Logistic Regression: learns optimal combination from training data
- **CHOICE CRITERIA": 
  - Explainability: ability to trace confidence to specific evidence sources
  - Uncertainty handling: distinguishes between conflicting evidence and missing evidence
  - Calibration: predicted confidence matches empirical accuracy
  - Update efficiency: incremental incorporation of new evidence
  - Robustness: graceful degradation with partial or noisy evidence
- **RECOMMENDED APPROACH": 
  - Dempster-Shafer for initial implementation (strong theoretical grounding, explainability)
  - Evaluate Bayesian approach if dependencies between evidence types are significant
  - Consider hybrid approach for production scalability

#### Evidence Dimensionality and Weighting
- **EVIDENCE DIMENSIONS": 
  - Source Reliability: trustworthiness and authority of information source
  - Directness: how directly evidence links to attribution hypothesis (direct vs circumstantial)
  - Independence: degree to which evidence is uncorrelated with other evidence
  - Specificity: how uniquely evidence points to particular actor vs general population
  - Temporal Consistency: alignment of evidence timing with hypothesized activity period
  - Corroboration: number and quality of independent sources supporting same conclusion
  - Contradiction: evidence that challenges or undermines the attribution hypothesis
- **WEIGHTING APPROACH": 
  - Expert elicitation or machine learning to determine dimension importance
  - Dynamic weighting based on evidence context and quality metrics
  - Discounting factors for potential deception or manipulation
  - Time-based decay for evidence relevance
  - Source-specific reliability scores based on historical accuracy
- **CONFIDENCE CALIBRATION": 
  - Platt scaling or isotonic regression for probability calibration
  - Reliability diagrams and Brier score for calibration assessment
  - Threshold selection based on operational cost-benefit analysis
  - Confidence intervals or credible intervals for uncertainty quantification
  - Regular recalibration against validated ground truth cases

#### Attribution Reporting and Explainability
- **APPROACH": Provide transparent, actionable attribution results for investigators
- **REPORT COMPONENTS": 
  - Hypothesis Statement: specific attribution claim being evaluated
  - Evidence Summary: enumerated evidence items supporting and contradicting hypothesis
  - Confidence Score: aggregated confidence with uncertainty bounds
  - Evidence Breakdown: contribution of each evidence dimension to final score
  - Alternative Hypotheses: competing explanations with their confidence scores
  - Data Gaps: missing evidence that would increase confidence if available
  - Recommendations: suggested next steps for investigation or validation
  - Provenance Tracking: complete trace from raw data to final confidence score
- **VISUALIZATION APPROACHES": 
  - Evidence timeline showing when and how evidence was collected
  - Confidence contribution waterfall chart
  - Hypothesis comparison matrix
  - Evidence network showing relationships and contradictions
  - Temporal evolution of confidence as evidence accumulates
- **INVESTIGATOR WORKFLOW SUPPORT": 
  - Hypothesis tracking and versioning as investigation evolves
  - Evidence bookmarking and annotation capabilities
  - Collaboration features for team-based investigation
  - Export capabilities for reporting and handoff
  - Integration with case management systems

### Implementation Guidelines and Best Practices

#### Modular Architecture Principles
- **APPROACH": Design loosely coupled, highly cohesive components for maintainability
- **MODULE RESPONSIBILITIES": 
  - Collectors: responsible for data acquisition from specific sources
  - Normalizers: responsible for format standardization and basic validation
  - Extractors: responsible for identifying entities and relationships in data
  - Resolution: responsible for determining when records refer to same real-world entity
  - Analyzers: responsible for deriving insights (stylometry, behavior, infrastructure)
  - Fusion: responsible for combining evidence into attribution hypotheses
  - Presentation: responsible for delivering results to users in actionable form
- **INTERFACE DESIGN": 
  - Well-defined input/output schemas using JSON or Protocol Buffers
  - Asynchronous communication where appropriate (message queues, event streaming)
  - Error handling and degradation strategies for partial failures
  - Versioned interfaces to support independent component evolution
  - Health checking and monitoring endpoints for operational oversight

#### Scalability and Performance Considerations
- **APPROACH": Design for achievable performance within student project constraints
- **SCALABILITY TARGETS": 
  - Handle synthetic lab data efficiently (100s-1000s of entities)
  - Support demonstration-scale real data (1000s-10,000s of records)
  - Enable reasonable response times for investigative queries (<5s for typical queries)
  - Allow batch processing for background analytics and model training
- **OPTIMIZATION TECHNIQUES": 
  - Indexing strategies for frequent query patterns (entity lookup, time range, source filtering)
  - Caching layers for expensive computations (similarity scores, graph traversals)
  - Asynchronous processing for non-interactive tasks (model training, report generation)
  - Resource pooling for database connections and external API calls
  - Progressive enhancement: basic functionality first, advanced features as performance allows
- **PERFORMANCE MONITORING": 
  - Instrument key operations with timing and resource usage metrics
  - Track queue lengths and processing latencies
  - Monitor error rates and degradation patterns
  - Set performance budgets for different operation types
  - Regular profiling to identify and address bottlenecks

#### Ethical and Legal Compliance by Design
- **APPROACH": Build compliance considerations into architecture and workflows
- **DATA HANDLING": 
  - Purpose limitation: use data only for stated attribution research purposes
  - Data minimization: collect and retain only necessary information
  - Storage limitation: define retention periods and secure disposal procedures
  - Security protection: appropriate technical and organizational measures
  - Transparency: document data flows, processing, and sharing practices
- **USER INTERFACE SAFEGUARDS": 
  - Purpose reminders: clear indication of authorized use cases
  - Access logging: track who accessed what data and when
  - Usage monitoring: detect potential misuse patterns
  - Content warnings: flag sensitive or potentially disturbing material
  - Export controls: restrict or audit sensitive data exports
- **GOVERNANCE FEATURES": 
  - Audit trails: comprehensive logging of system access and operations
  - Approval workflows: for sensitive operations or data sharing requests
  - Data quality metrics: monitor for degradation or contamination
  - Bias detection: assess for unfair or discriminatory patterns in results
  - Regular review: periodic assessment of compliance and effectiveness

This methodology document provides a comprehensive framework for implementing the SIH26151 dark web threat actor de-anonymization platform with scientific rigor, technical soundness, and ethical responsibility.