# Tools Survey
## SIH26151 — Dark web threat actor de-anonymization

### Onion Services Analysis Tools

#### OnionScan
- **SOURCE**: https://github.com/s-rah/onionscan
- **CLAIM**: Open-source tool for analyzing Tor hidden services for security misconfigurations and vulnerabilities
- **EVIDENCE**: 
  - Actively maintained GitHub repository
  - Used in academic research on Tor hidden service security
  - Tests for: server-status exposure, SSL certificate issues, default banners, descriptor inconsistencies
- **RELEVANCE**: Directly addresses requirement #2 (Infrastructure analysis of Tor hidden services)
- **IMPLEMENTATION IMPLICATION**: Can be used as a collector module or reference for building passive infrastructure analysis

#### OnionScout
- **SOURCE**: Various security research publications
- **CLAIM**: Framework for discovering and analyzing Tor hidden services
- **EVIDENCE**: 
  - Referenced in papers on hidden service discovery
  - Focuses on service enumeration and metadata collection
- **RELEVANCE**: Infrastructure analysis and discovery
- **IMPLEMENTATION IMPLICATION**: Inspiration for service discovery collectors

#### Caronte
- **SOURCE**: Security research tools
- **CLAIM**: Tool for analyzing Tor hidden services and their relationships
- **EVIDENCE**: 
  - Mentioned in Tor security research contexts
  - Focuses on service correlation and mapping
- **RELEVANCE**: Infrastructure correlation and hidden service analysis
- **IMPLEMENTATION IMPLICATION**: Reference for correlation algorithms

### Threat Intelligence Platforms

#### Maltego
- **SOURCE**: https://www.maltego.com/
- **CLAIM**: Commercial threat intelligence platform with graph-based visualization and entity resolution
- **EVIDENCE**: 
  - Widely used in cybersecurity industry
  - Supports OSINT, threat intelligence, and forensic investigations
  - Uses transforms for data enrichment and entity resolution
- **RELEVANCE**: Graph-based CTI, entity resolution, visualization (requirements #3, #5)
- **IMPLEMENTATION IMPLICATION**: Reference for graph engine design and entity resolution workflows

#### OpenCTI
- **SOURCE**: https://www.opencti.io/
- **CLAIM**: Open-source cyber threat intelligence platform
- **EVIDENCE**: 
  - GitHub repository with active community
  - Supports STIX/TAXII standards
  - Provides data model, graph storage, and API
- **RELEVANCE**: STIX/TAXII compliance, graph storage, entity resolution (requirements #3, #5)
- **IMPLEMENTATION IMPLICATION**: Reference for data model, STIX implementation, and graph abstraction

#### MISP
- **SOURCE**: https://www.misp-project.org/
- **CLAIM**: Open-source threat intelligence sharing platform
- **EVIDENCE**: 
  - Widely adopted in security communities
  - Event-based sharing with taxonomies and galaxies
  - Supports correlation and automated threat intelligence feeds
- **RELEVANCE**: Threat intelligence sharing, correlation (requirements #1, #3, #5)
- **IMPLEMENTATION IMPLICATION**: Reference for intelligence sharing and correlation mechanisms

### Cryptocurrency Analysis Tools

#### Chainalysis (Reference)
- **SOURCE**: https://www.chainalysis.com/
- **CLAIM**: Commercial blockchain analysis platform
- **EVIDENCE**: 
  - Industry standard for cryptocurrency investigations
  - Provides address clustering, transaction tracing, and risk scoring
  - Used by law enforcement and financial institutions
- **RELEVANCE**: Cryptocurrency wallet analysis and transaction tracing (requirement #3)
- **IMPLEMENTATION IMPLICATION**: Reference for crypto engine design; MVP should use public blockchain data only

#### Elliptic (Reference)
- **SOURCE**: https://www.elliptic.co/
- **CLAIM**: Commercial blockchain analytics and risk management
- **EVIDENCE**: 
  - Provides transaction monitoring, wallet screening, and regulatory compliance
  - Used by cryptocurrency businesses and financial institutions
- **RELEVANCE**: Cryptocurrency attribution and risk scoring
- **IMPLEMENTATION IMPLICATION**: Reference for future professional API integration

### Graph Database Technologies

#### Neo4j
- **SOURCE**: https://neo4j.com/
- **CLAIM**: Leading commercial graph database with ACID transactions
- **EVIDENCE**: 
  - Widely used in fraud detection, recommendation engines, and knowledge graphs
  - Supports Cypher query language
  - Has desktop and server editions
- **RELEVANCE**: Graph storage and querying for CTI relationships (requirement #5)
- **IMPLEMENTATION IMPLICATION**: Primary candidate for graph engine; evaluate against alternatives

#### Memgraph
- **SOURCE**: https://memgraph.com/
- **CLAIM**: In-memory graph database for real-time applications
- **EVIDENCE**: 
  - Optimized for real-time graph analytics
  - Supports Cypher-compatible querying
  - Open-source core with enterprise features
- **RELEVANCE**: High-performance graph querying
- **IMPLEMENTATION IMPLICATION**: Alternative for real-time analytics requirements

#### ArangoDB
- **SOURCE**: https://www.arangodb.com/
- **CLAIM**: Multi-model database (document, graph, key-value)
- **EVIDENCE**: 
  - Supports AQL (ArangoDB Query Language)
  - Flexible data modeling capabilities
  - Good balance of features and performance
- **RELEVANCE**: Flexible storage for diverse CTI data types
- **IMPLEMENTATION IMPLICATION**: Alternative if multi-model capabilities needed

#### PostgreSQL with Apache Age
- **SOURCE**: https://age.apache.org/
- **CLAIM**: PostgreSQL extension for graph processing
- **EVIDENCE**: 
  - Leverages existing PostgreSQL infrastructure
  - Supports openCypher query standard
  - Reduces operational complexity
- **RELEVANCE**: Graph capabilities with relational database familiarity
- **IMPLEMENTATION IMPLICATION**: Good option for teams with PostgreSQL experience

### Stylometry and Authorship Attribution Tools

#### JGAAP (Java Graphical Authorship Attribution Program)
- **SOURCE**: https://jgaap.sourceforge.io/
- **CLAIM**: Java-based authorship attribution and text analysis software
- **EVIDENCE**: 
  - Academic tool for stylometric analysis
  - Supports various feature sets and classification algorithms
  - Used in literary attribution and forensic linguistics
- **RELEVANCE**: Stylometric persona identification (requirement #4)
- **IMPLEMENTATION IMPLICATION**: Reference for feature extraction and classification approaches

#### Stylo (R Package)
- **SOURCE**: https://github.com/computationalstylistics/stylo
- **CLAIM**: R package for computational stylistics
- **EVIDENCE**: 
  - Actively maintained academic project
  - Implements various stylometric methods
  - Used in literary and forensic authorship attribution
- **RELEVANCE**: Stylometry engine implementation
- **IMPLEMENTATION IMPLICATION**: Reference for algorithms and validation approaches

#### Python Stylometry Libraries
- **SOURCE**: Various GitHub repositories
- **CLAIM**: Python libraries for stylometric analysis
- **EVIDENCE**: 
  - Examples: stylometry, authorship, textdistance
  - Active development in NLP community
  - Easy integration with ML pipelines
- **RELEVANCE**: Stylometric analysis for text posts and communications
- **IMPLEMENTATION IMPLICATION**: Preferred for MVP due to Python ecosystem integration

### Dark Web Crawlers and Collectors

#### darkweb-scraper (Reference)
- **SOURCE**: Various GitHub projects
- **CLAIM**: Frameworks for scraping dark web marketplaces and forums
- **EVIDENCE**: 
  - Examples: Ahmia, Haystak, TorBot
  - Handle Tor proxy rotation, CAPTCHA solving, rate limiting
  - Extract structured data from onion services
- **RELEVANCE**: Continuous collection from marketplaces, forums, deep web (requirement #1)
- **IMPLEMENTATION IMPLICATION**: Reference for collector plugin architecture

#### TorBot
- **SOURCE**: https://github.com/Disorganizer0/TorBot
- **CLAIM**: Python-based Tor reconnaissance and scraping tool
- **EVIDENCE**: 
  - Actively maintained
  - Features: hidden service discovery, data extraction, link analysis
  - Modular design for extensibility
- **RELEVANCE**: Dark web crawling and data collection
- **IMPLEMENTATION IMPLICATION**: Reference for collector design and Tor integration

### Entity Resolution and Record Linkage Tools

#### dedupe
- **SOURCE**: https://datamade.github.io/dedupe/
- **CLAIM**: Python library for accurate deduplication and entity resolution
- **EVIDENCE**: 
  - Uses active learning to reduce labeling effort
  - Supports custom data types and blocking strategies
  - Production-ready with good documentation
- **RELEVANCE**: Entity resolution engine (requirement #3)
- **IMPLEMENTATION IMPLICATION**: Strong candidate for entity resolution service

#### Record Linkage Toolkit
- **SOURCE**: https://recordlinkage.toolkit/
- **CLAIM**: Python library for record linkage and deduplication
- **EVIDENCE**: 
  - Comprehensive set of linkage algorithms
  - Supports probabilistic and deterministic matching
  - Good for tabular data entity resolution
- **RELEVANCE**: Cross-platform entity mapping
- **IMPLEMENTATION IMPLICATION**: Alternative or complement to dedupe

### Summary
This tools survey provides a foundation for selecting appropriate technologies and designing system components. Key insights:

1. **Collection**: Need modular collector plugins supporting Tor, web scraping, and API ingestion
2. **Storage**: Graph database (Neo4j/Memgraph/PostgreSQL+Age) recommended for relationship traversal
3. **Analysis**: Python-based ML stack for stylometry and behavior analysis
4. **Entity Resolution**: Probabilistic approach using libraries like dedupe
5. **Standards**: STIX/TAXII compliance important for interoperability
6. **Visualization**: Graph-based frontend similar to Maltego capabilities

Next steps: Deep dive into academic research (PAPERS.md) and dataset availability (DATASETS.md).